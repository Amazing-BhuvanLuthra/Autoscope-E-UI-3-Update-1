from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shutdown")
def shutdown():
    # Add a confirmation step or password protection for security (optional)
    subprocess.run(["sudo", "shutdown", "-h", "now"])  # Execute shutdown command
    # return "Raspberry Pi is shutting down..."

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # Allow access from other devices
