
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
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1]
]

#maze = [
#    [1,1,1],
#    [1,1,1],
#    [1,1,1]
#]

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

# Define the solve_maze function
def solve_maze(maze, current, end, path_previous):
    path_result = path_previous[:]  # create a copy of the path to avoid mutating the original list in other branches
    maze = copy.deepcopy(maze)  # Create a deep copy of the maze here

    # Check if the current position is the end
    if current == end:
        path_result.append(current)
        return path_result

    # Mark the current position as visited
    maze[current[0]][current[1]] = 0
    path_result.append(current)

    # Check if move up is valid
    if is_valid_position(maze, (current[0]-1, current[1])):
        new_path = solve_maze(maze, (current[0]-1, current[1]), end, path_result)
        ## validation
        if new_path:
            return new_path

    # Check if move right is valid
    if is_valid_position(maze, (current[0], current[1]+1)):
        new_path = solve_maze(maze, (current[0], current[1]+1), end, path_result)
        ## validation
        if new_path:
            return new_path

    # Check if move down is valid
    if is_valid_position(maze, (current[0]+1, current[1])):
        new_path = solve_maze(maze, (current[0]+1, current[1]), end, path_result)
        ## validation
        if new_path:
            return new_path

    # Check if move left is valid
    if is_valid_position(maze, (current[0], current[1]-1)):
        new_path = solve_maze(maze, (current[0], current[1]-1), end, path_result)
        ## validation
        if new_path:
            return new_path

    # Backtrack: unmark the current position and remove from path

    #maze[current[0]][current[1]] = 1
    #path_result.pop()

    

    return None  # return None to indicate no valid path found from this position


# Define the start and end points
start = (0, 0)
end = (len(maze)-1, len(maze[0])-1)

# Define array to store the path
# path = [[0, 0], [1, 0], [1,1],[2,1],[3,1],[4,1]]  # Dummy path for demonstration

# Define the path to solve the maze start from [0,0]
path = []

# render_maze(maze)

render_maze(maze)

print("\nStart solving the maze...\n")

# Call the solve_maze function
path = solve_maze(maze, (0,0), end, path)

if path:
    print_path_result(path)
else:
    print("No path found")
