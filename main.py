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
print(collections)

