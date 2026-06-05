from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def build_catalog(pdf_path):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    db = Chroma.from_documents(
        chunks,
        embedding,
        persist_directory="chroma_db"
    )

    db.persist()

def search_catalog(query):

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding
    )

    docs = db.similarity_search(
        query,
        k=4
    )

    return "\n".join(
        d.page_content
        for d in docs
    )