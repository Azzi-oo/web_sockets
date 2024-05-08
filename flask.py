import eventlet
import socketio.server
from flask import Flask
import socketio

sio = socketio.server()

flask_app = Flask(__name__)

app = socketio.WSGIApp(sio, flask_app)


@sio.event
def connect(sid, environ):
    print(f"User {sid} connect")


@sio.event
def disconnect(sid):
    print(f"User {sid} disconnect")


@flask_app.route("/")
def page_index():
    return "It works"


eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 80)), app)
