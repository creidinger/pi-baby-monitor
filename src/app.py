from flask import Flask, render_template
from camera import Camera

app = Flask(__name__)


@app.route("/")
def monitor():
    """Video streaming home page"""
    return render_template("index.html")
