#from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
#import psycopg2
from fastapi import FastAPI, Request, Depends, Response
import select
from datetime import datetime
#from app.config import config

app = FastAPI()

#connection = psycopg2.connect(dbname=config.PG_DB, user=config.PG_USERNAME, host=config.PG_SERVER, port=5432, password=config.PG_PWD)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Accept the connection from a client.
    await websocket.accept()
    while True:
        message = input("Enter a message to send: ")
        await websocket.send(message)
        print(f"Sent message: {message}")
        res=await websocket.recv()
        print(res)
    
