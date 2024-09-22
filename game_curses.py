import curses
import time
import numpy as np

stdscr = curses.initscr()
curses.curs_set(0)
stdscr.nodelay(1)


GRID_HEIGHT = curses.LINES - 1
GRID_WIDTH = curses.COLS - 1

# Function to initialize the grid with random live (1) and dead (0) cells
def initialize_grid():
    return np.random.choice([0, 1], GRID_HEIGHT * GRID_WIDTH, p=[0.8, 0.2]).reshape(GRID_HEIGHT, GRID_WIDTH)

# Function to calculate the next state of the grid
def update(grid):
    new_grid = grid.copy()
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            # Count the number of live neighbors
            live_neighbors = np.sum(grid[max(0, i-1):min(GRID_HEIGHT, i+2), max(0, j-1):min(GRID_WIDTH, j+2)]) - grid[i, j]
            
            # Apply the rules of the Game of Life
            if grid[i, j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                
                new_grid[i, j] = 0
                
            elif grid[i, j] == 1 and (live_neighbors == 3 or live_neighbors == 2):
                
                new_grid[i, j] = 1
                
            elif grid[i, j] == 0 and live_neighbors == 3:
                
                new_grid[i, j] = 1
                
    return new_grid

# Function to draw the grid in the terminal
def draw_grid(stdscr, grid):
    stdscr.clear()
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            char = "@" if grid[i, j] == 1 else " "
            stdscr.addch(i, j, char)
    stdscr.refresh()

# Main function to run the Game of Life
def game_of_life(stdscr):
    grid = initialize_grid()

    while True:
        draw_grid(stdscr, grid)
        grid = update(grid)
        time.sleep(0.1)

        # Press 'q' to quit
        key = stdscr.getch()
        if key == ord('q'):
            break

# Run the Game of Life using curses
# curses.wrapper(game_of_life)

game_of_life(stdscr)
