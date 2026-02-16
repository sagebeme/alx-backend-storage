# ALX Backend — Storage

## Description

Backend storage track: **MySQL (advanced)**, **MongoDB (NoSQL)**, and **Redis**. Each folder is a separate project. This README explains **what each file does** and **how to run the exercises** so you can follow or redo them yourself.

## Structure

* [0x00. MySQL Advanced](./0x00-MySQL_Advanced)
* [0x01. NoSQL (MongoDB)](./0x01-NoSQL)
* [0x02. Redis basic](./0x02-redis_basic)

| Folder | Topic | What you'll practice |
|--------|--------|----------------------|
| [0x00-MySQL_Advanced](./0x00-MySQL_Advanced) | MySQL advanced | Constraints, indexes, triggers, procedures, views |
| [0x01-NoSQL](./0x01-NoSQL) | MongoDB | Documents, collections, queries, aggregation |
| [0x02-redis_basic](./0x02-redis_basic) | Redis | Caching, key-value ops, expiring keys |

---

## Prerequisites

- **MySQL** 5.7+ (or 8.0) for `0x00-MySQL_Advanced`
- **MongoDB** for `0x01-NoSQL` (scripts are Python 3 + PyMongo)
- **Redis** server for `0x02-redis_basic` (Python 3 + `redis`, `requests`)

---

## 0x00 — MySQL Advanced

**Problem:** Real databases need uniqueness, indexes, automatic updates (triggers), reusable logic (stored procedures), and safe defaults (e.g. valid email). This project practices writing SQL that does that.

### Files and what they solve

| File | Problem solved | How to run |
|------|----------------|------------|
| `0-uniq_users.sql` | Table `users` with unique email | Load in MySQL, then run table creation |
| `1-country_users.sql` | Users table with country attribute | Same as above |
| `2-fans.sql` | Rank band origins by total fans | Run against DB with `metal_bands` |
| `3-glam_rock.sql` | List glam rock bands (formed 1969–1972, lifespan) | Query on bands table |
| `4-store.sql` | Trigger: decrease quantity on new order | Uses init script; then run trigger + store logic |
| `4-init.sql` | Schema for store (items, orders) | Load before `4-store.sql` |
| `5-valid_email.sql` | Trigger: reset email to NULL if invalid | Keeps email valid on update |
| `5-init.sql` | Users table for valid_email trigger | Load before `5-valid_email.sql` |
| `6-bonus.sql` | Stored procedure: add bonus | Run in MySQL client |
| `6-init.sql` | Schema for bonus project | Load before `6-bonus.sql` |
| `7-average_score.sql` | Stored procedure: compute user average score | Run in MySQL client |
| `7-init.sql` | Schema for users and corrections | Load before `7-average_score.sql` |

### Doing the exercises yourself

1. Create a database and load the relevant `*-init.sql` when a task depends on it.
2. Run the task script (e.g. `mysql -u root -p db < 2-fans.sql` or paste in MySQL client).
3. For triggers/procedures: ensure the table exists and column names match the spec.

Example:

```bash
mysql -u root -p < 0x00-MySQL_Advanced/0-uniq_users.sql
mysql -u root -p mydb < 0x00-MySQL_Advanced/2-fans.sql
```

---

## 0x01 — NoSQL (MongoDB)

**Problem:** Document stores use collections and JSON-like documents instead of fixed tables. This project uses **MongoDB** and **Python (PyMongo)** to list DBs, insert/find/update/delete documents, and run aggregation (e.g. logs, schools by topic).

### Executables (Mongo shell or scripts)

These are **Mongo shell** scripts (run with `mongosh` or `mongo`):

| File | Problem solved | How to run |
|------|----------------|------------|
| `0-list_databases` | List all databases | `mongosh < 0-list_databases` or paste in shell |
| `1-use_or_create_database` | Switch to/create a database | Same |
| `2-insert` | Insert a document | Same |
| `3-all` | Find all documents in a collection | Same |
| `4-match` | Find with a match filter | Same |
| `5-count` | Count documents (optionally with match) | Same |
| `6-update` | Update documents (e.g. add/rename fields) | Same |
| `7-delete` | Delete documents matching a filter | Same |
| `100-find` | Find with filter (e.g. by attribute) | Same |

