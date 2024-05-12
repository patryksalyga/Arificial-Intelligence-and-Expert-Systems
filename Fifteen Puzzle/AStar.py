from time import perf_counter

class Astr:
    def __init__(self, board):
        self.board = board
        self.queue = []
        self.queue.append(self.board)

    def solve(self, order):
        # Implementacja metody solve dla strategii A*.
        visited = 0
        processed = 0
        start = perf_counter()

        while len(self.queue) > 0:
            #self.queue[0].print_board()
            if self.queue[0] is not None and self.queue[0].is_solved():
                self.queue[0].last_move.pop(0)
                return self.queue[0].last_move, visited, processed, self.queue[0].depth, round((perf_counter() - start ) * 1000, 3)

            for o in "URDL":
                next_move = self.queue[0].next_move(o)
                if next_move is not None:
                    if self.queue[0].depth < 10:
                        #print(next_move.last_move)
                        self.queue.append(next_move)
                        visited += 1
     
            self.queue.pop(0)

            if order == "mahm":
                self.queue = sorted(self.queue, key=lambda Board: Board.distance_sum())
            elif order == "hamm":
                self.queue = sorted(self.queue, key=lambda Board: Board.hamm_coutning())
            
            processed += 1
        
        return -1, visited, processed, 20, round((perf_counter() - start ) * 1000, 3)
        # Zwraca: solution, visited, processed, max_depth, duration
        pass