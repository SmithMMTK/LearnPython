# 
# Create canvas and move a prompt around
# Detect collision with the edge of the screen
# Playable area is max_x-1 and max_y-2
# 

import curses




# Check if the prompt is at the edge of the screen
# Playable area is max_x-1 and max_y-2
def promptIsOutbound(x, y, max_x, max_y):
    if (x < 0 or x > max_x-1 or y < 0 or y > max_y-2):
        return True
    else:
        return False

# Display coordinates of the prompt
def displayCoordinates(stdscr, x, y, max_x, max_y):
    # Display the coordinates of the prompt with colors
    stdscr.addstr(max_y-1, 0, f"({x}, {y})", curses.color_pair(1))

  
    ## Show another information
    #
    #
    #


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


    firstTime = True
        

    while True:

      
        
        # Get the screen dimensions
        max_y, max_x = stdscr.getmaxyx()
        


        # Display the prompt and instructions to the user
        if firstTime:
            # Display the prompt for movement
            stdscr.addstr(max_y-1, 0, "Move me with arrow keys (Press 'q' to quit)")
            firstTime = False
        else:
            stdscr.clear()
            # Display the coordinates of the prompt
            displayCoordinates(stdscr, x, y,max_x,max_y) 
        
        

        # Display the prompt at the current position
        stdscr.addstr(y, x, "█")
        

        # Refresh the screen to display changes
        stdscr.refresh()
        
        ## End of display ## 

        # Get user input
        key = stdscr.getch()

        # Handle user input
        # No need to check if the prompt is at the edge of the screen because we will do that later
        if key == ord('q'):
            break
        elif key == curses.KEY_RIGHT:
            x += 1
        elif key == curses.KEY_LEFT:
            x -= 1
        elif key == curses.KEY_DOWN:
            y += 1
        elif key == curses.KEY_UP:
            y -= 1
        
        # Check if the prompt is at the edge of the screen
        if promptIsOutbound(x, y, max_x, max_y):
            stdscr.clear()
            stdscr.addstr(max_y-1, 0, "You hit the edge of the screen! Press any key to continue...")
            stdscr.refresh()
            # Wait for your input to continue
            stdscr.getch()
            break
           
            

if __name__ == "__main__":
    curses.wrapper(main)
