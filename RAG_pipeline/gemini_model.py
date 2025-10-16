import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

def load_gemini_model(model_name="gemini-2.0-flash-exp"):
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file!")
    
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=api_key
    )
    return llm


def ask_gemini_question(llm, question: str):
    response = llm.invoke([HumanMessage(content=question)])
    return response.content


if __name__ == "__main__":
    llm = load_gemini_model()
    answer = ask_gemini_question(llm, "tell me how to create biryanni?")
    print("Gemini response:")
    print(answer)
