class Board:
    def __init__(self, list, last_move=None):
        self.list = list
        self.last_move = last_move
        
    def get_list(self):
        return self.list


    def is_solved(self):
        return self.list == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
