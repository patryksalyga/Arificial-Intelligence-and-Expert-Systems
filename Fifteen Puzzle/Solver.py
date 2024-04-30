import time
from collections import deque

class Solver:
    def __init__(self, start_board):
        self.start_board = start_board
        self.visited = set()
        self.processed = set()

    def solve_bfs(self, order):
        order_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        visited = set()
        queue = deque([(self.start_board, "")])

        while queue:
            board, path = queue.popleft()
            if board.is_solved():
                return path

            for direction in order:
                dx, dy = order_map[direction]
                new_board = board.move(dx, dy)
                if new_board and new_board.get_list() not in visited:
                    visited.add(new_board.get_list())
                    queue.append((new_board, path + direction))

        return None


    def solve_dfs(self, order, max_depth=20):
        order_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        stack = [(self.start_board, "", 0)]
        max_reached_depth = 0

        start_time = time.time()
        while stack:
            board, path, depth = stack.pop()
            self.processed.add(board.get_list())
            if board.is_solved():
                end_time = time.time()
                return path, len(self.visited), len(self.processed), max_reached_depth, end_time - start_time

            if depth < max_depth:
                for direction in order:
                    dx, dy = order_map[direction]
                    new_board = board.move(dx, dy)
                    if new_board and new_board.get_list() not in self.visited:
                        self.visited.add(new_board.get_list())
                        stack.append((new_board, path + direction, depth + 1))
                        max_reached_depth = max(max_reached_depth, depth + 1)

        end_time = time.time()
        return None, len(self.visited), len(self.processed), max_reached_depth, end_time - start_time
