class DeadBoard:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = [[0] * width] * height
