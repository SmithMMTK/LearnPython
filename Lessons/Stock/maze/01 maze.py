
# Template for the maze project with basic functions
import time
import os 

# Render the maze function
def render_maze(maze):
    print("======================")
    print(" Maze to solve ")
    print("======================")
    for row in maze:
        print(' '.join([str(cell) for cell in row]))

# Test render_maze
maze = [
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0]
]

# Print the steps of the path
def print_path(path):
    # Step through each position in the path
    for position in path:
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("======================")
        print(" Path to solve ")
        print("======================")
        
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if (row, col) == position:
                    print('\033[92m' + 'P' + '\033[0m', end=' ')
                else:
                    if maze[row][col] == 1:
                        print('1', end=' ')  # Unvisited path cells
                    else:
                        print('0', end=' ')  # Walls
            print()
        time.sleep(0.5)  # Delay for 0.5 seconds

# Print the steps of the path
def print_path_result(path):

        
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            # Check if (row, col) is in the path
            if (row, col) in path:
                print('\033[92m' + 'P' + '\033[0m', end=' ')
            else:
                if maze[row][col] == 1:
                    print('1', end=' ')  # Unvisited path cells
                else:
                    print('0', end=' ')  # Walls
        print()

# Define the start and end points
start = (0, 0)
end = (9, 9)

# Define array to store the path
path = [(0, 0), (1, 0), (1,1),(2,1),(3,1),(4,1)]  # Dummy path for demonstration

# render_maze(maze)

print_path(path)

