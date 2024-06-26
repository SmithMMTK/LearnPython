
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
    [1, 2, 1, 3, 1, 0, 1, 0, 1, 1, 1, 1, 4, 1, 1],
    [1, 1, 0, 0, 1, 0, 2, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 3, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 2, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0, 1],
    [1, 5, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 2, 1, 0, 1, 1, 1, 0, 3, 0, 0, 1, 0, 1],
    [1, 0, 0, 2, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 2, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 3, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 2, 1, 1],
    [1, 0, 1, 1, 0, 2, 0, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 3],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 2, 1, 1, 0, 0, 1, 1, 3, 1, 1]
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
                print('\033[92m' + str(maze[row][col]) + '\033[0m', end=' ')
            else:
                if maze[row][col] >= 1:
                    print(maze[row][col], end=' ')  # Unvisited path cells
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

def canShortenSol1(path):
    
    # Loop through each position x,y in the path
    for turn in range(len(path) - 1):
        y, x = path[turn]
        
        # Calculate the eight possible directions: up, down, left, right, and diagonals
        possible_directions = [
            (y - 1, x),  # Up
            (y - 1, x + 1),  # Up-right
            (y, x + 1),  # Right
            (y + 1, x + 1),  # Down-right
            (y + 1, x),  # Down
            (y + 1, x - 1),  # Down-left
            (y, x - 1),  # Left
            (y - 1, x - 1)  # Up-left
        ]

        # Count toward position in the path from current position + 1 and then count the number of steps match with possible_directions
        # starting from for loop
        count = 0
        for pos in path[turn:]:
            if pos in possible_directions:
                count = count + 1

        
        # Check if three or more adjacent positions are part of the path
        if count >= 3:
            return True
    
    return False


# Define the start and end points of the maze
start = (0, 0)
end = (len(maze) - 1, len(maze[0]) - 1)

# List to store all possible solutions
solutions = []

# Start the maze solving process
solve_maze(maze, start, end, [], solutions)

# Display all found solutions
if not solutions:
    print("\nNo path found.")
else:

    # Check if the path can be shortened
    count = 0
    finalSolutions = []
    for path in solutions:

        if not canShortenSol1(path):
            finalSolutions.append(path)


    # Summarize solutions found with statistics and visualizations
    total_solutions = len(solutions)
    print("\nThere are ", total_solutions, "all path(s): to solve this maze")

    # Sorting solutions from shortest to longest
    # Add code to calculate the cost of solutions and sort by cost

    # Create two dimention array to store the cost of each path and index of the path
    costPath = []


    for i, path in enumerate(solutions, 1):
        ## Calculate cost of this path by cost = cost + path[x] and store in variable cost
        cost = 0
        for coord in path:
            cost += maze[coord[0]][coord[1]]
    
        # Print the path and its cost
        # print("Path", i, "and cost", cost)

        # Store the cost and index of the path in costPath including the length of the path
        costPath.append([cost, i, len(path)])


    print("\n")
    # Sorting the costPath array by cost
    costPath.sort()

    print("Sorted by cost")
    print("\n")
    for cost, index, pathLen in costPath:
        print("Path", index, "is cost", cost, "and take", pathLen, "steps.")
    
    print("\n")

    # Print the solution path from the costPath array
    for cost, index, PathLen in costPath:
        print_path_result(solutions[index - 1])
        print("\n")

    # Print the path with cost
    #for cost, index in costPath:
    #    print("Path", index, "and cost", cost)

    #for path in solutions:
    #    print_path_result(path)
    #    if path != solutions[-1]:  # Check if it's not the last path
    #        msg = "\n Rendering all solutions " + str(current) + "/" + str(len(solutions)) + "\n"
    #    print("\n")