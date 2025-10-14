import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Make sure your .env file has this:
# GEMINI_API_KEY=your_google_api_key_here

def call_openai_api2(question):
    llm = ChatOpenAI(
        model="gemini-2.0-flash",
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=os.environ.get("GEMINI_API_KEY"),
        temperature=0.7
    )

    response = llm.invoke(question)
    print("AI Response:", response.content)


if __name__ == "__main__":
    question = input("Enter your question: ")
    call_openai_api2(question)
