from flask import Flask
import redis 
import os

app = Flask(__name__)

# Connect to Redis (use environment variables for Redis connection)
redis_host = os.getenv('REDIS_HOST', 'localhost')  # This will be set to Redis service in Docker Compose
redis_port = os.getenv('REDIS_PORT', 6379)
r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def welcome():
    return "Welcome to the Flask + Redis app!"

@app.route('/count')
def count():
    count = r.incr('visits')  # Increment 'visits' key in Redis
    return f"Visit count: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
