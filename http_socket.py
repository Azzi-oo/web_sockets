import eventlet
import socketio

static_files = { '/': 'static/index.html' }

sio = socketio.Server(cors_allowed_origins='*', async_mode='eventlet')

app = socketio.WSGIApp(sio, static_files=static_files)


@sio.event
def connect(sid, environ):
    print(f"User {sid} connect")


@sio.event
def disconnect(sid):
    print(f"User {sid} disconnect")


eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 80)), app)
