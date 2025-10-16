from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def create_faiss_store(docs, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    
    # Create FAISS vector store
    store = FAISS.from_texts(docs, embedding_model)
    print("FAISS vector store created successfully!")
    return store

def search_faiss_store(store, query, k=2):
    results = store.similarity_search(query, k=k)
    return [doc.page_content for doc in results]


if __name__ == "__main__":
    docs = [
        "Delhi is the capital of India",
        "Kolkata is the capital of West Bengal",
        "Paris is the capital of France"
    ]
    
    store = create_faiss_store(docs)
    query = "Which city is the capital of France?"
    results = search_faiss_store(store, query)
    
    print("Query results:")
    for r in results:
        print(r)
