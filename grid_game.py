import turtle
import time
import math
import os

# Constants
CELL_SIZE = 40
EDGE_THRESHOLD = 15  # Distance threshold to detect edge clicks

# Aesthetics & Colors
WHITE = "#ffffff"
BLACK = "#2c3e50"
TEXT_COLOR = "#34495e"
DOT_COLOR = "#34495e"

PLAYER1_COLOR = "#1e90ff"  # DodgerBlue
PLAYER1_FILL = "#b0c4de"   # LightSteelBlue
PLAYER2_COLOR = "#ff4500"  # OrangeRed
PLAYER2_FILL = "#ffb6c1"   # LightPink

START_BTN_COLOR = "#2ecc71" # Emerald Green
BTN_TEXT_COLOR = "#ffffff"

# Fallback background colors if images are missing
BG_SPLASH_FALLBACK = "#e0f7fa"  # LightCyan
BG_GAME_FALLBACK = "#f5f5f5"    # WhiteSmoke
BG_OVER_FALLBACK = "#fff0f5"    # LavenderBlush

# Game states
STATE_SPLASH = 0
STATE_GAME = 1
STATE_GAMEOVER = 2

# Setup window
window = turtle.Screen()
window.setup(width=800, height=800)
window.title("Dots and Boxes - Enhanced Edition")
window.tracer(0)

# Drawers
grid_drawer = turtle.Turtle()
grid_drawer.speed(0)
grid_drawer.hideturtle()

lines_drawer = turtle.Turtle()
lines_drawer.speed(0)
lines_drawer.hideturtle()

box_drawer = turtle.Turtle()
box_drawer.speed(0)
box_drawer.hideturtle()

info_drawer = turtle.Turtle()
info_drawer.speed(0)
info_drawer.hideturtle()

ui_drawer = turtle.Turtle()
ui_drawer.speed(0)
ui_drawer.hideturtle()

# Game state variables
current_state = STATE_SPLASH
GRID_SIZE = 5
current_player = 1
edges_drawn = set()
boxes_drawn = set()
player1_score = 0
player2_score = 0
start_x = 0
start_y = 0

def set_background(bg_name, fallback_color):
    """Sets the background image if found, otherwise uses fallback color.
    Note: Python's turtle natively only supports .png and .gif. 
    To use .jpg or .jpeg, ensure the Pillow library is installed.
    """
    bg_set = False
    for ext in [".png", ".gif", ".jpg", ".jpeg"]:
        if os.path.exists(bg_name + ext):
            try:
                window.bgpic(bg_name + ext)
                bg_set = True
                break
            except Exception as e:
                print(f"Could not load {bg_name}{ext}: {e}")
                pass
    
    if not bg_set:
        try:
            window.bgpic("nopic")
        except Exception:
            pass
        window.bgcolor(fallback_color)

