from pymongo import MongoClient  # type: ignore

# Create a connection to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

db = client["store"]
books = db["books"]

print("\nAll records:")
for record in books.find():
    print(record)

filters = [
    ({"By title"},{"title": "The Great Gatsby"}, None),
    ({"by author"},{"author": "George Orwell"}, None),
    ({"by year range"},{"year": {"$gt": 1930, "$lt": 1965}}, None),
    ({"specific fields to return"},{}, {"title": 1, "author": 1, "_id": 0}),
]

for label, query, projection in filters:
    print(f"\nFilter: {label}")
    for record in books.find(query, projection):
        print(record)