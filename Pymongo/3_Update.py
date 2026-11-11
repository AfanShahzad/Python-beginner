from pymongo import MongoClient  # type: ignore

# Create a connection to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

db = client["store"]
books = db["books"]

# Update a single record
books.update_one(
    {"title": "The Great Gatsby"},  # Filter to find the record
    {"$set": {"year": 1926}}  # Update operation to set the year to 1926
)

# Update multiple records
books.update_many(
    {"year": {"$gt": 1930, "$lt": 1965}},  # Filter to find records with year between 1930 and 1965
    {"$set": {"classic": True}}  # Update operation to set the classic field to True
)

# push a new genre to the genres array for a specific book
books.update_one(
    {"title": "1984"},  # Filter to find records with title 1984
    {"$push": {"genres": "philosophy"}}  # Update operation to add philosophy to the genres array
)

# MongoDB does not allow changing the immutable _id field. Store sequential IDs
# in a separate field instead, ordered by the existing _id.
for i, book in enumerate(books.find({}).sort("_id")):
    books.update_one(
        {"_id": book["_id"]},
        {"$set": {"record_id": i}}
    )