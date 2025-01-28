import json
import os

DATA_FILE = "data/users.json"

def load_user_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,'r') as file:
            return json.load(file)
    return {}

def save_user_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data,file, indent=4)

def get_or_create_user(user_id, username):
    data = load_user_data()
    if str(user_id) not in data:
        data[str(user_id)] = {
            'username': username,
            "weight": None,
            "height": None,
            "age": None,
            "activity_minutes": None,
            "city": None,
            "water_consumed": 0,
            "calories_consumed": 0,
            "calories_burned": 0,
        }
        save_user_data(data)
    return data[str(user_id)]

def update_user_profile(user_id, field, value):
    data = load_user_data()
    if str(user_id) in data:
        data[str(user_id)][field] = value
        save_user_data(data)
