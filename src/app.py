from flask import Flask, render_template, request

import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Ola mundo"

if __name__ == "__main__":
    app.run(debug=False)
