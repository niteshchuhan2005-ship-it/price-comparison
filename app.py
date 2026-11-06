from flask import Flask, send_file, request, jsonify
import requests

app = Flask(__name__)

API_KEY = os.environ.get("SERPAPI_KEY", "")

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/search')
def search():
    q = request.args.get('q', 'phone')
    url = "https://serpapi.com/search.json"
    params = {"engine": "google_shopping", "q": q, "gl": "in", "hl": "en", "api_key": API_KEY}
    try:
        r = requests.get(url, params=params, timeout=15)
        data = r.json()
        return jsonify(data.get("shopping_results", [])[:5])
    except Exception as e:
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True, port=5000)