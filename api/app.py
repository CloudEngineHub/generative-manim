"""
GM (Generative Manim) API is licensed under the Apache License, Version 2.0
"""

import os
import time
import re
from subprocess import run, PIPE, Popen, CalledProcessError
import subprocess
from flask import Flask, jsonify, request, Response, url_for
from dotenv import load_dotenv
from flask_cors import CORS
import sys
import traceback
import json
from routes.code_generation import generate_code as generate_code_route
from routes.video_rendering import code_to_video as render_code_to_video

load_dotenv()
app = Flask(__name__, static_folder="public", static_url_path="/public")
CORS(app)

USE_LOCAL_STORAGE = os.getenv("USE_LOCAL_STORAGE", "true") == "true"
BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8080")


@app.route("/")
def hello_world():
    return "Generative Manim Processor"


@app.route("/generate-code", methods=["POST"])
def generate_code():
    return generate_code_route()


@app.route("/code-to-video", methods=["POST"])
def code_to_video():
    return render_code_to_video()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host="0.0.0.0", port=port)
