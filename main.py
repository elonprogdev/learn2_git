from flask import Flask, render_template, request, url_for, redirect
from flask_socketio import SocketIO
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"
socket_app = SocketIO(app, async_mode="eventlet")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")




@app.route("/about")
def about():
    return render_template("about.html")

@socket_app.on("guess")
def handle_guess(name):
  
    user = name
    print('gurs notify')
    
    try:
        socket_app.emit("response",  f"Привет {user}!", to=request.sid)
        
    except ValueError:
        socket_app.emit("response", "Invalid input. Enter a number.", to=request.sid)

if __name__ == "__main__":
    app.run(debug=True)

