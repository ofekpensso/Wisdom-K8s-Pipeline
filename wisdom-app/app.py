from flask import Flask
import random
import socket

app = Flask(__name__)

wisdoms = [
    "DevOps is a journey, not a destination.",
    "Automate everything!",
    "It works on my machine... and now on Docker too.",
    "Kubernetes: Greek for 'Helmsman'.",
    "Keep calm and git push."
]

@app.route('/')
def get_wisdom():
    host_name = socket.gethostname()
    return f"<div style='background-color: lightgreen; padding: 20px;'><h1>🚀 ofek DevOps Master V2!</h1><h2>Wisdom from pod: {host_name}</h2><p>{random.choice(wisdoms)}</p></div>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
