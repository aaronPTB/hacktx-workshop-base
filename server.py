from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "hello!"

@app.route("/view")
def view():
    pass

@app.route("/api/submit")
def submit():
    pass

if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
