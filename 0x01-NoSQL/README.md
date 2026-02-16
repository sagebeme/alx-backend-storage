# 0x01. NoSQL (MongoDB)

This project uses **MongoDB** and **Python (PyMongo)** to work with documents: listing databases, inserting, finding, updating, deleting, and running aggregations (e.g. logs, schools by topic).

---

## What does each file do?

Each answer is the **problem the file solves** and how to run it. Files without a `.py` extension are **Mongo shell** scripts; `.py` files are **Python** scripts.

---

### Mongo shell scripts (run with `mongosh` or `mongo`)

### **What does `0-list_databases` do?**  
It **lists all databases** in the MongoDB server (e.g. `show dbs`). You learn how to connect and run a basic command.  
**Run:** `mongosh < 0-list_databases` or paste in Mongo shell.

### **What does `1-use_or_create_database` do?**  
It **switches to a database** (and creates it if it doesn’t exist) with `use <dbname>`.  
**Run:** Paste in Mongo shell.

### **What does `2-insert` do?**  
It **inserts a document** into a collection (e.g. `db.schools.insertOne({...})`).  
**Run:** Paste in Mongo shell after selecting a database.

### **What does `3-all` do?**  
It **finds all documents** in a collection (e.g. `db.collection.find()`).  
**Run:** Paste in Mongo shell.

### **What does `4-match` do?**  
It **finds documents** that match a given filter (e.g. `db.collection.find({ field: value })`).  
**Run:** Paste in Mongo shell.

### **What does `5-count` do?**  
It **counts documents** in a collection, optionally with a match filter.  
**Run:** Paste in Mongo shell.

### **What does `6-update` do?**  
It **updates documents** (e.g. add or rename fields) using update operators.  
**Run:** Paste in Mongo shell.

### **What does `7-delete` do?**  
It **deletes documents** that match a given filter.  
**Run:** Paste in Mongo shell.

### **What does `100-find` do?**  
It **finds documents** with a specific filter (e.g. by attribute).  
**Run:** Paste in Mongo shell.

---

### Python scripts (PyMongo)

### **What does `8-all.py` do?**  
It **lists all documents** in a collection. Typically defines a function that takes a collection and returns `list(collection.find())`.  
**Run:** Use from REPL or run `8-main.py` if present.

### **What does `9-insert_school.py` do?**  
It **inserts one document** into a school collection; takes `mongo_collection` and `**kwargs`, inserts and returns the **inserted_id**.  
**Run:** Import and call with a collection and keyword args, or use a small main.

### **What does `10-update_topics.py` do?**  
It **updates all schools** matching a given name by setting their **topics** array. You practice `update_many` and `$set`.  
**Run:** `python3 10-main.py` (or equivalent).

### **What does `11-schools_by_topic.py` do?**  
It **finds schools** that have a given topic in their `topics` array (e.g. `find({ "topics": topic })`).  
**Run:** `python3 11-main.py` or import and call.

### **What does `12-log_stats.py` do?**  
It runs an **aggregation** on a logs collection (e.g. count by method, status) and prints or returns the stats.  
**Run:** `python3 12-log_stats.py` (ensure MongoDB has the logs data, e.g. from `dump/logs`).

### **What does `101-students.py` do?**  
It runs an **aggregation** on a students collection (e.g. group by grade or project).  
**Run:** `python3 101-main.py` or equivalent.

### **What does `102-log_stats.py` do?**  
It extends log statistics (e.g. top IPs, status distribution) using aggregation pipeline stages.  
**Run:** `python3 102-log_stats.py`.

---

### Other

### **What is `dump/logs/` (and `nginx.metadata.json`)?**  
Sample or real **log data** (and collection metadata) for loading into MongoDB and used by `12-log_stats.py` and `102-log_stats.py`.

### **What are the `*-main.py` files?**  
**Driver scripts** that create a Mongo client, get a database/collection, and call the task functions so you can run and test them.

---

## How to do the exercises yourself

1. Install MongoDB and start the server; install PyMongo: `pip install pymongo`.
2. For shell tasks: open `mongosh`, switch to a DB, create a collection, then run the commands in the script.
3. For Python: get a client and collection, then call the task functions with the collection and required arguments.
4. For aggregation: use `collection.aggregate([...])` with `$match`, `$group`, `$sort`, `$project`, etc.
