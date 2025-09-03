from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
RAPIDAPI_HOST = "google-trends-api5.p.rapidapi.com"

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
