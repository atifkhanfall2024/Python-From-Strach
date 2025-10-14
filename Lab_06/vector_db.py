# from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_chroma import Chroma
from typing import List
from langchain_core.documents import Document
from uuid import uuid4
from dotenv import load_dotenv
import os 
import shutil

load_dotenv()

class VectorDatabase():
    def __init__(self):
        # self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

        self.vector_db = Chroma(
            collection_name="hydrogenfuel",
            embedding_function=self.embeddings,
            persist_directory="./vectordb"
        )

    def delete_chroma(self,path="./vectordb"):
        if os.path.exists(path):
            shutil.rmtree(path)


    def loader(self, documents: List[Document], fresh_load :bool = False):
        if fresh_load:
            self.delete_chroma()
        
        uuids = [str(uuid4()) for item in range(len(documents))]
        self.vector_db.add_documents(documents=documents,ids=uuids)


    def search(self, question:str, k:int =3):
        results = self.vector_db.similarity_search(question,k)

        combined_results = ""

        for item in results:
            combined_results += item.page_content
            combined_results += "\n"

        return combined_results