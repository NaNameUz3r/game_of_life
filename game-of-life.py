import numpy as np
from board.dead_board import DeadBoard
from board.random_board import RandomBoard


x = DeadBoard(width=5, height=8)
y = RandomBoard(width=20, height=20)

print(np.matrix(y.board))
