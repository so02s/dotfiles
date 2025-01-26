import os
import time
import subprocess
from datetime import date

from jinja2 import Template
# from flask import render_template
from pathlib import Path

# Генерирование веб страничек

async def change_image(occupied: dict, schedule, path: Path):
    mode = "light"
    occup = "occupied" if occupied else "free"
    dist_path = path / mode / occup / "index.html"
    tmp = Template(open(dist_path).read())
    tmp.render(slots=schedule)

    with open(dist_path / "index.html", "w") as f:
        f.write(html)

    html_bytes = page.encode("utf-8")
    html_b64 = base64.b64encode(html_bytes).decode("utf-8")

    webbrowser.register('vivaldi', None, webbrowser.BackgroundBrowser('/usr/bin/vivaldi'))
    webbrowser.get('vivaldi').open_new_tab("data:text/html;base64," + html_b64)

    # return tmp.render(slots=schedule)

async def static_image(path: Path):
    mode = "light"
    # ТУТ ОШИБКА, HOUR НЕТ
    # mode = "light" if date.today().hour < 12 else "dark"
    tmp = Template(open(path / mode / "error" / "index.html").read())
    tmp.render()
    # return tmp.render()


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