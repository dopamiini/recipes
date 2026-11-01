from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Placeholder for a food recipe app for the course TiKaWe."