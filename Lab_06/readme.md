# searching fuction by passing two params one is prompt from user other is the k value mean number of docx


mongodb://muhammadatifkhan:ukjJEVg58zUN3roM@atifnodejs-shard-00-00.zjo3x.mongodb.net:27017,atifnodejs-shard-00-01.zjo3x.mongodb.net:27017,atifnodejs-shard-00-02.zjo3x.mongodb.net:27017/Chatbot?ssl=true&replicaSet=atlas-10eloi-shard-0&authSource=admin&retryWrites=true&w=majority



from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
people = db["people"]

def find_person_by_objectid(id_str):
    try:
        oid = ObjectId(id_str)
    except InvalidId:
        print("Invalid ObjectId format")
        return None

    person = people.find_one({"_id": oid})
    return person

# usage
result = find_person_by_objectid("650b9f8b2f1f2a3b4c5d6e7f")
if result:
    # convert _id to string for printing/JSON
    result["_id"] = str(result["_id"])
    print("Found:", result)
else:
    print("Person not found")
