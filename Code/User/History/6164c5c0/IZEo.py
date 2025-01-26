import os
import time
import subprocess
from datetime import date

from jinja2 import Template
# from flask import render_template
from pathlib import Path

# Генерирование веб страничек

async def change_image(occupied: dict, schedule, path: Path) -> str:
    mode = "light" if date.today().hour < 12 else "dark"
    occup = "occupied" if occupied else "free"

    tmp = Template(open(path / mode / occup / "index.html").read())

    return tmp.render(
        # path / mode / "occupied" / "index.html",
        slots=schedule
    )

async def static_image(path: Path) -> str:
    mode = "light"
    # mode = "light" if date.today().hour < 12 else "dark"
    tmp = Template()
    # return render_template(path / mode / "error" / "index.html")
    return tmp.render()


# Работа с дисплеем

os.environ['DISPLAY'] = ':0'

def turn_off_screen():
    os.system("xset dpms force off")

def turn_on_screen():
    os.system("xset dpms force on")


def set_brightness(brightness):
    try:
        subprocess.run(['xrandr', '--output', 'HDMI-1', '--brightness', str(brightness)], check=True)
    except subprocess.CalledProcessError as e:
        pass

def turn_on_hdmi(duration=1, steps = 50):
    for i in range(steps + 1):
        brightness = 1 - (i / steps)
        set_brightness(brightness)
        time.sleep(duration / steps)

def turn_off_hdmi(duration=5, steps = 100):
    for i in range(steps + 1):
        brightness = i / steps
        set_brightness(brightness)
        time.sleep(duration / steps)