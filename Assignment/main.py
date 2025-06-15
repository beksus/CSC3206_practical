from bfs import bfs_all_treasures_with_traps
from ucs import ucs_all_treasures_with_traps
from astar import astar_all_treasures_with_traps

# Cell types: Legend
#  
#  1 = Reward 1 (gravity buff)
#  2 = Reward 2 (speed buff)
# -1 = Trap 1 (gravity debuff)
# -2 = Trap 2 (speed debuff)
# -3 = Trap 3 (pushback)
# -4 = Trap 4 (delete uncollected treasures)
#  9 = Treasure


# Cell types mapping
cell_types = {
    0: 0, 1: 0, 2 : 0, 4: 0, 5: 0, 6: 0,
    7: -2, 8: 0, 9: 1, 10: 0, 11: 0, 12: 0,
    13: 0, 15: 0, 16: -2, 17: 0, 18: 0, 19: -4,
    20: 0, 22: 9, 23: 0, 24: 1, 25: 9, 27: 0, 
    29: 0, 30: 0, 31: 0, 32: 0,
    33: -3, 34: 0, 35: 2, 36: 0, 37: -3,
    38: 0, 41: 0, 42: 0,
    43: 0, 44: 2, 45: 9, 47: 0, 48: 0,
    50: -1, 51: 0, 52: 0, 53: 0, 54: 0,
    55: 0, 56: 0, 57: 9, 58: 0, 59: 0
    }

# State space
state_space = [
    [0,1], [0,6], [0,7],
    [1,0], [1,7], [1,8],

    
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
