import bfs
import ucs
import astar

def main():
    print("Welcome to the Pathfinding Algorithms Program!")
    print("Please choose an algorithm:")
    print("1. Breadth-First Search (BFS)")
    print("2. Uniform Cost Search (UCS)")
    print("3. A* Search")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        bfs.py.run_bfs()
    elif choice == '2':
        ucs.py.run_ucs()
    elif choice == '3':
        astar.py.run_astar()
    else:
        print("Invalid choice. Please try again.")