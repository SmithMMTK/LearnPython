# 
# Create canvas and move a prompt around
# Detect collision with the edge of the screen
# Playable area is max_x-1 and max_y-2
# Add innertia to the prompt
# Add Tail to the prompt every TURN_TIME
# Slide the tail of the prompt
# Revise code structure and display format
# Add comment to the code
# Add color to the prompt and tail
# Add GAME LEVEL
# Add fruit to the game
# Add multiple fruits to the game

import curses
import random
import datetime
import time



######################
## Define function  ##
######################

# Check if the prompt is at the edge of the screen
def promptIsOutbound(x, y, max_x, max_y):

    # Check if the prompt is at the edge of the screen
    # Playable area is max_x-1 and max_y-2 because the last line is used to display information
    if (x < 0 or x > max_x-1 or y < 0 or y > max_y-2):
        # Prompt is out of bound
        return True
    else:
        # Prompt is not out of bound
        return False

# Display coordinates of the prompt
def displayCoordinates(stdscr, x, y, max_x, max_y,turn,length, gameMode):
    # Display the coordinates of the prompt with colors
    stringToDisplay = f"({x}, {y}), turn {turn}, tail length {length}, {gameMode} :"
    stdscr.addstr(max_y-1, 0, stringToDisplay, curses.color_pair(2))

    # From the last line after stringToDisplay fille the space in the same line with ▓ 
    for i in range(len(stringToDisplay), max_x-1):
        stdscr.addstr(max_y-1, i, "▓", curses.color_pair(2))


# Display Game Title and instruction
def displayGameTitle(stdscr, max_x, max_y):

    # Display the title of the game at middle of screen
    stringToDisplay = "Snake Game"
    x = int((max_x-len(stringToDisplay))/2)
    y = int(max_y/2)
    stdscr.addstr(y, x, stringToDisplay, curses.color_pair(1))

    # Display the instruction to the user
    stringToDisplay = "Move me with arrow keys or press 'q' to quit"
    x = int((max_x-len(stringToDisplay))/2)
    y = int(max_y/2)+1
    stdscr.addstr(y, x, stringToDisplay, curses.color_pair(3))

    # Ask user to select level EASY, MEDIUM, HARD
    stringToDisplay = "Select level: EASY (e), MEDIUM (m), HARD (h)"
    x = int((max_x-len(stringToDisplay))/2)
    y = int(max_y/2)+2
    stdscr.addstr(y, x, stringToDisplay, curses.color_pair(3))


    

# Display the prompt and tail after each turn
def paintPrompt(stdscr, x, y, promptLength,turnTime,turnHistory, fruitPosition):
    
    # Check length of the promptTail if it is longer than 1 do the following
    if (promptLength) > 1:
        # Print the first element of the promptTail list
        stdscr.addstr(y, x, "█") 
        # Loop through the promptTail list
        for i in range(1,promptLength):
            # the next position of the promptTail is the turnTime-i element of the turnHistory list
            # Why turnTime-i ? Because the tail will follow the prompt and next move of tail will follow the previous move of the prompt, in this case the turnTime-i element of the turnHistory list
            # Get the y,x of the element turrnHistory[turnTime-i]
            y1 = turnHistory[turnTime-i][0]
            x1 = turnHistory[turnTime-i][1]
            # Display the prompt
            stdscr.addstr(y1, x1, "░")
            
            # Check if y,x of the element is the same as the current position of the prompt
            # If yes, the prompt hit the tail of the prompt
            if y1 == y and x1 == x:
                return False
    else:
        # promptTail is only 1 element (head of the prompt)
        # Display the prompt
        stdscr.addstr(y, x, "█")
    
    # Display the fruit
    if fruitPosition != []:
        for i in range(len(fruitPosition)):
            stdscr.addstr(fruitPosition[i][0], fruitPosition[i][1], "*", curses.color_pair(2))
            #stdscr.addstr(fruitPosition[0], fruitPosition[1], "*", curses.color_pair(2))
    
    # Prompt is not out of bound, and the prompt is not hit the tail of the prompt, display the prompt
    # Refresh the screen to display changes
    stdscr.refresh()
    return True

##########################
## End Define function  ##
##########################

