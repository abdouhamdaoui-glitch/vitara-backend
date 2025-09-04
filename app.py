from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import random
from datetime import datetime
import os

app = Flask(__name__)
CORS(app) # Allow all origins for now

# API Configuration
API_HOST = 'google-trends21.p.rapidapi.com'
API_KEY = os.environ.get('RAPIDAPI_KEY', '24b5aa43d1msh6602bfbd74dcefep190f3cjsn19fa0c61e536')
HEADERS = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY,
}

# Pre-defined list of common trending topics for fallback
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
def get_trending_now():
    """Get trending topics from Google Trends API or fallback data."""
    api_url = f"https://{API_HOST}/getTrendingNow?country=US&time=4&hl=en-US&tz=300"
    
    try:
        response = requests.get(api_url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # The new API structure is a bit different, we need to extract the data
        trending_data = []
        for item in data.get('results', []):
            for trend_topic in item.get('trendingTopics', []):
                trending_data.append({
                    "query": trend_topic.get('query'),
                    "traffic": trend_topic.get('traffic', 'N/A')
                })

        if trending_data:
            return jsonify({
                "trends": trending_data,
                "count": len(trending_data),
                "timestamp": datetime.now().isoformat(),
                "source": "google_trends_api",
                "message": "Successfully fetched live data."
            })
        else:
            raise ValueError("API returned no trending data.")
            
    except Exception as e:
        print(f"API call failed, using fallback data. Error: {e}")
        shuffled_topics = TRENDING_TOPICS.copy()
        random.shuffle(shuffled_topics)
        num_topics = random.randint(15, 25)
        current_trends = [{"query": t, "traffic": "N/A"} for t in shuffled_topics[:num_topics]]
        
        return jsonify({
            "trends": current_trends,
            "count": len(current_trends),
            "timestamp": datetime.now().isoformat(),
            "source": "reliable_fallback",
            "message": f"Using reliable fallback data. Error: {str(e)}"
        })

@app.route("/trends/keyword", methods=["GET"])
def get_keyword_trends():
    """Get trends for a specific keyword from the Google Trends API."""
    keyword = request.args.get('query')
    if not keyword:
        return jsonify({"error": "Missing 'query' parameter"}), 400
    
    api_url = f"https://{API_HOST}/getExploreSearchTerm?keyword={keyword}&country=US&time=now%207-d&category=0&hl=en-US&tz=300"
    
    try:
        response = requests.get(api_url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # This API returns a list of dictionaries with search interest data
        return jsonify({
            "keyword": keyword,
            "data": data.get('default', {}).get('timelineData', []),
            "source": "google_trends_api"
        })
        
    except Exception as e:
        print(f"Keyword API call failed. Error: {e}")
        return jsonify({
            "error": "Failed to fetch data for the keyword. Please try again later.",
            "message": str(e)
        }), 500

@app.route("/health", methods=["GET"])
def health_check():
    """Simple health check endpoint."""
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
            "trending_now": "/trends",
            "keyword_trends": "/trends/keyword?query=example",
            "health": "/health"
        },
        "status": "online"
    })

if __name__ == "__main__":
    app.run(debug=True)
