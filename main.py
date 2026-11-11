from draughts import AmericanBoard, SimpleEngine
import sys

if len(sys.argv) == 2:
    STARTPOS = sys.argv[1]
else:
    STARTPOS = "W:W21-32:B1-12"

board = AmericanBoard().from_fen(STARTPOS)
engine = SimpleEngine()

# engine_move = engine.play(board, ponder=False)
move, score = engine.get_best_move(board, with_evaluation=True)
print(move)
board.push(move)
print(board)
print(board.fen)