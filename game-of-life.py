import numpy as np
from board.dead_board import DeadBoard


x = DeadBoard(width=5, height=8)

print(np.matrix(x.board))
