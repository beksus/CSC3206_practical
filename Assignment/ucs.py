import heapq
from itertools import count



# === UCS Implementation ===

def ucs_all_treasures_with_traps(graph, start, TREASURES, TOTAL_TREASURES):
    visited = set()
    heap = []
    counter = count()

    heapq.heappush(heap, (
        0,                          # energy cost
        next(counter),              # tie-breaker
        graph[start],
        [start],
        1.0,                        # gravity
        1.0,                        # speed
        0,                          # gravity buffs
        0,                          # speed buffs
        []                          # collected treasures
    ))

    while heap:
        energy_used, _, cell, path, gravity, speed, g_buff, s_buff, seen = heapq.heappop(heap)

        key = (cell.coordinate, tuple(sorted(seen)))
        if key in visited:
            continue
        visited.add(key)

        new_gravity = gravity
        new_speed = speed
        g_buff_new = g_buff
        s_buff_new = s_buff
        seen_new = seen[:]

        # Handle traps and rewards
        if cell.type == -3:
            new_gravity *= 2
        elif cell.type == -2:
            new_speed *= 2
        elif cell.type == -1:
            if len(path) >= 3:
                back_cell_id = path[-3]
                back_path = path[:-2]
                heapq.heappush(heap, (
                    energy_used + 2 * new_gravity,
                    next(counter),
                    graph[back_cell_id],
                    back_path,
                    gravity,
                    speed,
                    g_buff,
                    s_buff,
                    seen[:]
                ))
            continue
        elif cell.type == -4:
            if len(seen) < TOTAL_TREASURES:
                continue
        elif cell.type == 1:
            new_gravity *= 0.5
            g_buff_new += 1
        elif cell.type == 2:
            new_speed *= 0.5
            s_buff_new += 1
        elif cell.type == 9:
            if cell.coordinate in TREASURES and cell.coordinate not in seen_new:
                seen_new.append(cell.coordinate)

        # Success condition
        if len(seen_new) == TOTAL_TREASURES:
            print("\n=== UCS: All Treasures Hunt Report ===")
            print("Path taken:        ", path)
            print("Steps taken:       ", len(path) - 1)
            print("Energy used:       ", energy_used)
            print("Gravity buffs:     ", g_buff_new)
            print("Speed buffs:       ", s_buff_new)
            print("Treasures gathered:", len(seen_new))
            print("Final gravity rate:", new_gravity)
            print("Final speed rate:  ", new_speed)
            return

        for child in cell.children:
            step_cost = int(1 * new_speed)
            next_energy = energy_used + step_cost * new_gravity
            heapq.heappush(heap, (
                next_energy,
                next(counter),
                child,
                path + [child.coordinate],
                new_gravity,
                new_speed,
                g_buff_new,
                s_buff_new,
                seen_new
            ))

    print("\nGame over. No complete treasure run.")


