import heapq
import itertools



# Heuristic function
def heuristic(cell_coord, seen, speed, TREASURES):
    remaining = TREASURES - set(seen)
    if not remaining:
        return 0
    min_dist = min(abs(cell_coord - t) for t in remaining)
    return min_dist * (1 / speed)

# A* with trap/buff logic
def astar_all_treasures_with_traps(graph, start, TREASURES, TOTAL_TREASURES):
    visited = set()
    heap = []
    counter = itertools.count()  # Unique counter for tie-breaking

    # (f_cost, count, g_cost, cell, path, gravity, speed, g_buffs, s_buffs, seen_treasures)
    heapq.heappush(heap, (
        0, next(counter), 0, graph[start], [start], 1.0, 1.0, 0, 0, []
    ))

    while heap:
        f_cost, _, energy_used, cell, path, gravity, speed, g_buff, s_buff, seen = heapq.heappop(heap)

        key = (cell.coordinate, tuple(sorted(seen)))
        if key in visited:
            continue
        visited.add(key)

        new_gravity = gravity
        new_speed = speed
        g_buff_new = g_buff
        s_buff_new = s_buff
        seen_new = seen[:]

        # Trap / Reward logic
        if cell.type == -3:
            new_gravity *= 2
        elif cell.type == -2:
            new_speed *= 2
        elif cell.type == -1:
            if len(path) >= 3:
                back_cell_id = path[-3]
                back_path = path[:-2]
                heapq.heappush(heap, (
                    energy_used + 2 * gravity,
                    next(counter),
                    energy_used + 2 * gravity,
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

        if len(seen_new) == TOTAL_TREASURES:
            print("\n=== All Treasures Hunt Report ===")
            print("Path taken:        ", path)
            print("Steps taken:       ", len(path) - 1)
            print("Energy used:       ", round(energy_used, 2))
            print("Gravity buffs:     ", g_buff_new)
            print("Speed buffs:       ", s_buff_new)
            print("Treasures gathered:", len(seen_new))
            print("Final gravity rate:", new_gravity)
            print("Final speed rate:  ", new_speed)
            return

        for child in cell.children:
            step_cost = 1 / new_speed
            next_energy = energy_used + step_cost * new_gravity
            h = heuristic(child.coordinate, seen_new, new_speed)
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