### Python scripts (PyMongo)

| File | Problem solved | How to run |
|------|----------------|------------|
| `8-all.py` | List all documents in a collection | `python3 8-main.py` (if main exists) or import and call |
| `9-insert_school.py` | Insert one document into `school` collection; returns `inserted_id` | Use from REPL or a small main that gets collection and calls `insert_school(coll, name="...", ...)` |
| `10-update_topics.py` | Update all schools matching name by setting `topics` array | `python3 10-main.py` |
| `11-schools_by_topic.py` | Find schools that have a given topic in `topics` | `python3 11-main.py` or equivalent |
| `12-log_stats.py` | Aggregation on logs: count by method, status, etc. | `python3 12-log_stats.py` (uses `dump/logs` or similar) |
| `101-students.py` | Aggregation on students (e.g. by grade or project) | `python3 101-main.py` |
| `102-log_stats.py` | Extended log stats (e.g. top IPs, status distribution) | `python3 102-log_stats.py` |

### Doing the exercises yourself

1. Install MongoDB and start the server; install PyMongo: `pip install pymongo`.
2. For Mongo shell tasks: open `mongosh`, switch to a DB, create a collection, then run the commands in the script (e.g. `db.schools.insertOne({...})`, `db.schools.find(...)`).
3. For Python: get a client and collection, e.g. `client = MongoClient(); db = client.my_db; coll = db.schools`, then call the task functions with `coll` and the required arguments.
4. For aggregation: use `collection.aggregate([...])` with `$match`, `$group`, `$sort`, `$project`, etc.

---

## 0x02 — Redis basic

**Problem:** Caching HTTP responses avoids repeated requests to the same URL and speeds up the app. This project uses **Redis** to store and count URL fetches and to cache page content with a TTL.

### Files and what they solve

| File | Problem solved | How to run |
|------|----------------|------------|
| `web.py` | `get_page(url)`: fetch URL, cache HTML in Redis (10s TTL), count requests per URL with `count:{url}` | Run Redis; then `python3 -c "from web import get_page; print(get_page('http://example.com'))"` or use in a small app |
| `exercise.py` | Redis exercises (get/set/incr, etc.) | Run with Redis server: `python3 exercise.py` (if it has a main) or run snippets in REPL |
| `0-main.py` | Example/demo for Redis usage | `python3 0-main.py` (Redis must be running) |

### Concepts

- **Keys:** e.g. `cached:{url}` for HTML body, `count:{url}` for request count.
- **Expiry:** `redis.setex(key, 10, value)` caches for 10 seconds.
- **Decorator:** `wrap_requests` wraps `get_page` so that every call uses Redis for cache and increment.

### Doing the exercises yourself

1. Install Redis and start it: `redis-server`. Install: `pip install redis requests`.
2. Implement a decorator that: (a) increments `count:{url}`, (b) returns cached value if present, (c) otherwise calls `requests.get(url)`, stores result with `setex`, returns body.
3. Run: `python3 -c "from web import get_page; get_page('http://example.com'); get_page('http://example.com')"` and check in Redis CLI: `GET count:http://example.com` (2) and `GET cached:http://example.com` (HTML).

---

## Quick reference: run by project

```bash
# MySQL (from repo root, adjust user/db)
mysql -u root -p mydb < 0x00-MySQL_Advanced/2-fans.sql

# NoSQL — Mongo shell
mongosh < 0x01-NoSQL/0-list_databases

# NoSQL — Python (ensure MongoDB is running)
cd 0x01-NoSQL && python3 9-insert_school.py   # or via main

# Redis (ensure redis-server is running)
cd 0x02-redis_basic && python3 -c "from web import get_page; print(get_page('http://example.com')[:200])"
```

---

## Summary

- **0x00-MySQL_Advanced:** SQL for constraints, triggers, procedures; run with MySQL client and init scripts.
- **0x01-NoSQL:** MongoDB shell scripts + PyMongo scripts for CRUD and aggregation; run with `mongosh` or `python3`.
- **0x02-redis_basic:** Redis caching and counters in Python; run with Redis server and `python3` using `web.py` and optional exercise/main scripts.

Each subfolder may have its own short `README.md`; this file is the high-level map of **what each file is for** and **how to run and redo the exercises**.
