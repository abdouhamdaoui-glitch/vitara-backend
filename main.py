import requests
import json

RAPIDAPI_KEY = "24b5aa43d1msh6602bfbd74dcefep190f3cjsn19fa0c61e536"
HEADERS = {
    "Content-Type": "application/json",
    "x-rapidapi-host": "",
    "x-rapidapi-key": RAPIDAPI_KEY
}

# ------------------- Trendly (Google Trends) -------------------
trendly_endpoints = {
    "topics": ("trendly.p.rapidapi.com", "https://trendly.p.rapidapi.com/topics", {"keywords":["France"],"start":"2020-05-01T00:43:37+0100","country":"","region":"","category":"","gprop":""}, "POST"),
    "categories": ("trendly.p.rapidapi.com", "https://trendly.p.rapidapi.com/cat", {}, "GET"),
    "geo": ("trendly.p.rapidapi.com", "https://trendly.p.rapidapi.com/geo", {}, "GET"),
    "realtime": ("trendly.p.rapidapi.com", "https://trendly.p.rapidapi.com/realtime", {"country":"United States","category":"All categories"}, "POST"),
    "suggest": ("trendly.p.rapidapi.com", "https://trendly.p.rapidapi.com/suggest", {"keyword":"amazon"}, "POST"),
    "queries": ("trendly.p.rapidapi.com", "https://trendly.p.rapidapi.com/queries", {"keywords":["France","Italy","Germany"],"start":"2020-05-01T00:43:37+0100","country":"France","region":"","category":"","gprop":""}, "POST"),
    "region": ("trendly.p.rapidapi.com", "https://trendly.p.rapidapi.com/region", {"keywords":["France","Italy","Germany"],"start":"2020-05-01T00:43:37+0100","country":"","region":"","category":"","gprop":"","resolution":"COUNTRY","include_low_volume":False}, "POST"),
    "historical": ("trendly.p.rapidapi.com", "https://trendly.p.rapidapi.com/historical", {"keywords":["France","Italy","Germany"],"start":"2020-05-01T00:43:37+0100","country":"France","region":"Alsace","category":"","gprop":""}, "POST"),
    "hot": ("trendly.p.rapidapi.com", "https://trendly.p.rapidapi.com/hot", {"country":"united_states"}, "POST"),
    "today": ("trendly.p.rapidapi.com", "https://trendly.p.rapidapi.com/today", {"country":"United States"}, "POST"),
}

trendly_results = {}
for key, (host, url, data, method) in trendly_endpoints.items():
    HEADERS["x-rapidapi-host"] = host
    if method == "POST":
        resp = requests.post(url, headers=HEADERS, json=data)
    else:
        resp = requests.get(url, headers=HEADERS)
    trendly_results[key] = resp.json()

with open("trendly_data.json", "w") as f:
    json.dump(trendly_results, f, indent=2)

print("✅ Trendly data saved in trendly_data.json")

# ------------------- Meta / Facebook Ads -------------------
meta_endpoints = {
    "search": ("meta-library.p.rapidapi.com", "https://meta-library.p.rapidapi.com/search", {"term":"sales"}, "POST"),
}

meta_results = {}
for key, (host, url, data, method) in meta_endpoints.items():
    HEADERS["x-rapidapi-host"] = host
    resp = requests.post(url, headers=HEADERS, json=data)
    meta_results[key] = resp.json()

with open("meta_data.json", "w") as f:
    json.dump(meta_results, f, indent=2)

print("✅ Meta (Facebook) data saved in meta_data.json")

# ------------------- Shopify Stores Info -------------------
shopify_endpoints = {
    "store_info": "https://shopify-stores-info.p.rapidapi.com/store/info?url=https%3A%2F%2Fshop.bodybuilding.com%2F",
    "collections": "https://shopify-stores-info.p.rapidapi.com/product/collections?url=https%3A%2F%2Fgear.aarmy.com%2F",
    "all_products": "https://shopify-stores-info.p.rapidapi.com/product/all?url=https%3A%2F%2Fgear.aarmy.com",
    "avg_price": "https://shopify-stores-info.p.rapidapi.com/product/avg-price?url=https%3A%2F%2Ffunisboutique.com",
    "screenshot": "https://shopify-stores-info.p.rapidapi.com/store/screenshot?url=https%3A%2F%2Fhypereserve.com",
    "screenshotv2": "https://shopify-stores-info.p.rapidapi.com/store/screenshotv2?url=https%3A%2F%2Fbodybuilding.com",
    "contacts": "https://shopify-stores-info.p.rapidapi.com/store/contacts?url=https%3A%2F%2Fbodybuilding.com",
    "analyticsv2": "https://shopify-stores-info.p.rapidapi.com/store/analyticsv2?url=https%3A%2F%2Fgymshark.com",
    "analytics": "https://shopify-stores-info.p.rapidapi.com/store/analytics?url=https%3A%2F%2Fwww.underarmour.com",
    "competitorsv1": "https://shopify-stores-info.p.rapidapi.com/store/competitorsv1?url=gymshark.com&limit=10",
    "search_products": "https://shopify-stores-info.p.rapidapi.com/product/search?url=https%3A%2F%2Ffunisboutique.com&query=camiseta",
    "social_media": "https://shopify-stores-info.p.rapidapi.com/store/social-media?url=https%3A%2F%2Fgear.aarmy.com%2F",
    "store_all": "https://shopify-stores-info.p.rapidapi.com/store/all?perPage=4",
    "best_selling": "https://shopify-stores-info.p.rapidapi.com/product/best-selling?url=https%3A%2F%2Fa4c.com",
    "apps": "https://shopify-stores-info.p.rapidapi.com/store/apps?url=https%3A%2F%2Fwww.vqfit.com",
    "random_store": "https://shopify-stores-info.p.rapidapi.com/store/random?perPage=7",
    "search_store": "https://shopify-stores-info.p.rapidapi.com/store/search?query=fit&perPage=7",
    "competitors": "https://shopify-stores-info.p.rapidapi.com/store/competitors?url=https%3A%2F%2Fwww.underarmour.com",
    "revenue": "https://shopify-stores-info.p.rapidapi.com/store/revenue?url=https%3A%2F%2Fhelmboots.com%2F"
}

shopify_results = {}
HEADERS["x-rapidapi-host"] = "shopify-stores-info.p.rapidapi.com"
for key, url in shopify_endpoints.items():
    resp = requests.get(url, headers=HEADERS)
    shopify_results[key] = resp.json()

with open("shopify_data.json", "w") as f:
    json.dump(shopify_results, f, indent=2)

print("✅ Shopify data saved in shopify_data.json")
