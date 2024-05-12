from time import perf_counter

class Dfs:
    def __init__(self, board):
        self.board = board
        self.queue = []
        self.queue.append(self.board)

    def solve(self, order):
        # Implementacja metody solve dla strategii DFS.
        visited = 0
        processed = 0
        start = perf_counter()
        i = 1
        max_depth = 0

        while len(self.queue) > 0:
            #self.queue[0].print_board()

            if self.queue[0].depth > max_depth:
                max_depth = self.queue[0].depth

            if self.queue[0] is not None and self.queue[0].is_solved():
                self.queue[0].last_move.pop(0)
                return self.queue[0].last_move, visited, processed, max_depth, round((perf_counter() - start ) * 1000, 3)

            for o in order:
                next_move = self.queue[0].next_move(o)
                if next_move is not None:
                    if self.queue[0].depth < 10:
                        self.queue.insert(i, next_move)
                        visited += 1
                        i += 1
                    
            i = 1      
            self.queue.pop(0)
            processed += 1

        return -1, visited, processed, 20, round((perf_counter() - start ) * 1000, 3)
        # Zwraca: solution, visited, processed, max_depth, duration
        pass