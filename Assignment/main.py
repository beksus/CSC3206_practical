from bfs import bfs_all_treasures_with_traps
from ucs import ucs_all_treasures_with_traps
from astar import astar_all_treasures_with_traps

# Cell types mapping
cell_types = {
    0: 0, 1: -3, 2: 0, 3: -2, 4: 1,
    5: -1, 6: 0, 7: 9, 8: -4, 9: 0,
    10: 0, 11: 2, 12: 0, 13: 0, 14: 0,
    15: 9, 16: 9, 17: 0, 18: 9, 19: 1,
    20: 0, 21: -2, 22: -3, 23: -1
}

# State space
state_space = [
    [0, 1], [0, 5], [1, 0], [1, 2], [1, 6],
    [2, 1], [2, 3], [2, 7], [3, 2], [3, 4], [3, 8],
    [4, 3], [4, 9], [5, 0], [5, 6], [5, 10],
    [6, 1], [6, 5], [6, 7], [6, 11], [7, 2], [7, 6],
    [7, 8], [7, 12], [8, 3], [8, 7], [8, 9], [8, 13],
    [9, 4], [9, 8], [9, 14], [10, 5], [10, 11],
    [10, 15], [11, 6], [11, 10], [11, 12], [11, 16],
    [12, 7], [12, 11], [12, 13], [12, 17], [13, 8],
    [13, 12], [13, 14], [13, 18], [14, 9], [14, 13],
    [14, 19], [15, 10], [15, 16], [16, 11], [16, 15],
    [16, 17], [16, 22], [17, 12], [17, 16], [17, 18],
    [17, 23], [18, 13], [18, 17], [18, 19], [19, 14],
    [19, 18], [22, 16], [23, 17]
]

# Treasures
TREASURES = {7, 15, 16, 18}
TOTAL_TREASURES = len(TREASURES)

# Cell class
class Cell:
    def __init__(self, coordinate, cell_type):
        self.coordinate = coordinate
        self.type = cell_type
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Build graph
graph = {}
for i in cell_types:
    graph[i] = Cell(i, cell_types[i])
for frm, to in state_space:
    if frm in graph and to in graph:
        graph[frm].add_child(graph[to])

# Run search algorithms
start_node = 0

print("\n=== Running BFS ===")
bfs_all_treasures_with_traps(graph, start_node, TREASURES, TOTAL_TREASURES)

print("\n=== Running UCS ===")
ucs_all_treasures_with_traps(graph, start_node, TREASURES, TOTAL_TREASURES)

print("\n=== Running A* ===")
astar_all_treasures_with_traps(graph, start_node, TREASURES, TOTAL_TREASURES)
