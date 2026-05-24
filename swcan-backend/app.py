from flask import Flask, jsonify
import requests

app = Flask(__name__)

# TEMP: mock database (we will replace with real scraping later)
swimmers = [
    {
        "id": "SWC-2011-001",
        "name": "Arthur Pigeon",
        "club": "RL Swim Club",
        "year": 2011,
        "meets": [
            {
                "name": "Regional Champs",
                "date": "2025-03-12",
                "events": [
                    {"event": "100 Free", "time": "56.21", "rank": 3}
                ]
            }
        ]
    }
]

@app.route("/api/swimmers")
def get_swimmers():
    return jsonify(swimmers)

@app.route("/api/swimmer/<swimmer_id>")
def get_swimmer(swimmer_id):
    for s in swimmers:
        if s["id"] == swimmer_id:
            return jsonify(s)
    return jsonify({"error": "not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
