from math import ceil

def bfs_all_treasures_with_traps(graph, start, TREASURES, TOTAL_TREASURES):
    visited = set()
    queue = []
    energy_used = 0

    # queue format: (cell, path, steps, gravity, speed, g_buffs, s_buffs, seen_treasures)
    queue.append((graph[start], [start], 0, 1.0, 1.0, 0, 0, []))  

    while queue:
        cell, path, steps, gravity, speed, g_buff, s_buff, seen = queue.pop(0)

        key = (cell.coordinate, tuple(sorted(seen)))
        if key in visited:
            continue
        visited.add(key)

        # Copy current state
        new_gravity = gravity
        new_speed = speed
        g_buff_new = g_buff
        s_buff_new = s_buff
        seen_new = list(seen)

        # Trap & Reward logic
        if cell.type == -3:  # Trap 3: pushback
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
                    list(seen)
                ))
            continue

        elif cell.type == -1:  # Trap 1: gravity debuff
            new_gravity *= 2
        elif cell.type == -2:  # Trap 2: speed debuff
            new_speed *= 2
        elif cell.type == -4:  # Trap 4: destroy uncollected treasures
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
                seen_new = seen_new + [cell.coordinate]  # avoid mutating shared list

        energy_used = steps * new_gravity  # energy = steps × gravity multiplier

        # Check if all treasures collected
        if len(seen_new) == TOTAL_TREASURES:
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

        # Expand neighbors
        for child in cell.children:
            new_steps = steps + ceil(1 * new_speed)  # avoid step becoming 0
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
