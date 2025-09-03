from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

# 1️⃣ Create the Flask app
app = Flask(__name__)

# 2️⃣ Enable CORS for all routes (or restrict origins for production)
CORS(app, resources={r"/*": {"origins": "*"}})


# 3️⃣ Your RapidAPI credentials
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
RAPIDAPI_HOST = "google-trends-api5.p.rapidapi.com"

# 4️⃣ Routes
@app.route("/trends", methods=["GET"])
def get_trends():
    url = f"https://{RAPIDAPI_HOST}/api/v1/trends"
    payload = {
        "geo": request.args.get("geo", "GB"),
        "hours": request.args.get("hours", "48"),
        "sort": request.args.get("sort", "title")
    }
    headers = {
        "content-type": "application/json",
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return {"message": "Vitara backend is running 🚀"}

# 5️⃣ Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
