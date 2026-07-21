import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    greeting = os.environ.get("GREETING", "Hello from my first Docker container!")
    return greeting

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
