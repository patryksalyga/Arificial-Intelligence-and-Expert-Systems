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
            i = 1
            if order == "hamm":
                for move in possible_moves:
                    count.append(move.hamm_coutning())
                
                for r in count:
                    if self.queue[0].depth < 20:
                        self.queue.insert(i,possible_moves[count.index(max(count))])
                        possible_moves.pop(count.index(max(count)))
                        i += 1
            
            elif order == "mahm":
                for move in possible_moves:
                    count.append(move.distance_sum())

                for r in count:
                    if self.queue[0].depth < 20:
                        self.queue.insert(i, possible_moves[count.index(min(count))])
                        possible_moves.pop(count.index(min(count)))
                        i +=1

                
            self.queue.pop(0)
            processed += 1
        
        return -1, visited, processed, 20, perf_counter() - start
        # Zwraca: solution, visited, processed, max_depth, duration
        pass