
# Template for the maze project with basic functions
import time
import os 
import copy

# Render the maze function
def render_maze(maze):
    print("======================")
    print(" Maze to solve ")
    print("======================")
    for row in maze:
        print(' '.join([str(cell) for cell in row]))

# Test render_maze
maze = [
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
]

#maze = [
#    [1,1,1],
#    [1,1,1],
#    [1,1,1]
#]

# Print the steps of the path
def print_path(path):
    # Step through each position in the path
    countDown = len(path) - 1
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
        print("Turns: ", countDown)
        countDown = countDown - 1
        time.sleep(0.1)  # Delay for 0.5 seconds

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


# Check if the current position is a wall or out of bounds
def is_valid_position(maze, position):
    # Check if the row is out of bounds
    if position[0] < 0 or position[0] >= len(maze):
        return False
    # Check if the column is out of bounds
    if position[1] < 0 or position[1] >= len(maze[0]):
        return False
    # Check if the cell is a wall
    if maze[position[0]][position[1]] == 0:
        return False
    return True

import copy

def solve_maze(maze, current, end, path_previous, solutions):
    # Create a local deep copy of the maze to prevent modifying the original during recursion
    maze = copy.deepcopy(maze)
    path_result = path_previous[:]  # Make a copy of the current path
    path_result.append(current)

    # Check if the current position is the end
    if current == end:
        solutions.append(path_result)
        return

    # Mark the current position as visited to avoid revisiting
    maze[current[0]][current[1]] = 0

    # Explore all four possible directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for row, column in directions:
        new_pos = (current[0] + row, current[1] + column)
        if is_valid_position(maze, new_pos):
            solve_maze(maze, new_pos, end, path_result, solutions)

# Function to check if a position is within the maze bounds and not a wall
def is_valid_position(maze, position):
    if position[0] < 0 or position[0] >= len(maze):
        return False
    if position[1] < 0 or position[1] >= len(maze[0]):
        return False
    return maze[position[0]][position[1]] == 1

# Define the start and end points of the maze
start = (0, 0)
end = (len(maze) - 1, len(maze[0]) - 1)

# List to store all possible solutions
solutions = []

# Start the maze solving process
solve_maze(maze[:], start, end, [], solutions)

# Display all found solutions
if not solutions:
    print("\nNo path found.")
else:

    # Summarize solutions found with sataistics and visualizations

    # Summarize solutions found with statistics and visualizations
    total_solutions = len(solutions)
    print("\nThere are ", total_solutions, "path(s): to solve this maze")
    for i, path in enumerate(solutions, 1):
        print("Path", i, "and take", len(path), "steps.")

    #msg = "Press Enter to view path 1/" + str(len(solutions)) + "\n"
    #print(msg)

    #input(msg)  # Wait for user to press Enter


    print("\n")
    current = 1

    # Sorting solutions from shortest to longest
    solutions.sort(key=len)

    for path in solutions:
        print_path_result(path)
        current = current + 1
        if path != solutions[-1]:  # Check if it's not the last path
            msg = "\n Rendering solutions " + str(current) + "/" + str(len(solutions)) + "\n"
            #input(msg)  # Wait for user to press Enter
            #print(msg)
            # Wait 3 seconds before displaying the next path
           # time.sleep(3)
        print("\n")
    print("All solutions have been displayed.")



