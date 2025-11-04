import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
load_dotenv()

def call_openai_api(question):
    client = OpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=os.environ.get("GEMINI_API_KEY")
    )
    response = client.chat.completions.create(
        temperature=0.7,
        model="gemini-2.0-flash",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )
    print(response.choices[0].message.content)

def call_openai_api2(question):
    response = ChatOpenAI(
        model="gemini-2.0-flash",
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=os.environ.get("GEMINI_API_KEY")

    ).invoke(question)

    print(response.content)

call_openai_api2(input("Enter your question: "))
