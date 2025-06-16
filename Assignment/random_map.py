# Randomly generated new cell types, state space, and treasures for UCS algorithm testing
import random

# Define total number of cells
NUM_CELLS = 60

# Possible cell types (excluding empty 0)
CELL_TYPE_OPTIONS = [1, 2, -1, -2, -3, -4, 9]

# Randomly assign cell types
cell_types_random = {i: random.choice([0] + CELL_TYPE_OPTIONS) for i in range(NUM_CELLS)}

# Ensure at least 4 treasures exist
treasure_cells = random.sample(range(NUM_CELLS), 4)
for cell in treasure_cells:
    cell_types_random[cell] = 9

# Generate random state space connections
state_space_random = []
for cell in range(NUM_CELLS):
    connections = random.sample([i for i in range(NUM_CELLS) if i != cell], random.randint(2, 4))
    for conn in connections:
        state_space_random.append([cell, conn])

# Deduplicate connections (make them undirected)
state_space_set = set()
for conn in state_space_random:
    a, b = sorted(conn)
    state_space_set.add((a, b))
state_space_random = [list(pair) for pair in state_space_set]

# Determine treasures
TREASURES_RANDOM = {cell for cell, val in cell_types_random.items() if val == 9}

# Print results
print("# Random Cell Types Mapping")
print("cell_types = {")
for k, v in cell_types_random.items():
    print(f"    {k}: {v},")
print("}")

print("\n# Random State Space")
print("state_space = [")
for conn in state_space_random:
    print(f"    {conn},")
print("]")

print("\n# Random Treasures")
print(f"TREASURES = {TREASURES_RANDOM}")
