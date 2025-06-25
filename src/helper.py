from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings


def loader_file(file):
    loader = DirectoryLoader(file,glob = "*.pdf",loader_cls=PyPDFLoader)
    document = loader.load()
    return document

def textsplit(data):
    text_split = RecursiveCharacterTextSplitter(chunk_size = 500 , chunk_overlap = 20)
    text_chunk = text_split.split_documents(data)
    return text_chunk

def download_hugging_face_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings
