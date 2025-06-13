
# BFS to collect all treasures while handling traps and rewards
def bfs_all_treasures_with_traps(graph, start, TREASURES, TOTAL_TREASURES):
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

