# Conway's Game of Life


## Overview

Conway's Game of Life is a cellular automaton devised by mathematician John Conway. It is a zero-player game, meaning that its progression is determined by its initial state, with no further input from humans. The game consists of a grid of cells that evolve through iterations based on simple rules:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Implementations

The repository contains the following implementations:

1. **Python with curses**  
   - **File:** `game_curses.py`  
   - **Description:** A terminal-based implementation using the `curses` library for drawing and updating the grid.

2. **Python with matplotlib and numpy**  
   - **File:** `game_matplotlib.py`  
   - **Description:** A graphical implementation using `matplotlib` for visualization and `numpy` for efficient numerical operations.

3. **HTML and JavaScript**  
   - **File:** `index.html`  
   - **Description:** A web-based implementation using HTML and JavaScript to render the game in a web browser.

---
<img src="https://github.com/Ali-Kazzazi/game_of_life/blob/master/curses.PNG"></a>
<img src="https://github.com/Ali-Kazzazi/game_of_life/blob/master/matplot.PNG"></a>
