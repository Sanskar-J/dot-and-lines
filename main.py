"""
Dots and Boxes - Mobile Edition (Kivy)
A two-player game on a grid where players draw lines and complete boxes
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.image import Image
from kivy.graphics import Line, Color, Ellipse, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
import math

Window.size = (800, 900)

class DotsAndBoxesGame(Widget):
    def __init__(self, grid_size=5, **kwargs):
        super().__init__(**kwargs)
        self.grid_size = grid_size
        self.cell_size = 60
        self.edge_threshold = 15
        
        self.current_player = 1
        self.edges_drawn = set()
        self.boxes_drawn = set()
        self.player1_score = 0
        self.player2_score = 0
        
        # Colors
        self.player1_color = (0.118, 0.565, 1.0, 1.0)  # Blue
        self.player2_color = (1.0, 0.271, 0.0, 1.0)    # Red
        self.player1_fill = (0.706, 0.769, 0.871, 0.5) # Light blue
        self.player2_fill = (1.0, 0.714, 0.757, 0.5)   # Light red
        self.dot_color = (0.173, 0.243, 0.314, 1.0)    # Dark gray
        
        self.start_x = 50
        self.start_y = self.height - 100
        
        self.bind(size=self.on_size)
        self.draw_game()
    
    def on_size(self, instance, value):
        self.draw_game()
    
    def draw_game(self):
        self.canvas.clear()
        
        with self.canvas:
            # Draw dots
            Color(*self.dot_color)
            for x in range(self.grid_size):
                for y in range(self.grid_size):
                    point_x = self.start_x + x * self.cell_size
                    point_y = self.start_y - y * self.cell_size
                    Ellipse(pos=(point_x - 4, point_y - 4), size=(8, 8))
            
            # Draw edges
            for edge in self.edges_drawn:
                p1, p2 = edge
                x1, y1 = p1
                x2, y2 = p2
                
                px1 = self.start_x + x1 * self.cell_size
                py1 = self.start_y - y1 * self.cell_size
                px2 = self.start_x + x2 * self.cell_size
                py2 = self.start_y - y2 * self.cell_size
                
                # Determine player color
                color = self.player1_color if self.get_edge_player(edge) == 1 else self.player2_color
                Color(*color)
                Line(points=[px1, py1, px2, py2], width=3)
            
            # Draw boxes
            for bx, by in self.boxes_drawn:
                box_player = self.get_box_player((bx, by))
                color = self.player1_fill if box_player == 1 else self.player2_fill
                Color(*color)
                
                x = self.start_x + bx * self.cell_size
                y = self.start_y - by * self.cell_size
                Rectangle(pos=(x + 4, y - self.cell_size + 4), size=(self.cell_size - 8, self.cell_size - 8))
    
    def get_edge_player(self, edge):
        """Return which player drew this edge (1 or 2)"""
        # This is simplified - you'd need to track player info separately
        return 1
    
    def get_box_player(self, box):
        """Return which player completed this box"""
        return 1
    
    def on_touch_down(self, touch):
        edge, p1, p2 = self.is_on_edge(touch.x, touch.y)
        if edge is not None:
            self.edges_drawn.add(edge)
            
            formed_boxes = self.get_formed_boxes(edge)
            if formed_boxes:
                for bx, by in formed_boxes:
                    if (bx, by) not in self.boxes_drawn:
                        self.boxes_drawn.add((bx, by))
                        if self.current_player == 1:
                            self.player1_score += 1
                        else:
                            self.player2_score += 1
            else:
                self.current_player = 2 if self.current_player == 1 else 1
            
            self.draw_game()
            return True
        return super().on_touch_down(touch)
    
    def is_on_edge(self, screen_x, screen_y):
        """Check if touch is on a valid edge"""
        best_dist = self.edge_threshold
        best_edge = None
        best_positions = (None, None)
        
        # Check horizontal edges
        for y in range(self.grid_size):
            p_y = self.start_y - y * self.cell_size
            if abs(screen_y - p_y) > self.edge_threshold:
                continue
            
            for x in range(self.grid_size - 1):
                p1_x = self.start_x + x * self.cell_size
                p2_x = self.start_x + (x + 1) * self.cell_size
                
                edge = tuple(sorted([(x, y), (x + 1, y)]))
                if edge in self.edges_drawn:
                    continue
                
                if p1_x - self.edge_threshold <= screen_x <= p2_x + self.edge_threshold:
                    dist = abs(screen_y - p_y)
                    if screen_x < p1_x:
                        dist = math.hypot(screen_x - p1_x, screen_y - p_y)
                    elif screen_x > p2_x:
                        dist = math.hypot(screen_x - p2_x, screen_y - p_y)
                    
                    if dist < best_dist:
                        best_dist = dist
                        best_edge = edge
                        best_positions = ((p1_x, p_y), (p2_x, p_y))
        
        # Check vertical edges
        for y in range(self.grid_size - 1):
            for x in range(self.grid_size):
                p_x = self.start_x + x * self.cell_size
                p1_y = self.start_y - y * self.cell_size
                p2_y = self.start_y - (y + 1) * self.cell_size
                
                edge = tuple(sorted([(x, y), (x, y + 1)]))
                if edge in self.edges_drawn:
                    continue
                
                if abs(screen_x - p_x) > self.edge_threshold:
                    continue
                
                if p2_y - self.edge_threshold <= screen_y <= p1_y + self.edge_threshold:
                    dist = abs(screen_x - p_x)
                    if screen_y < p2_y:
                        dist = math.hypot(screen_x - p_x, screen_y - p2_y)
                    elif screen_y > p1_y:
                        dist = math.hypot(screen_x - p_x, screen_y - p1_y)
                    
                    if dist < best_dist:
                        best_dist = dist
                        best_edge = edge
                        best_positions = ((p_x, p1_y), (p_x, p2_y))
        
        if best_edge:
            return best_edge, best_positions[0], best_positions[1]
        return None, None, None
    
    def check_box(self, bx, by):
        """Check if all four edges of a box are drawn"""
        edges = [
            tuple(sorted([(bx, by), (bx + 1, by)])),
            tuple(sorted([(bx, by + 1), (bx + 1, by + 1)])),
            tuple(sorted([(bx, by), (bx, by + 1)])),
            tuple(sorted([(bx + 1, by), (bx + 1, by + 1)]))
        ]
        return all(e in self.edges_drawn for e in edges)
    
    def get_formed_boxes(self, edge):
        """Return boxes formed by the new edge"""
        p1, p2 = edge
        x1, y1 = p1
        x2, y2 = p2
        
        formed = []
        if y1 == y2:  # Horizontal edge
            bx = min(x1, x2)
            if y1 > 0 and self.check_box(bx, y1 - 1):
                formed.append((bx, y1 - 1))
            if y1 < self.grid_size - 1 and self.check_box(bx, y1):
                formed.append((bx, y1))
        elif x1 == x2:  # Vertical edge
            by = min(y1, y2)
            if x1 > 0 and self.check_box(x1 - 1, by):
                formed.append((x1 - 1, by))
            if x1 < self.grid_size - 1 and self.check_box(x1, by):
                formed.append((x1, by))
        return formed


class DotsAndBoxesApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        title = Label(text='Dots and Boxes', size_hint_y=0.1, font_size='28sp', bold=True)
        main_layout.add_widget(title)
        
        # Game area
        game = DotsAndBoxesGame(grid_size=5, size_hint_y=0.8)
        main_layout.add_widget(game)
        
        # Info
        info = Label(text=f'Player 1 (Blue) vs Player 2 (Red)\nPlayer 1\'s Turn | Score: 0 - 0', 
                    size_hint_y=0.1, font_size='16sp')
        main_layout.add_widget(info)
        
        return main_layout


if __name__ == '__main__':
    DotsAndBoxesApp().run()
