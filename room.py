import eventlet.wsgi
import socketio
import eventlet
import socketio.server


sio = socketio.Server()
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print('User connected: ', sid)


@sio.on("join")
def join(sid, data):
    room = data['room']
    sio.enter_room(sid, room)
    print(f'User {sid} has joined the room {room}')


@sio.event("message")
def message(sid, data):
    text = data['text']
    room = data['room']
    sio.emit('message', {'text': text}, room=room)
    print(f'Message from {sid} in room {room}: {text}')


eventlet.wsgi.server(eventlet.listen(('', 80)), app)
