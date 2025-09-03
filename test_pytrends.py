from pytrends.request import TrendReq
import pandas as pd

def test_pytrends():
    print("Testing PyTrends connection...")
    
    try:
        # Initialize
        pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25))
        print("✓ PyTrends initialized successfully")
        
        # Test trending searches
        print("Fetching trending searches...")
        trending_df = pytrends.trending_searches(pn='united_states')
        
        print(f"DataFrame shape: {trending_df.shape}")
        print(f"DataFrame columns: {trending_df.columns.tolist()}")
        print(f"First few rows:\n{trending_df.head()}")
        
        # Convert to list
        trends_list = trending_df[0].tolist()
        print(f"\nTrends list ({len(trends_list)} items):")
        for i, trend in enumerate(trends_list[:10], 1):
            print(f"{i}. {trend}")
            
    except Exception as e:
        print(f"✗ Error: {e}")
        print(f"Error type: {type(e).__name__}")

if __name__ == "__main__":
    test_pytrends()