from engine import Engine
import asyncio
from websockets.server import serve
import sys
import signal

# import logging
# logging.basicConfig(level=logging.DEBUG)

# Open engine API
if (len(sys.argv) != 2):
    print(f"usage: python {sys.argv[0]}.py path/to/engine")
    exit(1)
myengine = Engine()
print("Opening chess engine API...", end="", flush=True)
myengine.open(sys.argv[1])
print("done", flush=True)


# Listen for interrupt signal to close engine API (Ctrl+C)
def handler():
    print("Closing chess engine API...", end="", flush=True)
    myengine.close()
    print("done")
    exit(0)
signal.signal(signal.SIGINT, handler)


# Actual listen function for websocket
async def listen(websocket):
    print("New connection!")

    async for message in websocket:
        msg: str = message
        res: str = ""
        print(f"Received: {msg}")

        # call proper function
        args: list[str] = msg.split(" ")

        if args[0] == "search":
            fenargs = args[1:-2]
            fenstr = ""
            for fenarg in fenargs:
                if (fenstr != ""): fenstr += " "
                fenstr += fenarg
            print(f"fen: \"{fenstr}\", wtime: {float(args[-2])}, btime: {float(args[-1])}")
            res = myengine.search(fenstr, float(args[-2]), float(args[-1]))

        print(f"Sending: {res}")
        await websocket.send(res)


async def main():
    async with serve(listen, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # run forever
asyncio.run(main())