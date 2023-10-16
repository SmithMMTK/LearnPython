# 
# Create canvas and move a prompt around
# Detect collision with the edge of the screen
# Playable area is max_x-1 and max_y-2
# Add innertia to the prompt
# Add Tail to the prompt every TURN_TIME
# Slide the tail of the prompt

import curses


## Define constants
# Time in milliseconds to wait for user input
THINGTIME = 150

# Number of turns to add a new element to the tail
TUNRN_TIME = 5

# GAMEMODE
GAMEMODE = 'RESTART'

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


# Display the prompt
def paintPrompt(stdscr, x, y, promptTail,turnTime,turnHistory):
    
    # Check length of the promptTail if it is longer than 1 do the following
    if len(promptTail) > 1:
        # Print the first element of the promptTail list
        stdscr.addstr(y, x, "█")
        # Loop through the promptTail list
        for i in range(1,len(promptTail)):
            # Get the y,x of the element turrnHistory[turnTime-i]
            y1 = turnHistory[turnTime-i][0]
            x1 = turnHistory[turnTime-i][1]
            # Display the prompt
            stdscr.addstr(y1, x1, "█")
            # check if y,x of the element is the same as the current position of the prompt
            if y1 == y and x1 == x:
                return False
        # Refresh the screen to display changes
    else:
        # Display the prompt
        stdscr.addstr(y, x, "█")
        # Refresh the screen to display changes
    
    stdscr.refresh()
    return True

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

    # Initial length of the prompt
    promptLength = 1

    # Initial velocity of the prompt
    moveDirection = "RIGHT"

    # Prompt tail list
    promptTail = []
    # assign the first element of the promptTail list to the current position of the prompt with moveDirection
    promptTail.append([x,y])

    # Turn history
    turnHistory = []
    turnHistory.append([x,y])
    turnTime = -1
    

    firstTime = True
    
    # Get the screen dimensions
    max_y, max_x = stdscr.getmaxyx()

    while True:
        
        # Turn counter
        turn += 1
        turnTime += 1

        # Add a new tail to the prompt every TURN_TIME
        if turn == TUNRN_TIME:
            # Add a new element to the tail of the prompt with the current position of the prompt
            promptTail.append([y,x])
            # Add 1 to the length of the prompt
            promptLength += 1
            turn = -1
        
        

        


        # Display the prompt and instructions to the user
        if firstTime:
            # Display the prompt for movement
            stdscr.addstr(max_y-1, 0, "Move me with arrow keys or press 'q' to quit)")
            #Pause the program until user input
            stdscr.getch()
            firstTime = False
        else:
            stdscr.clear()
            # Display the coordinates of the prompt
            displayCoordinates(stdscr, x, y,max_x,max_y,turn,len(promptTail)) 
        
        
        ## Display the prompt ##

        ## if paintPrompt returns False, break the loop
        if not (paintPrompt(stdscr, x, y, promptTail,turnTime,turnHistory)):
            #stdscr.clear()
            stdscr.timeout(-1) 
            stdscr.addstr(max_y-1, 0, "You hit the tail of the snake ! (Press 'r' to restart or 'q' to quit)...")
            stdscr.refresh()
            while True:
                key = stdscr.getch()
                if key == ord('q'):
                    GAMEMODE = 'QUIT'
                    break
                elif key == ord('r'):
                    GAMEMODE = 'RESTART'
            break


        
        ## End of display ## 

        # Move the prompt according to the velocity of the prompt (moveDirection) if no input is given in 1 second
        # If the prompt is move beyond the edge of the screen, stop the prompt and display a message



        # Get user input
        # Get user input with a 0-millisecond timeout (non-blocking)
        # Use following line for debugging
        # stdscr.timeout(-1)
        stdscr.timeout(THINGTIME)
        key = stdscr.getch()
        
        # Check opposite direction of the prompt
        oppositeDirection = False
        if len(turnHistory) > 1:
            if key == curses.KEY_RIGHT and moveDirection == "LEFT":
                oppositeDirection = True
            elif key == curses.KEY_LEFT and moveDirection == "RIGHT":
                oppositeDirection = True
            elif key == curses.KEY_DOWN and moveDirection == "UP":
                oppositeDirection = True
            elif key == curses.KEY_UP and moveDirection == "DOWN":
                oppositeDirection = True
        

        # Detect key input or timeout
        if key == -1 or oppositeDirection:
            # No key input
            if moveDirection == "RIGHT":
                x += 1
            elif moveDirection == "LEFT":
                x -= 1
            elif moveDirection == "DOWN":
                y += 1
            elif moveDirection == "UP":
                y -= 1
            oppositeDirection = False
        else:
            # Key input
            # Handle user input
            if key == ord('q'):
                GAMEMODE = 'QUIT'
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
            #stdscr.clear()
            stdscr.timeout(-1) 
            stdscr.addstr(max_y-1, 0, "You hit the edge of the screen! (Press 'r' to restart or 'q' to quit)...")
            stdscr.refresh()
            # While loop to wait until user press q
            while True:
                key = stdscr.getch()
                if key == ord('q'):
                    GAMEMODE = 'QUIT'
                    return 'QUIT'
                elif key == ord('r'):
                    GAMEMODE = 'RESTART'
                    return 'RESTART'
            return 'QUIT'

        
        # Check opposite direction of the prompt
        turnHistory.append([y,x])
            
            
# Main loop
# IF GAMEMODE is 'RESTART' restart the game
if __name__ == "__main__":
    while True:
        MODE = curses.wrapper(main)
        if MODE == 'QUIT':
            break
