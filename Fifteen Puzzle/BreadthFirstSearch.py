from time import perf_counter

class Bfs:
    def __init__(self, board):
        self.board = board
        self.queue = []
        self.queue.append(self.board)


    def solve(self, order):
        # Implementacja metody solve dla strategii BFS.
        visited = 0
        processed = 0
        start = perf_counter()

        while len(self.queue) > 0:
            self.queue[0].print_board()
            if self.queue[0] is not None and self.queue[0].is_solved():
                self.queue[0].last_move.pop(0)
                return self.queue[0].last_move, visited, processed, self.queue[0].depth, perf_counter() - start

            for o in order:
                next_move = self.queue[0].next_move(o)
                visited += 1
                if next_move is not None:
                    if self.queue[0].depth < 20:
                        self.queue.append(next_move)
                    
                    
            self.queue.pop(0)
            processed += 1
   
        # Zwraca: solution, visited, processed, max_depth, duration
        # NIE WIEM GDZIE PROCESSED I VISITED
        pass