from flask import Flask, render_template, request
import requests
from decouple import config
from datetime import date
import pathlib

api_url = config("URL")
payload = {
    "room": config("ROOM_NUMBER"),
    "date": "2024-12-16"
}

base_dir = pathlib.Path('./sources') / config("DISPLAY")
file = "index.html"


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # Взять данные с бота
    payload["date"] = date.today().isoformat()
    response = requests.get(api_url, json=payload)

    # В зависимости от времени темный/светлый дизайн
    if date.today().hour < 12:
        mode = "light"
    else:
        mode = "dark"

    path = base_dir / mode

    # Если ошибка
    if response.status_code != 200:
        path = path
        return render_template("error.html", error=response.status_code)

    else:
        return "Error"