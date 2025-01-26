import time
import threading
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

data_cache = {}
cache_lock = threading.Lock()  

def fetch_leaderboard_for_contest(contest_id):
    """Fetch leaderboard data for a specific contest."""
    unix_timestamp = int(time.time() * 1000)
    url = f"https://www.hackerrank.com/rest/contests/{contest_id}/leaderboard?offset=0&limit=10000&_={unix_timestamp}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        leaderboard = response.json()

        with cache_lock:
            data_cache[contest_id] = leaderboard
        
        return leaderboard
    except requests.exceptions.RequestException as e:
        print(f"Error fetching leaderboard for {contest_id}: {e}")
        return None

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Retrieve leaderboard data for a specific contest ID."""
    contest_id = request.args.get('contest_id')
    
    if not contest_id:
        return jsonify({"error": "Contest ID is required."}), 400

    with cache_lock:  
        if contest_id in data_cache and data_cache[contest_id]:
            return jsonify(data_cache[contest_id])
    
    leaderboard = fetch_leaderboard_for_contest(contest_id)
    if leaderboard:
        return jsonify(leaderboard)
    else:
        return jsonify({"error": f"Failed to fetch data for contest ID {contest_id}. Please try again later."}), 503
