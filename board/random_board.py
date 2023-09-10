from .dead_board import DeadBoard
import random


class RandomBoard(DeadBoard):
    def __init__(self, width: int, height: int):
        super().__init__(width=width, height=height)
        self.__randomize_board()

    def __randomize_board(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                choice = random.choice([0, 1])
                if choice == 1:
                    cell_state = 1
                else:
                    cell_state = 0
                self.board[x][y] = cell_state
