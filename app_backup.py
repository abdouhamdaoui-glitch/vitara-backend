from flask import Flask, jsonify
import json

app = Flask(__name__)

# Route for Trendly
@app.route("/api/trendly")
def get_trendly():
    with open("trendly_data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

# Route for Meta
@app.route("/api/meta")
def get_meta():
    with open("meta_data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

# Route for Shopify
@app.route("/api/shopify")
def get_shopify():
    with open("shopify_data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
