from flask import Flask,render_template,jsonify,request
from transformers import pipeline
from src.helper import download_hugging_face_embeddings
from langchain_huggingface import HuggingFacePipeline
from langchain.chains import create_retrieval_chain
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import Document, BaseRetriever
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
 
embeddings = download_hugging_face_embeddings()

index_name = "medicalbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retrieve = docsearch.as_retriever(search_type = "similarity",search={"k":3})

pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-large",
    max_new_tokens=150,
    device=-1
)

llm = HuggingFacePipeline(pipeline=pipe)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

qa_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retrieve, qa_chain)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get",methods = ["GET","POST"])
def chat():
    msg = request.form["msg"] 
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ",response["answer"])
    return str(response["answer"])


if __name__ =='__main__':
    app.run(host = "0.0.0.0",port = 8080 , debug = False)