def draw_splash():
    """Draw the splash screen with Start button"""
    global current_state
    current_state = STATE_SPLASH
    
    # Clear other drawers
    grid_drawer.clear()
    lines_drawer.clear()
    box_drawer.clear()
    info_drawer.clear()
    ui_drawer.clear()
    
    set_background("bg1", BG_SPLASH_FALLBACK)
    
    ui_drawer.penup()
    ui_drawer.goto(0, 150)
    ui_drawer.color(TEXT_COLOR)
    ui_drawer.write("Dots and Boxes", align="center", font=("Verdana", 42, "bold"))
    ui_drawer.goto(0, 80)
    ui_drawer.write("The Classic Strategy Game", align="center", font=("Verdana", 16, "normal"))
    
    # Draw Start Button
    btn_width = 200
    btn_height = 60
    ui_drawer.goto(-btn_width // 2, -20)
    ui_drawer.pendown()
    ui_drawer.fillcolor(START_BTN_COLOR)
    ui_drawer.pencolor(START_BTN_COLOR)
    ui_drawer.begin_fill()
    for _ in range(2):
        ui_drawer.forward(btn_width)
        ui_drawer.right(90)
        ui_drawer.forward(btn_height)
        ui_drawer.right(90)
    ui_drawer.end_fill()
    ui_drawer.penup()
    
    ui_drawer.goto(0, -65)
    ui_drawer.color(BTN_TEXT_COLOR)
    ui_drawer.write("START GAME", align="center", font=("Verdana", 18, "bold"))
    window.update()

def start_game(n):
    """Initializes and transitions to the game screen."""
    global current_state, GRID_SIZE, current_player, edges_drawn, boxes_drawn
    global player1_score, player2_score, start_x, start_y
    
    GRID_SIZE = int(n)
    if GRID_SIZE < 2:
        GRID_SIZE = 2 
        
    req_width = max(800, GRID_SIZE * CELL_SIZE + 150)
    req_height = max(800, GRID_SIZE * CELL_SIZE + 150)
    window.setup(width=req_width, height=req_height)
    
    current_state = STATE_GAME
    current_player = 1
    edges_drawn = set()
    boxes_drawn = set()
    player1_score = 0
    player2_score = 0
    
    start_x = -GRID_SIZE * CELL_SIZE // 2
    start_y = GRID_SIZE * CELL_SIZE // 2
    
    ui_drawer.clear()
    set_background("bg2", BG_GAME_FALLBACK)
    
    draw_grid()
    update_info()
    window.update()

def show_game_over():
    """Transitions to the game over screen."""
    global current_state
    current_state = STATE_GAMEOVER
    
    # Clear game components
    grid_drawer.clear()
    lines_drawer.clear()
    box_drawer.clear()
    info_drawer.clear()
    
    set_background("bg3", BG_OVER_FALLBACK)
    
    ui_drawer.clear()
    ui_drawer.penup()
    ui_drawer.goto(0, 150)
    
    if player1_score > player2_score:
        msg = "Player 1 Wins!"
        color = PLAYER1_COLOR
    elif player2_score > player1_score:
        msg = "Player 2 Wins!"
        color = PLAYER2_COLOR
    else:
        msg = "It's a Tie!"
        color = TEXT_COLOR
        
    ui_drawer.color(color)
    ui_drawer.write(msg, align="center", font=("Verdana", 48, "bold"))
    
    ui_drawer.goto(0, 50)
    ui_drawer.color(TEXT_COLOR)
    score_txt = f"Final Score\nPlayer 1: {player1_score}   |   Player 2: {player2_score}"
    ui_drawer.write(score_txt, align="center", font=("Verdana", 20, "normal"))
    
    # Restart Button
    ui_drawer.goto(0, -100)
    ui_drawer.color(START_BTN_COLOR)
    ui_drawer.write("Click anywhere to return to Main Menu", align="center", font=("Verdana", 16, "italic"))
    window.update()

def draw_grid():
    """Draw the grid points"""
    grid_drawer.clear()
    grid_drawer.penup()
    grid_drawer.pencolor(DOT_COLOR)
    
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            point_x = start_x + x * CELL_SIZE + CELL_SIZE // 2
            point_y = start_y - y * CELL_SIZE - CELL_SIZE // 2
            grid_drawer.goto(point_x, point_y)
            grid_drawer.dot(8)

def is_on_edge(screen_x, screen_y):
    """Check if click is on a valid edge between two points"""
    best_edge = None
    best_positions = (None, None)
    best_dist = EDGE_THRESHOLD

    # Check horizontal edges
    for y in range(GRID_SIZE):
        p_y = start_y - y * CELL_SIZE - CELL_SIZE // 2
        if abs(screen_y - p_y) > EDGE_THRESHOLD:
            continue

        for x in range(GRID_SIZE - 1):
            p1_x = start_x + x * CELL_SIZE + CELL_SIZE // 2
            p2_x = start_x + (x + 1) * CELL_SIZE + CELL_SIZE // 2
            
            if p1_x - EDGE_THRESHOLD <= screen_x <= p2_x + EDGE_THRESHOLD:
                horizontal_dist = abs(screen_y - p_y)
                if screen_x < p1_x:
                    horizontal_dist = math.hypot(screen_x - p1_x, screen_y - p_y)
                elif screen_x > p2_x:
                    horizontal_dist = math.hypot(screen_x - p2_x, screen_y - p_y)

                if horizontal_dist < best_dist:
                    edge = tuple(sorted([(x, y), (x + 1, y)]))
                    if edge not in edges_drawn:
                        best_dist = horizontal_dist
                        best_edge = edge
                        best_positions = ((p1_x, p_y), (p2_x, p_y))

    # Check vertical edges
    for y in range(GRID_SIZE - 1):
        for x in range(GRID_SIZE):
            p_x = start_x + x * CELL_SIZE + CELL_SIZE // 2
            p1_y = start_y - y * CELL_SIZE - CELL_SIZE // 2
            p2_y = start_y - (y + 1) * CELL_SIZE - CELL_SIZE // 2
            
            if abs(screen_x - p_x) > EDGE_THRESHOLD:
                continue

            if p2_y - EDGE_THRESHOLD <= screen_y <= p1_y + EDGE_THRESHOLD:
                vertical_dist = abs(screen_x - p_x)
                if screen_y < p2_y:
                    vertical_dist = math.hypot(screen_x - p_x, screen_y - p2_y)
                elif screen_y > p1_y:
                    vertical_dist = math.hypot(screen_x - p_x, screen_y - p1_y)

                if vertical_dist < best_dist:
                    edge = tuple(sorted([(x, y), (x, y + 1)]))
                    if edge not in edges_drawn:
                        best_dist = vertical_dist
                        best_edge = edge
                        best_positions = ((p_x, p1_y), (p_x, p2_y))

    if best_edge is not None:
        return best_edge, best_positions[0], best_positions[1]
    return None, None, None

def draw_line(p1, p2, color):
    """Draw a line between two points"""
    lines_drawer.penup()
    lines_drawer.goto(p1)
    lines_drawer.pendown()
    lines_drawer.pencolor(color)
    lines_drawer.pensize(5)
    lines_drawer.goto(p2)
    lines_drawer.penup()

def check_box(bx, by):
    """Check if all four edges of a box are drawn"""
    return (tuple(sorted([(bx, by), (bx + 1, by)])) in edges_drawn and
            tuple(sorted([(bx, by + 1), (bx + 1, by + 1)])) in edges_drawn and
            tuple(sorted([(bx, by), (bx, by + 1)])) in edges_drawn and
            tuple(sorted([(bx + 1, by), (bx + 1, by + 1)])) in edges_drawn)

def get_formed_boxes(edge):
    """Return a list of boxes formed by the newly drawn edge"""
    p1, p2 = edge
    x1, y1 = p1
    x2, y2 = p2
    
    formed_boxes = []
    if y1 == y2:  # Horizontal edge
        bx = min(x1, x2)
        if y1 > 0 and check_box(bx, y1 - 1):
            formed_boxes.append((bx, y1 - 1))
        if y1 < GRID_SIZE - 1 and check_box(bx, y1):
            formed_boxes.append((bx, y1))
    elif x1 == x2:  # Vertical edge
        by = min(y1, y2)
        if x1 > 0 and check_box(x1 - 1, by):
            formed_boxes.append((x1 - 1, by))
        if x1 < GRID_SIZE - 1 and check_box(x1, by):
            formed_boxes.append((x1, by))
    return formed_boxes

def fill_box(bx, by, color):
    """Fill a completed box with the player's color"""
    top_left_x = start_x + bx * CELL_SIZE + CELL_SIZE // 2
    top_left_y = start_y - by * CELL_SIZE - CELL_SIZE // 2
    
    margin = 4
    box_drawer.penup()
    box_drawer.goto(top_left_x + margin, top_left_y - margin)
    box_drawer.pendown()
    box_drawer.color(color, color)
    box_drawer.begin_fill()
    box_drawer.goto(top_left_x + CELL_SIZE - margin, top_left_y - margin)
    box_drawer.goto(top_left_x + CELL_SIZE - margin, top_left_y - CELL_SIZE + margin)
    box_drawer.goto(top_left_x + margin, top_left_y - CELL_SIZE + margin)
    box_drawer.goto(top_left_x + margin, top_left_y - margin)
    box_drawer.end_fill()
    box_drawer.penup()

def update_info():
    """Update player info text during game"""
    info_drawer.clear()
    info_drawer.penup()
    
    y_pos = GRID_SIZE * CELL_SIZE // 2 + 30
    info_drawer.goto(0, y_pos)
    
    color = PLAYER1_COLOR if current_player == 1 else PLAYER2_COLOR
    info_drawer.color(color)
    
    turn_txt = f"Player {current_player}'s Turn"
    score_txt = f"P1 (Blue): {player1_score}   |   P2 (Red): {player2_score}"
    
    info_drawer.write(f"{turn_txt}\n{score_txt}", align="center", font=("Verdana", 14, "bold"))

def check_game_over():
    total_boxes = (GRID_SIZE - 1) * (GRID_SIZE - 1)
    if len(boxes_drawn) >= total_boxes:
        show_game_over()
        return True
    return False

def on_click(x, y):
    """Handle mouse click based on the current state"""
    global current_player, player1_score, player2_score
    
    if current_state == STATE_SPLASH:
        # Check if Start button is clicked
        btn_width = 200
        btn_height = 60
        if -btn_width//2 <= x <= btn_width//2 and -80 <= y <= -20:
            user_input = window.numinput("Grid Size", "Enter the grid size (n x n):", minval=2, maxval=50, default=5)
            if user_input is not None:
                start_game(int(user_input))
        return

    elif current_state == STATE_GAMEOVER:
        # Click anywhere to restart to splash screen
        draw_splash()
        return

    elif current_state == STATE_GAME:
        edge, p1, p2 = is_on_edge(x, y)
        if edge is not None:
            edges_drawn.add(edge)
            color = PLAYER1_COLOR if current_player == 1 else PLAYER2_COLOR
            draw_line(p1, p2, color)
            
            formed_boxes = get_formed_boxes(edge)
            if formed_boxes:
                fill_color = PLAYER1_FILL if current_player == 1 else PLAYER2_FILL
                for bx, by in formed_boxes:
                    if (bx, by) not in boxes_drawn:
                        boxes_drawn.add((bx, by))
                        fill_box(bx, by, fill_color)
                        if current_player == 1:
                            player1_score += 1
                        else:
                            player2_score += 1
                # Player gets another turn, do NOT switch
            else:
                # Switch player
                current_player = 2 if current_player == 1 else 1
                
            if not check_game_over():
                update_info()
                
            window.update()

# Initial state
draw_splash()

# Setup mouse click handling
window.listen()
window.onclick(on_click)

window.update()
window.mainloop()
