import chess
import chess.engine

class Engine:
    def __init__(self):
        self.engine: chess.engine.SimpleEngine
        self.board = chess.Board()

    def open(self, dir: str):
        self.engine = chess.engine.SimpleEngine.popen_uci(dir)

    def close(self):
        self.engine.quit()

    def search(self, fen: str, wtime: float, btime: float):
        # wtime and btime are in SECONDS
        self.board.set_fen(fen)
        result = self.engine.play(self.board, chess.engine.Limit(white_clock=wtime, black_clock=btime, white_inc=0, black_inc=0))
        return result.move.uci()