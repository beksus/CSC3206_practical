# Cell types: Legend
#  0 = normal
#  1 = Reward 1 (gravity buff)
#  2 = Reward 2 (speed buff)
# -1 = Trap 3 (pushback)
# -2 = Trap 2 (speed debuff)
# -3 = Trap 1 (gravity debuff)
# -4 = Trap 4 (delete uncollected treasures)
#  9 = Treasure

# Map cell types( have to remap it)
cell_types = {
    0: 0, 1: -3, 2: 0, 3: -2, 4: 1,
    5: -1, 6: 0, 7: 9, 8: -4, 9: 0,
    10: 0, 11: 2, 12: 0, 13: 0, 14: 0,
    15: 9, 16: 9, 17: 0, 18: 9, 19: 1,
    20: 0, 21: -2, 22: -3, 23: -1
}

# Adjacency list of connections (edges) (have to remap it)
state_space = [
    [0, 1], [0, 5],
    [1, 0], [1, 2], [1, 6],
    [2, 1], [2, 3], [2, 7],
    [3, 2], [3, 4], [3, 8],
    [4, 3], [4, 9],
    [5, 0], [5, 6], [5, 10],
    [6, 1], [6, 5], [6, 7], [6, 11],
    [7, 2], [7, 6], [7, 8], [7, 12],
    [8, 3], [8, 7], [8, 9], [8, 13],
    [9, 4], [9, 8], [9, 14],
    [10, 5], [10, 11], [10, 15],
    [11, 6], [11, 10], [11, 12], [11, 16],
    [12, 7], [12, 11], [12, 13], [12, 17],
    [13, 8], [13, 12], [13, 14], [13, 18],
    [14, 9], [14, 13], [14, 19],
    [15, 10], [15, 16],
    [16, 11], [16, 15], [16, 17], [16, 22],
    [17, 12], [17, 16], [17, 18], [17, 23],
    [18, 13], [18, 17], [18, 19],
    [19, 14], [19, 18],
    [22, 16], [23, 17]
]

# Treasures to collect (*remap it)
TREASURES = {7, 15, 16, 18}
TOTAL_TREASURES = len(TREASURES)

# Define Cell class
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

# BFS to collect all treasures while handling traps and rewards
def bfs_all_treasures_with_traps(start):
    visited = []
    queue = []
    queue.append((graph[start], [start], 0, 1.0, 1.0, 0, 0, []))  
    # (cell, path, steps, gravity, speed, g_buffs, s_buffs, seen_treasures)

    while queue:
        cell, path, steps, gravity, speed, g_buff, s_buff, seen = queue.pop(0)

        key = (cell.coordinate, tuple(sorted(seen)))
        if key in visited:
            continue
        visited.append(key)

        # Copy state
        new_gravity = gravity
        new_speed = speed
        g_buff_new = g_buff
        s_buff_new = s_buff
        seen_new = seen[:]

        # Handle trap and reward types
        if cell.type == -3:  # Trap 1: gravity debuff
            new_gravity *= 2
        elif cell.type == -2:  # Trap 2: speed debuff
            new_speed *= 2
        elif cell.type == -1:  # Trap 3: pushback
            if len(path) >= 3:
                back_cell_id = path[-3]
                back_path = path[:-2]
                queue.append((
                    graph[back_cell_id],
                    back_path,
                    steps + 2,
                    gravity,
                    speed,
                    g_buff,
                    s_buff,
                    seen[:]
                ))
            continue
        elif cell.type == -4:  # Trap 4: end game
            if len(seen) < TOTAL_TREASURES:
                continue  # treat as wall
        elif cell.type == 1:  # Reward 1: gravity buff
            new_gravity *= 0.5
            g_buff_new += 1
        elif cell.type == 2:  # Reward 2: speed buff
            new_speed *= 0.5
            s_buff_new += 1
        elif cell.type == 9:  # Treasure
            if cell.coordinate in TREASURES and cell.coordinate not in seen_new:
                seen_new.append(cell.coordinate)

        # If all treasures gathered
        if len(seen_new) == TOTAL_TREASURES:
            energy_used = steps * new_gravity
            print("\n=== All Treasures Hunt Report ===")
            print("Path taken:        ", path)
            print("Steps taken:       ", steps)
            print("Energy used:       ", energy_used)
            print("Gravity buffs:     ", g_buff_new)
            print("Speed buffs:       ", s_buff_new)
            print("Treasures gathered:", len(seen_new))
            print("Final gravity rate:", new_gravity)
            print("Final speed rate:  ", new_speed)
            return

        # Expand next moves
        for child in cell.children:
            new_steps = steps + int(1 * new_speed)
            queue.append((
                child,
                path + [child.coordinate],
                new_steps,
                new_gravity,
                new_speed,
                g_buff_new,
                s_buff_new,
                seen_new
            ))

    print("\nGame over. No complete treasure run.")

# Run the search
bfs_all_treasures_with_traps(0)

