import socketio
import uvicorn
from fastapi import FastAPI


app = FastAPI()

sio = socketio.AsyncServer(async_mode='asgi')

socker_app = socketio.ASGIApp(sio, app)

storage = {"user_counter": 0}


@sio.event
async def connect(sid, environ):
    storage["user_counter"] += 1
    print(f"User {sid} connect")


@app.get("/")
async def get_index():
    return f"user_counter = {storage['user_counter']}"


uvicorn.run(socker_app, host='0.0.0.0', port=80)
