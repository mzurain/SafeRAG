from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

# Load documents
loaders = [
    PyPDFLoader("./administrative_doc.pdf"),
    TextLoader("./NCBKSAJE.txt"),
]
docs = []
for loader in loaders:
    docs.extend(loader.load())

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

# Store in ChromaDB
embedding = OllamaEmbeddings(model="nomic-embed-text:latest")
vectorstore = Chroma(
    collection_name="knowledge_base",
    embedding_function=embedding,
    persist_directory="./chroma_db",
)
vectorstore.add_documents(chunks)
print(f"Done. {len(chunks)} chunks ingested into ChromaDB.")
