# 
# Create canvas and move a prompt around
# Detect collision with the edge of the screen
# Playable area is max_x-1 and max_y-2
# Add innertia to the prompt
# Add Tail to the prompt every TURN_TIME

import curses


## Define constants
# Time in milliseconds to wait for user input
THINGTIME = 500

# Number of turns to add a new element to the tail
TUNRN_TIME = 10


# Check if the prompt is at the edge of the screen
# Playable area is max_x-1 and max_y-2
def promptIsOutbound(x, y, max_x, max_y):
    if (x < 0 or x > max_x-1 or y < 0 or y > max_y-2):
        return True
    else:
        return False

# Display coordinates of the prompt
def displayCoordinates(stdscr, x, y, max_x, max_y,turn,length):
    # Display the coordinates of the prompt with colors
    stdscr.addstr(max_y-1, 0, f"({x}, {y}), turn {turn}, tail length {length}", curses.color_pair(1))

  
    ## Show another information
    #
    #
    #

# Reposition the tail of the prompt
def repositionHeadTail(promptTail, y, x):
    # Set the y,x of the first element with moveDirection
    promptTail[0] = [y,x]

    return promptTail 


def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    # Enable color mode
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Initial position of the prompt
    x, y = 0, 0

    # Turn counter (every TURN_TIME) and start by -1 to add the first element of the promptTail list
    turn = -1

    # Initial velocity of the prompt
    moveDirection = "RIGHT"


    # Prompt tail list
    promptTail = []
    # assign the first element of the promptTail list to the current position of the prompt with moveDirection
    promptTail.append([x,y])

    

    firstTime = True
        

    while True:
        
        # Turn counter
        turn += 1

        if turn == TUNRN_TIME:
            promptTail.append([x,y])
            turn = 0
        
        
        # Get the screen dimensions
        max_y, max_x = stdscr.getmaxyx()
        


        # Display the prompt and instructions to the user
        if firstTime:
            # Display the prompt for movement
            stdscr.addstr(max_y-1, 0, "Move me with arrow keys (Press 'q' to quit)")
            #Pause the program until user input
            stdscr.getch()
            firstTime = False
        else:
            stdscr.clear()
            # Display the coordinates of the prompt
            displayCoordinates(stdscr, x, y,max_x,max_y,turn,len(promptTail)) 
        
        

        # Display the prompt at the current position
        stdscr.addstr(y, x, "█")
        

        # Refresh the screen to display changes
        stdscr.refresh()
        
        ## End of display ## 

        # Move the prompt according to the velocity of the prompt (moveDirection) if no input is given in 1 second
        # If the prompt is move beyond the edge of the screen, stop the prompt and display a message



        # Get user input
        # Get user input with a 0-millisecond timeout (non-blocking)
        stdscr.timeout(THINGTIME)
        key = stdscr.getch()
        
        # Detect key input or timeout
        if key == -1:
            # No key input
            if moveDirection == "RIGHT":
                x += 1
            elif moveDirection == "LEFT":
                x -= 1
            elif moveDirection == "DOWN":
                y += 1
            elif moveDirection == "UP":
                y -= 1
        else:
            # Key input
            # Handle user input
            if key == ord('q'):
                break
            elif key == curses.KEY_RIGHT:
                x += 1
                moveDirection = "RIGHT"
            elif key == curses.KEY_LEFT:
                x -= 1
                moveDirection = "LEFT"
            elif key == curses.KEY_DOWN:
                y += 1
                moveDirection = "DOWN"
            elif key == curses.KEY_UP:
                y -= 1
                moveDirection = "UP"
        
        # Check if the prompt is at the edge of the screen
        if promptIsOutbound(x, y, max_x, max_y):
            stdscr.clear()
            stdscr.addstr(max_y-1, 0, "You hit the edge of the screen! Press any key to continue...")
            stdscr.refresh()
            # Wait for your input to continue
            stdscr.getch()
            break

        # Reposition the tail of the prompt
        promptTail = repositionHeadTail(promptTail, y, x)
           
            

if __name__ == "__main__":
    curses.wrapper(main)
