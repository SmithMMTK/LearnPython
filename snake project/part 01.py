# 
# Create canvas and move a prompt around
# 

import curses
import random

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

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
        
        # Display the prompt at the current position
        stdscr.addstr(y, x, "█")
        
        # Refresh the screen to display changes
        stdscr.refresh()
        
        # Get user input
        key = stdscr.getch()

        # Handle user input
        if key == ord('q'):
            break
        elif key == curses.KEY_RIGHT and x < max_x - 1:
            x += 1
        elif key == curses.KEY_LEFT and x > 0:
            x -= 1
        elif key == curses.KEY_DOWN and y < max_y - 1:
            y += 1
        elif key == curses.KEY_UP and y > 0:
            y -= 1

if __name__ == "__main__":
    curses.wrapper(main)
