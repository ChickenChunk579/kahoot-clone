from flask import Flask, send_from_directory, render_template, url_for, redirect
import os

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)