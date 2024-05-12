import os
import matplotlib.pyplot as plt
import numpy as np

from Board import Board
from AStar import Astr
from BreadthFirstSearch import Bfs
from DepthFirstSearch import Dfs

def run_algorithms_and_plot():
    orders = ["RDUL", "RDLU", "DRUL", "DRLU", "LUDR", "LURD", "ULDR", "ULRD"]
    heuristics = ["mahm", "hamm"]
    algorithms = ["bfs", "dfs", "a*"]
    folder_path = "puzzle"
    results = {}
    success_rates = {}
    max_depths = {}
    processed_states = {}
    visited_states = {}
    i = 0

    for algorithm in algorithms:
        for file in os.listdir(folder_path):
            if file.endswith(".txt"):
                with open(os.path.join(folder_path, file), 'r') as f:
                    lines = f.readlines()
                    puzzle = Board([list(map(int, line.split())) for line in lines[1:]])
                
                # Pobierz głębokość z nazwy pliku
                depth = int(file.split('_')[1])

                if algorithm == "a*":
                    for heuristic in heuristics:
                        alg = Astr(puzzle)
                        result = alg.solve(heuristic)
                        results.setdefault((algorithm, heuristic, depth), []).append(result[4])
                        success_rates.setdefault((algorithm, heuristic, depth), []).append(1 if result[0] != -1 else 0)
                        max_depths.setdefault((algorithm, heuristic, depth), []).append(result[3])
                        processed_states.setdefault((algorithm, heuristic, depth), []).append(result[2])
                        visited_states.setdefault((algorithm, heuristic, depth), []).append(result[1])
                elif algorithm == "bfs":
                    for order in orders:
                        alg = Bfs(puzzle)
                        result = alg.solve(order)
                        results.setdefault((algorithm, order, depth), []).append(result[4])
                        success_rates.setdefault((algorithm, order, depth), []).append(1 if result[0] != -1 else 0)
                        max_depths.setdefault((algorithm, order, depth), []).append(result[3])
                        processed_states.setdefault((algorithm, order, depth), []).append(result[2])
                        visited_states.setdefault((algorithm, order, depth), []).append(result[1])
                else:  # dfs
                    for order in orders:
                        alg = Dfs(puzzle)
                        result = alg.solve(order)
                        results.setdefault((algorithm, order, depth), []).append(result[4])
                        success_rates.setdefault((algorithm, order, depth), []).append(1 if result[0] != -1 else 0)
                        max_depths.setdefault((algorithm, order, depth), []).append(result[3])
                        processed_states.setdefault((algorithm, order, depth), []).append(result[2])
                        visited_states.setdefault((algorithm, order, depth), []).append(result[1])

                print(i)
                i += 1

    # Obliczanie średnich czasów
    avg_times = {key: sum(values) / len(values) for key, values in results.items()}
    avg_success_rates = {key: sum(values) / len(values) for key, values in success_rates.items()}
    avg_max_depths = {key: sum(values) / len(values) for key, values in max_depths.items()}
    avg_processed_states = {key: sum(values) / len(values) for key, values in processed_states.items()}
    avg_visited_states = {key: sum(values) / len(values) for key, values in visited_states.items()}

    metrics = [(avg_times, 'czasów przetwarzania', 'Średni czas przetwarzania'),
               (avg_success_rates, 'skuteczności', 'Średnia skuteczność'),
               (avg_max_depths, 'maksymalnej głębokości', 'Średnia maksymalna głębokość'),
               (avg_processed_states, 'ilości przetworzonych stanów', 'Średnia ilość przetworzonych stanów'),
               (avg_visited_states, 'odwiedzonych stanów', 'Średnia ilość odwiedzonych stanów')]

    for avg_metric, metric_name, ylabel in metrics:
        depths = range(1, 8)  # Ustawiamy głębokość od 1 do 7
        width = 1 / (len(orders) + 1)  

        # Wykres dla BFS
        plt.figure(figsize=(15, 10))
        legend_added = []
        for (algorithm, param, depth), avg_value in avg_metric.items():
            if algorithm == "bfs":
                plt.bar(depth - 0.5 + orders.index(param) * width, avg_value, width, label=f'{param}' if param not in legend_added else "", color=f'C{orders.index(param)}')
                if param not in legend_added:
                    legend_added.append(param)
        plt.title(f'Porównanie {metric_name} dla BFS')
        plt.xlabel('Głębokość')
        plt.ylabel(ylabel)
        plt.xticks(np.arange(len(depths)) + 8.0 * width, depths)  
        plt.legend()
        plt.show()

        # Wykres dla DFS
        plt.figure(figsize=(15, 10))
        legend_added = []
        for (algorithm, param, depth), avg_value in avg_metric.items():
            if algorithm == "dfs":
                plt.bar(depth - 0.5 + orders.index(param) * width, avg_value, width, label=f'{param}' if param not in legend_added else "", color=f'C{orders.index(param)}')
                if param not in legend_added:
                    legend_added.append(param)
        plt.title(f'Porównanie {metric_name} dla DFS')
        plt.xlabel('Głębokość')
        plt.ylabel(ylabel)
        plt.xticks(np.arange(len(depths)) + 8.0 * width, depths)  
        plt.legend()
        plt.show()

        # Wykres dla A*
        plt.figure(figsize=(15, 10))
        legend_added = []
        for (algorithm, param, depth), avg_value in avg_metric.items():
            if algorithm == "a*":
                plt.bar(depth - 0.5 + heuristics.index(param) * width, avg_value, width, label=f'{param}' if param not in legend_added else "", color=f'C{heuristics.index(param)}')
                if param not in legend_added:
                    legend_added.append(param)
        plt.title(f'Porównanie {metric_name} dla A*')
        plt.xlabel('Głębokość')
        plt.ylabel(ylabel)
        plt.xticks(np.arange(len(depths)) + 5.0 * width, depths)
        plt.legend()
        plt.show()

        # Oblicz średnią wartość dla każdego algorytmu lub heurystyki
        avg_values = {}
        for (algorithm, param, _), value in avg_metric.items():
            if algorithm in ['bfs', 'dfs']:
                if algorithm not in avg_values:
                    avg_values[algorithm] = [value]
                else:
                    avg_values[algorithm].append(value)
            elif algorithm == 'a*' and param in ['mahm', 'hamm']:
                if param not in avg_values:
                    avg_values[param] = [value]
                else:
                    avg_values[param].append(value)

        for key in avg_values:
            avg_values[key] = sum(avg_values[key]) / len(avg_values[key])

        # Generuj wykres porównawczy
        plt.figure(figsize=(15, 10))
        ind = np.arange(len(avg_values))  
        width = 0.35  

        for i, (key, avg_value) in enumerate(avg_values.items()):
            plt.bar(ind[i], avg_value, width, label=f'{key}', color=f'C{i}')

        plt.title(f'Porównanie {metric_name} dla wszystkich algorytmów')
        plt.xlabel('Algorytm lub Heurystyka')
        plt.ylabel(ylabel)
        plt.xticks(ind, list(avg_values.keys()))  
        plt.legend()
        plt.show()




run_algorithms_and_plot()
