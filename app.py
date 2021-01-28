from flask import Flask 

app = Flask(__name__)

@app.route("/ping", methods=['get'])
def ping():
    return "pong"