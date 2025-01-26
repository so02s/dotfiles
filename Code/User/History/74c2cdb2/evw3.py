from flask import Flask, render_template, request
import requests
from decouple import config

api_url = config("URL")
payload = {
    "room": "1",
    "date": "2024-12-16"
}

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    response = response.get(api_url)

