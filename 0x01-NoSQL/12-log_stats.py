from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()
db = client.logs
collection = db.nginx

# Get total number of logs
total_logs = collection.count_documents({})

# Get counts for each HTTP method
http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in http_methods}

# Get count for method=GET and path=/status
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

# Display the results
print(f"{total_logs} logs")
print("Methods:")
for method in http_methods:
    print(f"    method {method}: {method_counts[method]}")
print(f"{status_check_count} status check")
