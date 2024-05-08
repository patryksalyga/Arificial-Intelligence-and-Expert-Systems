import argparse

from Board import Board
from AStar import Astr
from BreadthFirstSearch import Bfs
from DepthFirstSearch import Dfs

def main():
    parser = argparse.ArgumentParser(description='Solve the 15-puzzle.')
    parser.add_argument('strategy', choices=['bfs', 'dfs', 'astr'], help='The search strategy to use.')
    parser.add_argument('order', help='The order to search the neighborhood.')
    parser.add_argument('input_file', help='The input file with the initial board layout.')
    parser.add_argument('solution_file', help='The output file to write the solution to.')
    parser.add_argument('stats_file', help='The output file to write the stats to.')
    args = parser.parse_args()

    with open(args.input_file, 'r') as f:
        lines = f.readlines()
        w, k = map(int, lines[0].split())
        board_list = [list(map(int, line.split())) for line in lines[1:]]
        start_board = Board(board_list)

    if args.strategy == 'bfs':
        solver = Bfs(start_board)
    elif args.strategy == 'dfs':
        solver = Dfs(start_board)
    else:
        solver = Astr(start_board)

    
    solution, visited, processed, max_depth, duration = solver.solve(args.order)

    with open(args.solution_file, 'w') as f:
        for move in solution:
            f.write(move)

    with open(args.stats_file, 'w') as f:
        f.write(f'Length of solution: {len(solution)}\n')
        f.write(f'Number of visited states: {visited}\n')
        f.write(f'Number of processed states: {processed}\n')
        f.write(f'Max recursion depth: {max_depth}\n')
        f.write(f'Duration: {duration}\n')

if __name__ == '__main__':
    main()
