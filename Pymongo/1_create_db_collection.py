from pymongo import MongoClient  # type: ignore

# Create a connection to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Create a new database and collection
db = client["store"]
books = db["books"]

client.drop_database("store")  # Drop the database if it already exists

data = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year":1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Pride and Prejudice", "author": "George Orwell", "year": 1973},
]

# Insert the data into the collection
books.insert_many(data)