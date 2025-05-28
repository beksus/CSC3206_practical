initial_state = "Arad"
goal_state = "Bucharest"

state_space = [
    ['Arad', 'Zerind', 75],
    ['Arad', 'Sibiu', 140],
    ['Arad', 'Timisoara', 118],
    ['Zerind', 'Oradea', 71],
    ['Oradea', 'Sibiu', 151],
    ['Timisoara', 'Lugoj', 111],
    ['Lugoj', 'Mehadia', 70],
    ['Mehadia', 'Drobeta', 75],
    ['Drobeta', 'Craiova', 120],
    ['Sibiu', 'Fagaras', 99],
    ['Sibiu', 'Rimnicu Vilcea', 80],
    ['Rimnicu Vilcea', 'Craiova', 146],
    ['Rimnicu Vilcea', 'Pitesti', 97],
    ['Craiova', 'Pitesti', 138],
    ['Fagaras', 'Bucharest', 211],
    ['Pitesti', 'Bucharest', 101],
    ['Bucharest', 'Giurgiu', 90],
    ['Bucharest', 'Urziceni', 85],
    ['Urziceni', 'Hirsova', 98],
    ['Hirsova', 'Eforie', 86],
    ['Urziceni', 'Vaslui', 142],
    ['Vaslui', 'Iasi', 92],
    ['Iasi', 'Neamt', 87]
]


class Node:
  def __init__(self, state=None, parent=None):
    self.state = state
    self.parent = parent
    self.children = []

  def addChildren(self, children):
    self.children.extend(children)

def expandAndReturnChildren(state_space, node):
  children = []
  for [n,m,c] in state_space:
    if n == node.state:
      childnode = Node(m, node)
      children.append(childnode)
    elif m == node.state:
      childnode = Node(n, node)
      children.append(childnode)
  return children

def bfs(state_space, initial_state, goal_state):
    # STEP 1 - Initialization
    frontier    = []        # the front-line, the CURRENT exploration/test node
    explored    = []        # list of nodes we already explored
    found_goal  = False
    frontier.append(Node(initial_state, None))  # first node in the frontier is the initial_state
    goal_node   = Node()
    solution    = []
    path_cost = 0

    # STEP 2 - Search for Goal Loop
    while not found_goal:

        # 2.1 Manage the Frontier & Explored Lists
        children = expandAndReturnChildren(state_space, frontier[0])
        frontier[0].addChildren(children)
        explored.append(frontier[0])
        del frontier[0]

        # 2.2 Goal Test
        for child in children:
            # first, check if node was alrady expanded or explored
            if not (child.state in [e.state for e in explored]) and not (child.state in [f.state for f in frontier]):
                # next, check if node is goal
                if child.state == goal_state:
                    found_goal = True       # end algorithm
                    print("Goal Found!")
                    goal_node = child       # for later processing
                frontier.append(child)      # to search deeper

        # 2.3 Progress output
        print("Explored:", [e.state for e in explored])
        print("Frontier:", [f.state for f in frontier])
        print("Children:", [c.state for c in children])
        print("")

    # STEP 3 Find Solution path
    solution = [goal_node.state]        # start from goal node
    trace_node = goal_node              # use the trace node to trace the path back to the initial node

    # 3.1 trace your steps and find the solution path
    while trace_node.parent is not None:                # are you back to the initial_state ?
        solution.insert(0, trace_node.parent.state)     # then find the parent and add it to the solution list
        trace_node = trace_node.parent                  # set trace to parent (to go back one level, and repeat)

    # 3.2 determine the cose of the solution path.
    for i in range(len(solution) - 1):
        city1 = solution[i]
        city2 = solution[i + 1]

        for [from_city, to_city, cost] in state_space:
            if (from_city == city1 and to_city == city2) or (from_city == city2 and to_city == city1):
                path_cost += cost
                break  # Exit once the matching pair is found

    return solution, path_cost

# Run the BFS algorithm and print the solution written by CSC3206 AI Labs
print('Solution: ' + str(bfs(state_space, initial_state, goal_state)))