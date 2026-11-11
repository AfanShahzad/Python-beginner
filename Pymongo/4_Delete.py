from pymongo import MongoClient  # type: ignore

# Create a connection to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

db = client["store"]
books = db["books"]

#insert three sample records to delete
books.insert_one({"title": "Business", "author": "John Doe", "year": 2020})
books.insert_one({"title": "Truth", "author": "Jane Smith", "year": 2021})
books.insert_one({"title": "1984", "author": "George Orwell", "year": 1948})

# Delete a single record
books.delete_one({"title": "1984", "record_id": {"$exists": False}})

# Delete multiple records
books.delete_many({"year": {"$gt": 2019}})