import random

num_nodes = 60
max_edges_per_node = 6  # Max neighbors per node
possible_cell_types = [-4, -3, -2, -1, 0, 1, 2, 9]
num_treasures = 3

# Generate cell_types
cell_types = {}
for node in range(num_nodes):
    cell_types[node] = random.choice(possible_cell_types)

# Ensure exactly num_treasures treasures (value 9)
treasure_nodes = random.sample(range(num_nodes), num_treasures)
for node in treasure_nodes:
    cell_types[node] = 9

# Generate state_space (no self-loops, no duplicate edges)
state_space = []
connections = {i: set() for i in range(num_nodes)}

for node in range(num_nodes):
    current_edges = len(connections[node])
    max_possible_new_edges = max_edges_per_node - current_edges
    if max_possible_new_edges <= 0:
        continue  # Node already has max edges

    min_edges = min(2, max_possible_new_edges)  # At least 2 if possible
    max_edges = max_possible_new_edges

    if max_edges < 2:
        num_edges = max_edges  # If less than 2 possible, take whatever possible
    else:
        num_edges = random.randint(2, max_edges)

    possible_neighbors = [n for n in range(num_nodes) if n != node and len(connections[n]) < max_edges_per_node and n not in connections[node]]
    neighbors = random.sample(possible_neighbors, min(num_edges, len(possible_neighbors)))

    for neighbor in neighbors:
        if neighbor not in connections[node]:
            state_space.append([node, neighbor])
            connections[node].add(neighbor)
            connections[neighbor].add(node)  # Ensure bidirectional edge

# Output in required format
print("cell_types = {" + ", ".join(f"{k}: {v}" for k, v in cell_types.items()) + "}")
print("\nstate_space = [" + ", ".join(str(edge) for edge in state_space) + "]")
print(f"\nTREASURES = {set(treasure_nodes)}")