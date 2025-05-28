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