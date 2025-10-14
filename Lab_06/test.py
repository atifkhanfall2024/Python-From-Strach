from pdf_handler import PDF_Handler
from vector_db import VectorDatabase


# pdf_handler = PDF_Handler("./HydrogenFuel.pdf")

# chunks = pdf_handler.load_docs()

vector = VectorDatabase()

# vector.loader(chunks)
print(vector.search("hydrogen"))