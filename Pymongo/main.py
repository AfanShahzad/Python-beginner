from pymongo import MongoClient  # type: ignore
import json
uri = "mongodb://localhost:27017/"

try:
    # Initialize the client
    client = MongoClient(uri)
    
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("Successfully connected to MongoDB!\n_________________________________________")
    
except Exception as e:
    print(f"Connection failed: {e}")
    
db = client.get_database("ecommerce")
print(json.dumps(list(db.sales.find()), indent=4, default=str))
# for record in db.sales.find():
#     print(record)