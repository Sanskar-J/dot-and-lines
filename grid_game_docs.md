# Dots and Boxes Game Documentation

## Overview
`grid_game.py` is a Python script that implements the classic two-player "Dots and Boxes" game using the built-in `turtle` graphics library. Players take turns drawing horizontal or vertical lines between adjacent dots on a 25x25 grid. When a player completes the fourth side of a 1x1 box, they earn a point, color the box with their designated color, and are granted an extra turn. The game ends when all boxes on the grid are claimed, and the player with the most points wins!

## Requirements
- Python 3.x
- `turtle` module (built-in standard library)
- `math` and `time` modules (built-in standard libraries)

## Constants
The game's visuals and logic rely on several predefined constants:
- `GRID_SIZE`: Number of dots per row/column (default: `25`).
- `CELL_SIZE`: Distance between adjacent dots in pixels (default: `30`).
- `EDGE_THRESHOLD`: Distance threshold (in pixels) to detect whether a mouse click is close enough to a valid edge (default: `12`).
- **Colors**:
  - `WHITE`, `BLACK`, `LIGHT_GRAY`: Theme colors.
  - `PLAYER1_COLOR`: Color for Player 1's lines (`blue`).
  - `PLAYER2_COLOR`: Color for Player 2's lines (`red`).
  - `PLAYER1_FILL`: Color to fill Player 1's completed boxes (`lightblue`).
  - `PLAYER2_FILL`: Color to fill Player 2's completed boxes (`pink`).

## Global Game State
- `current_player`: Tracks whose turn it is (`1` or `2`).
- `edges_drawn`: A `set` that stores the edges that have already been drawn to prevent duplicate moves.
- `boxes_drawn`: A `set` that stores the coordinates of all completed boxes: `(bx, by)`.
- `player1_score`, `player2_score`: Track the points (completed boxes) of each player.
- `game_over`: A boolean flag indicating if all boxes have been filled.
- `start_x`, `start_y`: The starting coordinates of the top-left corner of the grid to center it on the screen.

## Turtle Drawers
The game utilizes different Turtle objects to handle specific drawing tasks efficiently without redrawing the entire screen:
- `grid_drawer`: Draws the black dots representing the grid.
- `lines_drawer`: Draws the colored lines between dots when a player makes a move.
- `box_drawer`: Fills in the 1x1 area of a completed box with the scoring player's color.
- `info_drawer`: Renders the text indicating whose turn it is, the current score, and the final "Game Over" message.

## Core Functions

### Logic & Drawing
- **`draw_grid()`**: Plots dots at regular intervals.
- **`is_on_edge(screen_x, screen_y)`**: Determines if a given set of mouse click coordinates falls on a valid, undrawn edge between two dots.
- **`draw_line(p1, p2, color)`**: Renders a line between two points.
- **`check_box(bx, by)`**: Checks the `edges_drawn` set to see if all four edges surrounding the grid coordinate `(bx, by)` exist.
- **`get_formed_boxes(edge)`**: Checks the adjacent 1x1 squares around a newly drawn `edge` and returns a list of boxes that were just completed.
- **`fill_box(bx, by, color)`**: Uses `box_drawer` to visually fill a completed 1x1 box.

### Game State & UI
- **`update_info()`**: Updates the text at the top of the screen. Shows the current player's turn alongside the real-time score. When `game_over` is True, displays the winning player and final score.
- **`check_game_over()`**: Checks if the total number of items in `boxes_drawn` matches the total possible boxes (`(GRID_SIZE - 1) * (GRID_SIZE - 1)`). Sets `game_over` to True if they match.
- **`on_click(x, y)`**: Event handler bound to the left mouse click:
  1. Prevents interaction if the game is over.
  2. Identifies a valid edge and draws the line.
  3. Checks for newly completed boxes using `get_formed_boxes()`.
  4. For every completed box: increments the current player's score and fills the box.
  5. If one or more boxes were formed, the current player takes another turn (turn does not switch).
  6. Otherwise, play passes to the other player.
  7. Checks for game over and updates UI.

## How to Play
1. Run the script using Python: `python grid_game.py`
2. **Player 1 (Blue)** starts. Click the empty space between any two adjacent dots (horizontally or vertically) to draw a line.
3. If drawing the line completes a 1x1 box, that box fills with your color, you score a point, and you **must** take another turn.
4. If no box is completed, your turn ends, and **Player 2 (Red)** goes.
5. The game concludes when the entire grid is full of colored boxes. The player with the highest score wins!