#
# Main function
#
def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    # Get the screen dimensions
    max_y, max_x = stdscr.getmaxyx()
   

    # Refresh the screen to see the window
    stdscr.refresh()

    # Enable color mode
    curses.start_color()

    # Define color pairs
    # 1: Red text on black background
    # 2: Green text on black background
    # 3: Yellow text on black background
    # 4: Blue text on black background
    # 5: Black text on white background
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Initial position of the prompt by start a 2/3 on left side of the screen
    x, y = int(curses.COLS/3), int(curses.LINES/2)

    # Turn counter (every TURN_TIME) and start by -1 to add the first element of the promptTail list
    turn = -1

    # Initial length of the prompt
    promptLength = 1

    # Initial move direction of the prompt
    moveDirection = "RIGHT"

    # Turn history
    turnHistory = []
    turnHistory.append([x,y])
    turnTime = -1

    

    # First time flag
    # Because the first time the program run, it will display the prompt and instructions to the user
    firstTime = True
    


    # THINGTIME : Time in milliseconds to wait for user input otherwise move the prompt to the current direction
    THINGTIME = 150

    # TURN_TIME : Number of turns to add a new element to the tail
    TUNRN_TIME = 5

    # Game mode
    GAMEMODE = ""

    # How many turn to add a new fruit
    FRUITTURN = random.randint(20,50)
    turnFruit = -1
    fruitPosition = []

    
    while True:
        
        # Turn counter, add 1 every turn and turnTime
        # turn use for add a new element to the promptTail list every TURN_TIME
        # turnTime use for move the tail of the prompt
        turn += 1
        turnTime += 1
        turnFruit += 1

        # Defined the start time of this turn
        startTime = datetime.datetime.now()

        # Add a new fruit to the game every FRUITTURN
        #if (turnFruit == FRUITTURN) and (not fruiteMode):
        if (turnFruit == FRUITTURN):
            # Random position of the fruit in the game within the playable area
            # Randeom no. of turn to add a new fruit
            FRUITTURN = random.randint(20,50)
            while True:
                # Random position of the fruit in the game within the playable area
                fruitPosition.append([random.randint(0,max_y-2),random.randint(0,max_x-1)])
                # Check if the fruit is not on the current position of the prompt
                if fruitPosition != [y,x]:
                    break
            turnFruit = -1
                

        # Add a new tail to the prompt every TURN_TIME
        if turn == TUNRN_TIME:
            # Add 1 to the length of the prompt
            promptLength += 1
            turn = -1

        # Display the prompt and instructions to the user
        # Display Welcome screen
        if firstTime:
            # Display the prompt for movement
            displayGameTitle(stdscr, max_x, max_y)
            #Pause the program until user input
            key = stdscr.getch()
        

            # Get user input to select level or quit the game
            while key != ord('q') and key != ord('e') and key != ord('m') and key != ord('h'):
                key = stdscr.getch()
        
            if key == ord('q'):                
                return 'QUIT'
                break
            elif key == ord('e'):
                THINGTIME = 210
                TUNRN_TIME = 10
                GAMEMODE = "Easy"
            elif key == ord('m'):
                THINGTIME = 140
                TUNRN_TIME = 5
                GAMEMODE = "Medium"
            elif key == ord('h'):
                THINGTIME = 70
                TUNRN_TIME = 3
                GAMEMODE = "Hard"
            
            # End firs time process
            firstTime = False
        else:
            stdscr.clear()
            # Display the coordinates of the prompt
            displayCoordinates(stdscr, x, y,max_x,max_y,turn, promptLength, GAMEMODE) 
        
        
        ## Display the prompt ##

        ## if paintPrompt returns False, break the loop
        if not (paintPrompt(stdscr, x, y, promptLength,turnTime,turnHistory,fruitPosition)):
            #stdscr.clear()
            stdscr.timeout(-1) 
            stdscr.addstr(max_y-1, 0, "You hit the tail of the snake ! (Press 'r' to restart or 'q' to quit)...")
            #stdscr.refresh()
            while True:
                key = stdscr.getch()
                if key == ord('q'):
                    return 'QUIT'
                    break
                elif key == ord('r'):
                    return 'RESTART'
            break

        # Check if the prompt hit the fruitPosition
        for i in range(len(fruitPosition)):
            if (y == fruitPosition[i][0]) and (x == fruitPosition[i][1]):
                turnFruit = -1
                promptLength += 1
                turn = -1
                fruitPosition.pop(i)
                break


        # Move the prompt according to the velocity of the prompt (moveDirection) if no input is given in 1 second
        # If the prompt is move beyond the edge of the screen, stop the prompt and display a message

        # Get user input
        # Get user input with a 0-millisecond timeout (non-blocking)
        # Use following line for debugging
        # stdscr.timeout(-1)
        stdscr.timeout(THINGTIME)
        key = stdscr.getch()
        
        # Check opposite direction of the prompt
        # If the prompt is moving to the right, the prompt cannot move to the left
        # If the prompt is moving to the left, the prompt cannot move to the right
        # If the prompt is moving to the up, the prompt cannot move to the down
        # If the prompt is moving to the down, the prompt cannot move to the up
        # then ignore the user input
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
        # If no key input, move the prompt according to the velocity of the prompt (moveDirection)
        # Detect no key input from value of key = -1
        # Key must not be -1 and oppositeDirection must be False (the prompt is not moving to the opposite direction)
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
                return 'QUIT'
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
            
            # get current time of the turn
            currentTime = datetime.datetime.now()

            # Calculate the time elapsed since the start of the turn
            timeElapsed = (currentTime - startTime).total_seconds() * 1000
            
            # If timeElapsed is less than THINGTIME, wait for the remaining time
            if timeElapsed < THINGTIME:
                delayTime = THINGTIME - timeElapsed
                time.sleep(delayTime/1000)
            
        # Check if the prompt is at the edge of the screen
        if promptIsOutbound(x, y, max_x, max_y):
            #stdscr.clear()
            stdscr.timeout(-1) 
            stdscr.addstr(max_y-1, 0, "You hit the edge of the screen! (Press 'r' to restart or 'q' to quit)...")
            #stdscr.refresh()
            # While loop to wait until user press q
            while True:
                key = stdscr.getch()
                if key == ord('q'):
                    return 'QUIT'
                elif key == ord('r'):
                    return 'RESTART'
            return 'QUIT'

       
        # Keep track of the turn history to use for the tail of the prompt
        turnHistory.append([y,x])
            
            
# Main loop
# Loop program until GAMEMODE is 'QUIT'
if __name__ == "__main__":
    while True:
        MODE = curses.wrapper(main)
        if MODE == 'QUIT':
            break
