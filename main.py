import socketio
import uvicorn

sio = socketio.AsyncServer(async_mode='asgi')

app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
	print(f"Client {sid} connect")


@sio.event
async def disconnect(sid):
	print(f"Client {sid} disconnect")


if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=80)
