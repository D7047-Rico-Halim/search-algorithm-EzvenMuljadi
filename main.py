from graphs import bfs, dfs, ucs, greedy_bfs, a_star

# main.py

# Declare the graph as an adjacency list with edge weights
graph = {
    'A' : [('B', 1), ('C', 4)],
    'B' : [('A', 1), ('C', 2), ('D', 5)],
    'C' : [('A', 4), ('B', 2), ('D', 1), ('E', 3)],
    'D' : [('B', 5), ('C', 1), ('F', 2)],
    'E' : [('C', 3), ('F', 1)],
    'F' : [('D', 2), ('E', 1), ('G', 3)],
    'G' : [('F', 3)]
}

# Declare the heuristic values for each node
heuristics = {
    'A' : 7,
    'B' : 6,
    'C' : 4,
    'D' : 3,
    'E' : 2,
    'F' : 1,
    'G' : 0
}
