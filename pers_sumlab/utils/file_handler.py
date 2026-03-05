import json
import os

DATA_FILE = "data/data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": [], "projects": []}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {"users": [], "projects": []}

def save_data(data):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)