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

        while self.queue[0].depth < 20:
            self.queue[0].print_board()

            if self.queue[0].depth > max_depth:
                max_depth = self.queue[0].depth

            if self.queue[0] is not None and self.queue[0].is_solved():
                self.queue[0].last_move.pop(0)
                return self.queue[0].last_move, visited, processed, max_depth, perf_counter() - start

            for o in order:
                next_move = self.queue[0].next_move(o)
                visited += 1
                if next_move is not None:
                    self.queue.insert(i, next_move)
                    i += 1
                    
            i = 1      
            self.queue.pop(0)
            processed += 1
        # Zwraca: solution, visited, processed, max_depth, duration
        pass