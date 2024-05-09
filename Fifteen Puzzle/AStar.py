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

        while self.queue[0].depth < 20:
            self.queue[0].print_board()
            if self.queue[0] is not None and self.queue[0].is_solved():
                self.queue[0].last_move.pop(0)
                return self.queue[0].last_move, visited, processed, self.queue[0].depth, perf_counter() - start

            possible_moves = []

            for o in "URDL":
                next_move = self.queue[0].next_move(o)
                visited += 1
                if next_move is not None:
                    print(next_move.last_move)
                    possible_moves.append(next_move)

            count = []
            if order == "hamm":
                for move in possible_moves:
                    count.append(move.hamm_coutning())
                pick_index = count.index(max(count))
            
            elif order == "mahm":
                for move in possible_moves:
                    count.append(move.distance_sum())

                pick_index = count.index(min(count))

            print(*count)
                    
            
            self.queue.append(possible_moves[pick_index])

            self.queue.pop(0)
            processed += 1
        # Zwraca: solution, visited, processed, max_depth, duration
        pass