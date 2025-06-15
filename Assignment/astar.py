
import heapq
import itertools
from math import ceil

def heuristic(cell_coord, seen, TREASURES, graph):
    remaining = TREASURES - set(seen)
    if not remaining:
        return 0

    min_h = float('inf')
    for t in remaining:
        h = abs(cell_coord - t)
        if graph[t].type == -1: h += 2   # Penalty for gravity trap
        elif graph[t].type == 1: h -= 1  # Bonus for gravity buff
        min_h = min(min_h, h)
    # Assume best-case gravity (0.25) for admissibility
    return min_h * 0.25

def astar_all_treasures_with_traps(graph, start, TREASURES, TOTAL_TREASURES):
    visited = set()
    heap = []
    counter = itertools.count()

    heapq.heappush(heap, (
        0, next(counter), 0, graph[start], [start], 1.0, 1.0, 0, 0, []
    ))

    while heap:
        f_cost, _, energy_used, cell, path, gravity, speed, g_buff, s_buff, seen = heapq.heappop(heap)

        # Improved visited key: includes gravity, speed, and seen treasures
        key = (cell.coordinate, tuple(sorted(seen)), round(gravity, 2), round(speed, 2))
        if key in visited:
            continue
        visited.add(key)

        new_gravity = gravity
        new_speed = speed
        g_buff_new = g_buff
        s_buff_new = s_buff
        seen_new = list(seen)

        # === Handle Traps and Rewards ===
        if cell.type == -1:  # Trap 1: gravity debuff
            new_gravity *= 2
        elif cell.type == -2:  # Trap 2: speed debuff
            new_speed *= 2
        elif cell.type == -3:  # Trap 3: pushback
            if len(path) >= 3:
                back_cell_id = path[-3]
                back_path = path[:-2]
                heapq.heappush(heap, (
                    energy_used + 2 * new_gravity,
                    next(counter),
                    energy_used + 2 * new_gravity,
                    graph[back_cell_id],
                    back_path,
                    gravity,
                    speed,
                    g_buff,
                    s_buff,
                    list(seen)
                ))
            continue
        elif cell.type == -4:  # Trap 4: kill if treasures not all
            if len(seen) < TOTAL_TREASURES:
                continue
        elif cell.type == 1:  # Reward 1: gravity buff
            new_gravity *= 0.5
            g_buff_new += 1
        elif cell.type == 2:  # Reward 2: speed buff
            new_speed *= 0.5
            s_buff_new += 1
        elif cell.type == 9:  # Treasure
            if cell.coordinate in TREASURES and cell.coordinate not in seen_new:
                seen_new = seen_new + [cell.coordinate]

        # === Goal Check ===
        if len(seen_new) == TOTAL_TREASURES:
            print("\n=== A* All Treasures Hunt Report ===")
            print("Path taken:        ", path)
            print("Steps taken:       ", len(path) - 1)
            print("Energy used:       ", round(energy_used, 2))
            print("Gravity buffs:     ", g_buff_new)
            print("Speed buffs:       ", s_buff_new)
            print("Treasures gathered:", len(seen_new))
            print("Final gravity rate:", new_gravity)
            print("Final speed rate:  ", new_speed)
            return

        # === Expand Children ===
        for child in cell.children:
            step_cost = ceil(1 * new_speed)
            next_energy = energy_used + step_cost * new_gravity
            h = heuristic(child.coordinate, seen_new, TREASURES, graph)
            total_cost = next_energy + h

            heapq.heappush(heap, (
                total_cost,
                next(counter),
                next_energy,
                child,
                path + [child.coordinate],
                new_gravity,
                new_speed,
                g_buff_new,
                s_buff_new,
                seen_new
            ))

    print("\nGame over. No complete treasure run.")