from sqlite3 import Timestamp
from datetime import datetime
from flask import Flask, request
from weatherController import get_air_temp


app = Flask(__name__)

@app.route("/")
def index():
    return {
        "author": "Joshua Sharkey",
        "name": "Climate Monitor App",
        "status": "OK" 
    }

@app.route("/warp/temp")
def get_temp():
    temp = get_air_temp(request.remote_addr)
    status =  "Too Hot" if temp > 50 else "Too Cold"
    timestamp = datetime.now().timestamp()
    return {
        "temp": temp,
        "status": status,
        "timestamp": timestamp
    }