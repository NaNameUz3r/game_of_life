import pytest
from dead_board import DeadBoard


def test__dead_board_init__returns_2d_emtpy_array():
    new_board = DeadBoard(2, 2)
    assert new_board.board[0][0] == 0
    assert len(new_board.board[1]) == 2
