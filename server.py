import argparse
import os
import time
from typing import List

import undetected_geckodriver as uc
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait

# webdriver

parser = argparse.ArgumentParser()
parser.add_argument(
    "--dev", action="store_true", help="Run in development mode (no kiosk)"
)
args = parser.parse_args()

profile_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "firefox_profile")
)

# Create profile directory if it doesn't exist
if not os.path.exists(profile_path):
    os.makedirs(profile_path)

options = Options()
if not args.dev:
    options.add_argument("--kiosk")

options.add_argument("-profile")
options.add_argument(profile_path)

service = Service(executable_path="/usr/local/bin/geckodriver")
driver = uc.Firefox(options=options, service=service)

driver.get("https://youtube.com")


def openVideo(url: str):
    print("Opening video...")
    driver.get(url)
    print("Waiting for client javascript...")

    # wait for client JS to render
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    time.sleep(2)

    print("JS loaded, sending fullscreen input...")

    body = driver.find_element("tag name", "body")  # find <body>

    body.send_keys("f")


# webserver


class CommandRequest(BaseModel):
    commands: List[str]


class PlayVideoRequest(BaseModel):
    url: str


app = FastAPI()

KEY_MAP = {
    "space": Keys.SPACE,
    "arrowleft": Keys.ARROW_LEFT,
    "arrowright": Keys.ARROW_RIGHT,
    "f": "f",
}


@app.post("/playvideo")
def playvideo(req: PlayVideoRequest):
    print("/playvideo endpoint hit")
    print("URL: ", req.url)
    openVideo(req.url)


@app.post("/update")
def update(req: CommandRequest):
    print("/update endpoint hit")
    print("commands:", req.commands)
    body = driver.find_element("tag name", "body")  # find <body>

    for command in req.commands:
        key = KEY_MAP.get(command.lower())
        if key:  # ignore unknown commands
            body.send_keys(key)

    return {"status": "ok", "executed": req.commands}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
