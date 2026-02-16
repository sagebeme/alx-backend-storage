0x02. Redis basic
=================

This project uses **Redis** from Python to **cache HTTP responses** and **count how many times each URL was requested**, so repeated requests for the same URL don’t hit the web server every time.

Tasks
-----

### 1. What does `web.py` do?

It implements a **caching layer** around fetching a web page: (1) **`get_page(url)`** — fetches the URL with `requests.get` and returns the response text; (2) a **decorator** (e.g. `wrap_requests`) that (a) **increments** a Redis key `count:{url}` every time the URL is requested, (b) **returns the cached HTML** from Redis key `cached:{url}` if it exists, (c) otherwise calls the real `get_page`, **stores the result** in Redis with a TTL (e.g. 10 seconds) using `setex`, and returns it. So the first request hits the web; later requests within the TTL come from Redis. Run: Start Redis (`redis-server`), then e.g. `python3 -c "from web import get_page; print(get_page('http://example.com')[:200])"`. Call again to see cache and count in action.

**Repo:**

-   GitHub repository: `alx-backend-storage`
-   Directory: `0x02-redis_basic`
-   File: `web.py`

### 2. What does `exercise.py` do?

It contains **Redis exercises** (get, set, incr, etc.) so you can practice basic Redis operations from Python (e.g. connect, set a key, get it, increment a counter). Run: `python3 exercise.py` if it has a `if __name__ == "__main__"` block, or run snippets in the REPL.

**Repo:**

-   GitHub repository: `alx-backend-storage`
-   Directory: `0x02-redis_basic`
-   File: `exercise.py`

### 3. What does `0-main.py` do?

It is a **demo or test script** that uses the Redis client or the caching logic (e.g. calls `get_page` or exercises Redis) so you can verify everything works. Run: `python3 0-main.py` (with Redis server running).

**Repo:**

-   GitHub repository: `alx-backend-storage`
-   Directory: `0x02-redis_basic`
-   File: `0-main.py`

---

**How to do the exercises yourself**

1. Install Redis and start it: `redis-server`. Install Python deps: `pip install redis requests`.
2. Implement a decorator that: (a) increments `count:{url}`, (b) returns cached value if present, (c) otherwise fetches the URL, stores with `redis.setex("cached:{url}", 10, result)`, and returns the result.
3. Decorate `get_page` with that decorator.
4. Run multiple requests to the same URL and check in Redis CLI: `GET count:http://example.com` and `GET cached:http://example.com`.
