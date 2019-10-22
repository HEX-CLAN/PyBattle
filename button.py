import pyglet
import settings

class Button:
    def __init__(self, text, x, y, w, h):
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)
        self.label = pyglet.text.Label(
            text,
            font_name='Caviar Dreams',
            font_size=24,
            x=x,
            y=y,
            anchor_x='center',
            anchor_y='center',
            color=settings.button_color
        )
        self.hover = False
        
    def draw(self):
        color = 100 if self.hover else 70
        pyglet.graphics.draw(
            4,
            pyglet.gl.GL_POLYGON,
            ('v2i', (
                self.x - self.w//2, self.y - self.h//2,
                self.x + self.w//2, self.y - self.h//2, 
                self.x + self.w//2, self.y + self.h//2,
                self.x - self.w//2, self.y + self.h//2)),
            ('c4B', settings.button_bg)
        )
        self.label.draw()

    def on_hover(self, mouse_x, mouse_y):
        if (self.x-self.w//2) < mouse_x < (self.x+self.w//2) and (self.y-self.h//2) < mouse_y < (self.y+self.h//2):
            self.hover = True
            self.label.color = settings.violet
        else:
            self.hover = False
            self.label.color = settings.cyan
            