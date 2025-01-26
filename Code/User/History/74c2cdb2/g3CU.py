from flask import Flask, render_template, request
import requests
from decouple import config

api_url = config("URL")
payload = {
    "room": config("ROOM_NUMBER"),
    "date": "2024-12-16"
}

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    response = response.get(api_url, json=payload)

    if response.status_code == 200:
        pass

    else:
        return "Error"