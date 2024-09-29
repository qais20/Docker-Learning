from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis (use environment variables for Redis connection)
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = os.getenv('REDIS_PORT', 6379)
r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def welcome():
    return '''
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-image: url('https://coolbackgrounds.io/images/unsplash/samuel-zeller-medium-b832fe04.jpg');
                background-size: cover;
                color: black;
            }
            .container {
                background-color: rgba(255, 255, 255, 0.8);
                padding: 50px;
                margin-top: 100px;
                border-radius: 15px;
                display: inline-block;
            }
            .btn {
                padding: 10px 20px;
                margin: 10px;
                font-size: 18px;
                color: white;
                background-color: #000000;
                text-decoration: none;
                border-radius: 5px;
                border: none;
                cursor: pointer;
            }
            .btn:hover {
                background-color: #000000;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to VisitCounterX by Qais!</h1>
            <p>Track your visits by clicking the button down below👇</p>
            <a href="/about" class="btn">Go to About Page</a>
            <a href="/count" class="btn">Check Visit Counter</a>
        </div>
    </body>
    </html>
    '''

@app.route('/count')
def count():
    count = r.incr('visits')  # Increment 'visits' key in Redis
    return f'''
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-image: url('https://coolbackgrounds.io/images/unsplash/samuel-zeller-medium-b832fe04.jpg');
                background-size: cover;
                color: black;
            }}
            .container {{
                background-color: rgba(255, 255, 255, 0.8);
                padding: 50px;
                margin-top: 100px;
                border-radius: 15px;
                display: inline-block;
                text-align: center;
            }}
            .counter {{
                font-size: 50px;
                color: #000000;
                margin: 20px;
                font-weight: bold;
            }}
            .quote {{
                font-size: 20px;
                font-style: italic;
                margin-top: 20px;
            }}
            .progress-bar {{
                width: 100%;
                background-color: #f3f3f3;
                border-radius: 25px;
                margin: 20px 0;
            }}
            .progress-bar-fill {{
                height: 30px;
                width: {count}% ;
                background-color: black;  /* Black progress bar */
                border-radius: 25px;
                transition: width 1s ease-in-out;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Visit Counter</h1>
            <div class="counter" id="visitCount">Visit Count: {count}</div>
            
            <!-- Progress Bar -->
            <div class="progress-bar">
                <div class="progress-bar-fill" style="width: {min(count, 100)}%;"></div>
            </div>

            <!-- Random Quote -->
            <div class="quote">{get_random_quote()}</div>
        </div>

        <script>
            // Animate visit counter (simple animation)
            const visitCountEl = document.getElementById('visitCount');
            let start = 0;
            const end = {count};
            const duration = 2000; // 2 seconds
            const stepTime = Math.abs(Math.floor(duration / end));
            const timer = setInterval(function() {{
                start += 1;
                visitCountEl.textContent = "Visit Count: " + start;
                if (start >= end) {{
                    clearInterval(timer);
                }}
            }}, stepTime);
        </script>
    </body>
    </html>
    '''

# Random quote generator with Prophet Muhammad (PBUH) quotes
import random

def get_random_quote():
    quotes = [
        "The best of people are those that bring most benefit to the rest of mankind.",
        "Kindness is a mark of faith, and whoever is not kind has no faith.",
        "The strongest among you is the one who controls his anger.",
        "Make things easy for people and do not make them difficult."
    ]
    return random.choice(quotes)



@app.route('/about')
def about():
    return '''
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-image: url('https://coolbackgrounds.io/images/unsplash/samuel-zeller-medium-b832fe04.jpg');
                background-size: cover;
                color: black;
            }
            .container {
                background-color: rgba(255, 255, 255, 0.8);
                padding: 50px;
                margin-top: 100px;
                border-radius: 15px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>About This Application</h1>

            <p>Welcome to my first official project! My name is <strong>Qais</strong>, and I'm excited to showcase this Flask web app built with the power of Docker, Redis, and Nginx.</p>

            <p>This project is more than just a simple web app—it's a hands-on journey into the world of DevOps and containerization. By leveraging <em>Docker</em> and <em>Docker Compose</em>, I've created a multi-container environment that connects the front-end (Flask) with a Redis database, all managed seamlessly with Nginx for load balancing.</p>

            <h2>What's Inside?</h2>
            <ul>
              <li>🛠 <strong>Flask</strong> – A lightweight Python web framework powering the app.</li>
              <li>💾 <strong>Redis</strong> – A fast, in-memory key-value store, managing the visit counts and more.</li>
              <li>🚀 <strong>Docker</strong> – Containerizing the entire environment for consistent development and deployment.</li>
              <li>⚙️ <strong>Nginx</strong> – Handling load balancing and ensuring smooth, scalable performance.</li>
            </ul>

            <h2>What’s Next?</h2>
            <p>This is just the beginning! I'm planning to add more cool features like user tracking, interactive maps, and advanced scaling techniques. Stay tuned, as I'll continue to improve this project.</p>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777)
