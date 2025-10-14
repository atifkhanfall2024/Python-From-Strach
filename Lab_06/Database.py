from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

# ✅ MongoDB connection
client = MongoClient(
    "mongodb://muhammadatifkhan:ukjJEVg58zUN3roM@"
    "atifnodejs-shard-00-00.zjo3x.mongodb.net:27017,"
    "atifnodejs-shard-00-01.zjo3x.mongodb.net:27017,"
    "atifnodejs-shard-00-02.zjo3x.mongodb.net:27017/"
    "LLM?ssl=true&replicaSet=atlas-10eloi-shard-0&authSource=admin&retryWrites=true&w=majority"
)

# ✅ Connect to your actual DB
db = client["LLM"]
people = db["people"]
chats = db["chats"]


# ✅ Find a person by ObjectId
def find_person_by_objectid(id_str):
    try:
        oid = ObjectId(id_str)
    except InvalidId:
        print("Invalid ObjectId format")
        return None
    return people.find_one({"_id": oid})


# ✅ Store an AI conversation
def store_chat(question, answer):
    """Stores a chat entry with question & answer."""
    chat_doc = {
        "question": question,
        "answer": answer
    }

    try:
        result = chats.insert_one(chat_doc)
        print(f"💾 Chat saved with ID: {result.inserted_id}")
    except Exception as e:
        print("❌ Error inserting into MongoDB:", e)
