from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"""mongodb+srv://souzavitorchaves:{password}@mongosb.iwcui0b.mongodb.net/?retryWrites=true&w=majority"""

client = MongoClient(connection_string)

dbs = client.list_database_names()
test_db = client.test #this "test" right here is the database in mongodb
collections = test_db.list_collection_names()
#print(collections)

def inserted_test_doc():
    collection = test_db.test
    test_document = {
        "name": "Tim",
        "type": "Test"
    }
    inserted_id = collection.insert_one(test_document)
    print(inserted_id)

# inserted_test_doc()

#__________________________ new DB below

production = client.production
person_colletion = production.person_collection

def create_documents():
    first_names = ["Tim", "Sarah", "Jennifer", "Jose", "Brad", "Allen"]
    last_names = ["Rustica", "Smith", "Bart", "Cater", "Pit", "Geral"]
    ages = [21, 40, 23, 19, 34, 67]

    docs = []

    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {"first_name": first_name, "last_name": last_name, "age": age}
        docs.append(doc)
        #person_collection.insert_one(doc)
    
    person_colletion.insert_many(docs)
    
# create_documents()

printer = pprint.PrettyPrinter()

def find_all_people():
    people = person_colletion.find()

    for person in people:
        printer.pprint(person)

# find_all_people()

def find_tim():
    tim = person_colletion.find_one({"first_name": "Tim"}) 
    # in the query above all the var need to be specific the same as DB and it's like an "and" condition, not "or"
    printer.pprint(tim)

# find_tim()

def count_all_people():
    count = person_colletion.count_documents(filter={})
    # count = person_collection.find().count()
    print("Number of people", count)

# count_all_people()

def get_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)
    person = person_colletion.find_one({"_id": _id})
    printer.pprint(person)

#get_person_by_id("65c6eb7a7869f19a3fccb515")

def get_age_range(min_age, max_age):
    query = {"$and": [
                {"age": {"$gte": min_age}},  # gte = greater than or equal
                {"age": {"$lte": max_age}}   # lte = less than or equal
        ]}
    people = person_colletion.find(query).sort("age")
    for person in people:
        printer.pprint(person)

# get_age_range(20, 35)
        
def project_columns():
    columns = {"_id": 0, "first_name": 1, "last_name": 1} # 0 don't select and 1 does select
    people = person_colletion.find({}, columns)
    for person in people: 
        printer.pprint(person)

project_columns()