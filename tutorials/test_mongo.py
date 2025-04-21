from pymongo import MongoClient

# Replace <username>, <password>, and <dbname> with actual values
uri = "mongodb+srv://pankajv91505:PankajVerma3110@cluster0.3g9qmiy.mongodb.net/"

try:
    client = MongoClient(uri)
    # List database names to check if connection is successful
    databases = client.list_database_names()
    print("✅ Connection successful!")
    print("📂 Databases:", databases)
except Exception as e:
    print("❌ Connection failed:")
    print(e)
