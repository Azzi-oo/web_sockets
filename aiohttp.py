import socketio
from aiohttp import web

sio = socketio.AsyncServer(async_mode='aiohttp')

app = web.Application()
sio.attach(app)


@sio.event
async def connect(sid, environ):
    print(f"Client {sid} connect")


@sio.event
def disconnect(sid):
    print(f"Client {sid} not connect")


if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=80)
