import math, random, simpleguitk as simplegui
from vectorclass import Vector

WIDTH = 1315
HEIGHT = 790
CANVAS_DIMS = (WIDTH, HEIGHT)

ballpos = [CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2]
ballradius = 20 # edit to make the sprite big/small
ballcolour = "Blue"

IMG = simplegui.load_image('https://is1-ssl.mzstatic.com/image/thumb/Purple113/v4/05/8d/e8/058de8d2-7963-1c7b-8865-02d52b222aa2/OsmosOSX.png/1200x630bb.png')
IMG_CENTRE = (300, 300)
IMG_DIMS = (610, 610)

STEP = 0

BACKGROUNDIMG = simplegui.load_image('https://i.pinimg.com/originals/96/69/32/966932addf40da9dccfacad5d09b15da.jpg')

# Global variables
radius= 100
img_dest_dim = (radius,radius) #size of sprite
img_pos = CANVAS_DIMS[0]/2, 2*CANVAS_DIMS[1]/3
img_rot = 0

newlist = []

class Player:
    global radius
    def __init__(self, pos, radius):
        self.pos = pos
        self.vel = Vector()
        self.radius = radius
        self.colour = 'White'

    def draw(self, canvas):
        global img_rot
        img_rot += STEP
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, self.pos.get_p(), (self.radius,self.radius), img_rot)
    
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
        #self.img_dest_dim = radius
        #self.pos = ballpos
       
class Keyboard:
    
    def __init__(self):
        self.right = False
        self.left = False
        self.space = False
        self.up = False
        self.down = False

    def keyDown(self, key):
        global STEP
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        elif key == simplegui.KEY_MAP['left']:
            self.left = True
        elif key == simplegui.KEY_MAP['space']:
            self.space = True
        elif key == simplegui.KEY_MAP['up']:
            self.up = True
        elif key == simplegui.KEY_MAP['down']:
            self.down = True


    def keyUp(self, key):
        global STEP
        STEP = 0
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        elif key == simplegui.KEY_MAP['left']:
            self.left = False
        elif key == simplegui.KEY_MAP['space']:
            self.space = False
        elif key == simplegui.KEY_MAP['up']:
            self.up = False
        elif key == simplegui.KEY_MAP['down']:
            self.down = False




class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.right:
            self.wheel.vel.add(Vector(1, 0))
        if self.keyboard.left:
            self.wheel.vel.add(Vector(-1, 0))
        if self.keyboard.up:
            self.wheel.vel.add(Vector(0, -1))
        if self.keyboard.down:
            self.wheel.vel.add(Vector(0, 1))
        if self.keyboard.space:
            self.wheel.vel.multiply(1.1)
            self.wheel.radius-=0.1


        if player.pos.y >= CANVAS_DIMS[1]-25:
            player.pos.y = CANVAS_DIMS[1]-25

        if player.pos.y <= CANVAS_DIMS[1]-(CANVAS_DIMS[1]-25):
            player.pos.y = CANVAS_DIMS[1]-(CANVAS_DIMS[1]-25)

        if player.pos.x <= CANVAS_DIMS[0]-(CANVAS_DIMS[0]-25):
            player.pos.x = CANVAS_DIMS[0]-(CANVAS_DIMS[0]-25)

        if player.pos.x >= CANVAS_DIMS[0]-25:
            player.pos.x = CANVAS_DIMS[0]-25

kbd = Keyboard()
player = Player(Vector(CANVAS_DIMS[0]/2, CANVAS_DIMS[1]/2), 20)
inter = Interaction(player, kbd)
        
class Circle():
    
    def __init__(self, centerpoint, radius1, linewidth, linecolor, fillcolor):
        self.centerpoint = centerpoint
        self.radius1 = radius1
        self.linewidth = linewidth
        self.linecolor = linecolor
        self.fillcolor = fillcolor
        
    def draw(self,canvas):
        canvas.draw_circle(self.centerpoint, self.radius1, self.linewidth, self.linecolor, self.fillcolor)     

class Food():
    def __init__(self, centerpoint, radius1, linewidth, linecolor, fillcolor):
        Circle.__init__(self, centerpoint, radius1, linewidth, linecolor, fillcolor)
        self.is_visible = True
        
    def draw(self, canvas):
        if self.is_visible:
            Circle.draw(self, canvas)
            
    def update(self):
        global ballradius
        if self.is_visible and distance(newlist, self.centerpoint) <= player.radius*0.5 + self.radius1: #checks if the main sprite has touched the center point of the smaller balls 
            if player.radius*0.5 >= self.radius1:    
                self.is_visible = False
                player.radius = math.sqrt(player.radius**2 + self.radius1**2) #so radius1 is the radius of the 

def distance(a, b): #finds radius and increases it y the size of the 
    return math.sqrt( (a[1] - b[1]) ** 2 + (a[0] - b[0]) ** 2)



def mousehandler(pos):#this allows the mouse to drag
    global ballpos, ballcolour
    ballpos= list(pos)
    ballcolour = "Blue"
    print (ballpos)
    
            
            
'''def on_ground():   
    if wheel.pos.y == CANVAS_DIMS[1]-70:
        return True
    else:
        return False'''
    
    




def draw(canvas):
    newlist.clear()
    #canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, ballpos, img_dest_dim, img_rot)
    
    inter.update()
    
    newlist.append(player.pos.x)
    newlist.append(player.pos.y)
    print (newlist)
    print(player.radius)
    player.update()
    
    player.draw(canvas)
    for ball in balls:
        ball.update()
        ball.draw(canvas)



balls = []
#This generates the food
for i in range (50): #make this bigger to increase food
    radius1 = random.randint(1,50) # radius of the blob circles
    x = random.randint(radius1, WIDTH-radius1) #finding position of each circle
    y = random.randint(radius1, HEIGHT-radius1)
    balls.append(Food((x, y), radius1, 5, 'red', 'Red'))

frame = simplegui.create_frame('Interactions', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('#2C6A6A')
frame.set_mousedrag_handler(mousehandler)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
