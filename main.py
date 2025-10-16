import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from RAG_pipeline.chunk import load_and_create_chunks
from RAG_pipeline.chain import create_gemini_qa_chain
from RAG_pipeline.gemini_model import load_gemini_model
from RAG_pipeline.prompt import load_prompt_templates
from RAG_pipeline.cache import ResponseCache  


def load_documents(data_folder):
    docs = []
    for file in os.listdir(data_folder):
        file_path = os.path.join(data_folder, file)
        if file.endswith(".txt"):
            loader = TextLoader(file_path, encoding="utf-8")
        else:
            print(f" Skipping unsupported file type: {file}")
            continue
        docs.extend(loader.load())
    print(f" Loaded {len(docs)} documents from {data_folder}")
    return docs

def split_documents(docs, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(docs)
    print(f" Split into {len(chunks)} text chunks.")
    return chunks

def create_vector_store(chunks, embedding_model="sentence-transformers/all-MiniLM-L6-v2"):
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
    vectorstore = FAISS.from_documents(chunks, embedding=embeddings)
    print(" FAISS vector store created successfully!")
    return vectorstore

def main():
    try:
        load_dotenv()
        data_folder = r"D:\Sagar\bank of maharashtra loans gen ai project\loans data"

        cache = ResponseCache()

        docs = load_documents(data_folder)
        chunks = split_documents(docs)

        vectorstore = create_vector_store(chunks)

        qa_chain = create_gemini_qa_chain(vectorstore)

        while True:
            query = input("\n Ask a question (or type 'exit' to quit): ")
            if query.lower() in ["exit", "quit"]:
                print(" Exiting the chatbot. Goodbye!")
                break

            cached_answer = cache.get(query)
            if cached_answer:
                print("\n Answer (from cache):", cached_answer)
                continue

            response = qa_chain.invoke({"query": query})
            answer = response["result"]
            print("\n Answer (from Gemini):", answer)

            cache.add(query, answer)

    except Exception as e:
        print(f"Error in main pipeline: {e}")

if __name__ == "__main__":
    main()
