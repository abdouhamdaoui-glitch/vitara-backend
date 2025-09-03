from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow all origins for now

# Pre-defined list of common trending topics
TRENDING_TOPICS = [
    "Taylor Swift", "NBA", "NFL", "Weather", "Stock Market",
    "COVID updates", "Elections", "New movies", "Sports news", 
    "Technology trends", "Travel destinations", "Food recipes",
    "Music releases", "Gaming news", "Education resources",
    "Space news", "Climate change", "Health tips", "Business news",
    "Entertainment news", "Super Bowl", "Olympics", "Holiday travel",
    "Black Friday", "Cyber Monday", "Amazon deals", "iPhone news",
    "Android updates", "Tesla", "Elon Musk", "Facebook", "Instagram",
    "TikTok trends", "YouTube", "Netflix", "Disney+", "Prime Video"
]

@app.route("/trends", methods=["GET"])
def get_trends():
    """Get trending topics - always works with fallback data"""
    try:
        # Shuffle the topics to make it look fresh
        shuffled_topics = TRENDING_TOPICS.copy()
        random.shuffle(shuffled_topics)
        
        # Take a random number between 15-25 topics
        num_topics = random.randint(15, 25)
        current_trends = shuffled_topics[:num_topics]
        
        return jsonify({
            "trends": current_trends,
            "count": len(current_trends),
            "timestamp": datetime.now().isoformat(),
            "source": "reliable_fallback",
            "message": "Using reliable fallback data"
        })
        
    except Exception as e:
        # Ultimate fallback if even this fails
        return jsonify({
            "trends": ["Technology", "Sports", "Entertainment", "News", "Weather"],
            "count": 5,
            "timestamp": datetime.now().isoformat(),
            "source": "emergency_fallback",
            "error": str(e)
        })

@app.route("/health", methods=["GET"])
def health_check():
    """Simple health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "vitara-trends-backend",
        "timestamp": datetime.now().isoformat()
    })

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Vitara backend is running 🚀",
        "endpoints": {
            "trends": "/trends",
            "health": "/health"
        },
        "status": "active"
    })

if __name__ == "__main__":
    print("Starting reliable backend server...")
    app.run(host="0.0.0.0", port=5000, debug=True)