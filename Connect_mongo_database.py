from pymongo import MongoClient

# Connect to the MongoDB server running on localhost
client = MongoClient("your mongoDb link id")

# Access a specific database
db = client['mydatabase']

# Access a specific collection within the database
collection = db['mycollection']

# Insert a document into the collection
new_document = {
    'name': 'John Doe',
    'age': 30,
    'email': 'john@example.com'
}
inserted_document = collection.insert_one(new_document)
print('Inserted document ID:', inserted_document.inserted_id)

# Find and print all documents in the collection
print('All documents in the collection:')
for document in collection.find():
    print(document)

# Find and print documents that match a specific query
query = {'age': {'$gt': 25}}  # Find documents where age is greater than 25
print('Documents with age greater than 25:')
for document in collection.find(query):
    print(document)

# Close the connection to the MongoDB server
client.close()
