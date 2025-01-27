# LaziBoard

A Svelte chess application which can play with any UCI chess engine (only tested Stockfish).
Talks to a basic Python HTTP server to compute moves for the chess engine.

## How to Use

1. Download your preferred UCI chess engine and place the executable in
`engine_server/engines`. You'll have to create the directory.

2. Change directories into `/engine_server` in an Anaconda terminal. Then, download
the `chess` package if you haven't already and run the HTTP server:
```
pip install chess
python myhttp.py engines/executable_name
```

3. In a new terminal, download the necessary node modules and start the Svelte server:
```
pnpm i
pnpm dev
```