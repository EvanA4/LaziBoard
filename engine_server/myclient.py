#!/usr/bin/env python

import asyncio
from websockets.client import connect

async def hello():
    async with connect("ws://localhost:8765") as websocket:

        tosend = input("What would you like to send? ")
        while tosend != "quit":
            await websocket.send(tosend)
            message = await websocket.recv()
            print(f"Received: {message}")
            
            tosend = input("What would you like to send? ")

asyncio.run(hello())