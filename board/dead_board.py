class DeadBoard:
    def __init__(self, width: int, height: int):
        self.board = [[0 for _ in range(height)] for _ in range(width)]
