from random_board import RandomBoard


def test__random_board_init__should_contain_alive_cells():
    rb = RandomBoard(10, 10)

    counter = 0
    for x in rb.board:
        for y in rb[x]:
            if rb.board[x][y] == 1:
                counter += 1

    assert counter > 2
