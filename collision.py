from vectorclass import Vector
import simpleguitk as simplegui

WIDTH = 600
HEIGHT = 300    
    
SHEET_URL = "https://httpsimage.com/v2/ff1cf8db-5051-4242-931b-c91f32a62426.png"
SHEET_WIDTH = 955
SHEET_HEIGHT = 955
SHEET_COLUMNS = 5
SHEET_ROWS = 5


class Spritesheet:
    def __init__(self, imgurl, columns, rows, frame_duration):
        self.img = simplegui.load_image(imgurl)
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.columns = columns
        self.rows = rows
        self.frame_duration = frame_duration
        
        self.frame_width = self.width / columns
        self.frame_height = self.height / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]
        self.frame_clock = 0

    def update_index(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.rows

    def draw(self, canvas, pos):
        self.frame_clock += 1
        if self.frame_clock % self.frame_duration == 0:
            self.update_index()
    
        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )
        
        source_size = (self.frame_width, self.frame_height)
        #dest_centre = (300, 257)-This is not need as we want the sprite to take the position of the Ball so we will use "pos":
        dest_size = (90, 90)
        canvas.draw_image(self.img, source_centre, source_size, pos, dest_size)  


class Ball:
    def __init__(self, pos, radius=35, sprite=None):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 35)
        self.colour = '#00008B'
        self.sprite = sprite

    def draw(self, canvas): 
        canvas.draw_circle(self.pos.get_p(), self.radius, 1, self.colour, self.colour)
        self.sprite.draw(canvas, self.pos.get_p())
       
        
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
   

class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False


    def keyDown(self, key):
        
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        elif key == simplegui.KEY_MAP['left']:
            self.left = True


    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        elif key == simplegui.KEY_MAP['left']:
            self.left = False

            
class Interaction:
    def __init__(self,ball, keyboard):
        self.ball = ball
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.right:
            self.ball.vel.add(Vector(1, 0))
        elif self.keyboard.left:
            self.ball.vel.add(Vector(-1, 0))
            
kbd = Keyboard()

sheet = Spritesheet(
    SHEET_URL,  
    SHEET_COLUMNS, 
    SHEET_ROWS, 
    40
)

ball = Ball(Vector(WIDTH/2, HEIGHT-40), 40, sheet)
inter = Interaction(ball, kbd)

def draw(canvas):
    if ball.pos.x < 37:
        ball.pos = Vector(465 ,HEIGHT-40)
    elif ball.pos.x > 465:
        ball.pos = Vector(37, HEIGHT-40)
    inter.update()
    ball.update()
    ball.draw(canvas)

       
# Creating a frame and assigning callbacks to event handlers
frame = simplegui.create_frame("Sprite", 600, 300)
frame.set_canvas_background('#6495ED')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()


