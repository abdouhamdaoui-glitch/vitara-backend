from flask import Flask, jsonify, request
from flask_cors import CORS
from pytrends.request import TrendReq
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Use a global variable for pytrends client
pytrends = TrendReq(hl='en-US', tz=360)

# Pre-defined list of common trending topics for fallback
TRENDING_TOPICS = [
    "Tesla", "YouTube", "Olympics", "Entertainment news", "Weather",
    "Netflix", "Black Friday", "Holiday travel", "iPhone news",
    "Education resources", "New movies", "Super Bowl", "Health tips",
    "Prime Video", "NFL", "NBA", "Business news", "Technology trends"
]

@app.route("/trends", methods=["GET"])
def get_trending_now():
    try:
        trending_searches_df = pytrends.trending_searches(pn='united_states')
        
        if not trending_searches_df.empty:
            trends_list = [{"query": row["title"], "traffic": row.get("traffic", "N/A")} for _, row in trending_searches_df.iterrows()]
            return jsonify({
                "trends": trends_list,
                "count": len(trends_list),
                "timestamp": datetime.now().isoformat(),
                "source": "pytrends_api",
                "message": "Successfully fetched live data."
            })
        else:
            raise ValueError("PyTrends returned no trending data.")
    
    except Exception as e:
        print(f"PyTrends call failed, using fallback data. Error: {e}")
        return jsonify({
            "trends": [{"query": t, "traffic": "N/A"} for t in TRENDING_TOPICS],
            "count": len(TRENDING_TOPICS),
            "timestamp": datetime.now().isoformat(),
            "source": "reliable_fallback",
            "message": f"Using reliable fallback data due to a live API error: {str(e)}"
        })

@app.route("/trends/keyword", methods=["GET"])
def get_keyword_trends():
    keyword = request.args.get('query')
    if not keyword:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    try:
        pytrends.build_payload(kw_list=[keyword], timeframe='today 5-y')
        interest_over_time_df = pytrends.interest_over_time()
        
        if not interest_over_time_df.empty:
            keyword_data = interest_over_time_df.reset_index().to_dict('records')
            return jsonify({
                "keyword": keyword,
                "data": [{"date": item.get('date').isoformat(), "value": item.get(keyword)} for item in keyword_data],
                "source": "pytrends_api",
                "message": "Successfully fetched live data."
            })
        else:
            return jsonify({
                "error": "No data found for this keyword.",
                "message": "PyTrends returned no data for the requested keyword."
            }), 404

    except Exception as e:
        print(f"Keyword API call failed. Error: {e}")
        return jsonify({
            "error": "Failed to fetch data for the keyword. Please try again later.",
            "message": str(e)
        }), 500

@app.route("/health", methods=["GET"])
def health_check():
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
