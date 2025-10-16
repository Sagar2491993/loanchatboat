import os
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


from RAG_pipeline.gemini_model import load_gemini_model
from RAG_pipeline.prompt import load_prompt_templates


def create_gemini_qa_chain(vectorstore):
    """Create a Retrieval-based QA chain using Gemini model and FAISS vectorstore."""
    try:
        llm = load_gemini_model()
        prompt_text = load_prompt_templates()

        prompt = PromptTemplate(
            template=prompt_text,
            input_variables=["context", "question"]
        )

        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=True
        )

        print(" Gemini QA Chain created successfully!")
        return qa_chain

    except Exception as e:
        print(f" Error creating Gemini QA chain: {e}")
        raise


if __name__ == "__main__":
    print("Run this via main.py, not directly.")
