import math, random, simpleguitk as simplegui
from vectorclass import Vector
import os, sys

WIDTH = 1315
HEIGHT = 790
CANVAS_DIMS = (WIDTH, HEIGHT)

ballpos = [CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2]
ballradius = 20 # edit to make the sprite big/small

LIVES_IMG = simplegui.load_image('https://image.shutterstock.com/image-vector/heart-pixel-icon-vector-illustration-260nw-413867536.jpg')
LIVES_CENTRE, LIVESDIMS = (100,100), (600, 600)

IMG = simplegui.load_image('https://is1-ssl.mzstatic.com/image/thumb/Purple113/v4/05/8d/e8/058de8d2-7963-1c7b-8865-02d52b222aa2/OsmosOSX.png/1200x630bb.png')
IMG_CENTRE, IMG_DIMS = (300, 300), (610,610)

BACKGROUNDIMG = simplegui.load_image('https://images2.imgbox.com/4a/38/b798aeH2_o.jpg')

LOGO_IMAGE = simplegui.load_image('https://images2.imgbox.com/1d/dd/4Kj7pUOr_o.png')
GAMEOVER_IMAGE = simplegui.load_image('https://images2.imgbox.com/39/fb/U2OMmElb_o.png')
PRESSKEY_IMAGE = simplegui.load_image('https://images2.imgbox.com/4f/bc/cLxcNfmt_o.png')
LOGO_IMAGE_DIMS, PRESSKEY_IMAGE_DIMS, GAMEOVER_IMAGE_DIMS = (1007, 235), (1139, 178), (852, 135)

STEP = 0

menuActive = True

# Global variables
radius = 100
img_dest_dim = (radius,radius) #size of sprite
img_pos = CANVAS_DIMS[0]/2, 2*CANVAS_DIMS[1]/3
img_rot = 0

newlist = []
balls = []

class Player:
    global radius
    def __init__(self, pos, radius,lives):
        self.pos = pos
        self.vel = Vector()
        self.radius = radius
        self.colour = 'White'
        self.lives = lives

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
        self.one = False
        self.two = False

    def keyDown(self, key):
        global STEP
        if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['d']:
            self.right = True
        elif key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['a']:
            self.left = True
        elif key == simplegui.KEY_MAP['space']:
            self.space = True
        elif key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['w']:
            self.up = True
        elif key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['s']:
            self.down = True
        elif key == simplegui.KEY_MAP['one'] or key == simplegui.KEY_MAP['1']:
            self.one = True
        elif key == simplegui.KEY_MAP['two'] or key == simplegui.KEY_MAP['2']:
            self.two = True


    def keyUp(self, key):
        global STEP
        STEP = 0
        if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['d']:
            self.right = False
        elif key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['a']:
            self.left = False
        elif key == simplegui.KEY_MAP['space']:
            self.space = False
        elif key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['w']:
            self.up = False
        elif key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['s']:
            self.down = False
        elif key == simplegui.KEY_MAP['one'] or key == simplegui.KEY_MAP['1']:
            self.one = False
        elif key == simplegui.KEY_MAP['two'] or key == simplegui.KEY_MAP['2']:
            self.two = False

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
player = Player(Vector(CANVAS_DIMS[0]/2, CANVAS_DIMS[1]/2), 50 , 3)
inter = Interaction(player, kbd)

class Circle:
    def __init__(self, centerpoint, radius1, linewidth, linecolor, fillcolor, vel):
        self.centerpoint = centerpoint #Vector(-1,0)
        self.radius1 = radius1
        self.linewidth = linewidth
        self.linecolor = linecolor
        self.fillcolor = fillcolor
        self.vel = vel

    def draw(self,canvas):
        canvas.draw_circle(self.centerpoint, self.radius1, self.linewidth, self.linecolor, self.fillcolor)
       
    def update(self):
        self.centerpoint.add(self.vel)
        self.vel.multiply(0.85)

class Food():
    def __init__(self, centerpoint, radius1, linewidth, linecolor, fillcolor, vel):
        Circle.__init__(self, centerpoint, radius1, linewidth, linecolor, fillcolor, vel)
        self.is_visible = True
        
    def draw(self, canvas):
        if self.is_visible:
            Circle.draw(self, canvas)
            #
    def update(self):
        global ballradius
        #if self.is_visible:
        #Circle.update(self)
        #
        #self.centerpoint.add(self.vel)
        if self.is_visible and distance(newlist, self.centerpoint) <= player.radius*0.5 + self.radius1: #checks if the main sprite has touched the center point of the smaller balls
            if player.radius*0.5 >= self.radius1:
                self.is_visible = False
                player.radius = math.sqrt(player.radius**2 + self.radius1**2)
                balls.remove(self) #so radius1 is the radius of the
                enemyspawn()
            else:
                #player.pos = (250,250)
                player.radius = 0.001
                player.pos.x = CANVAS_DIMS[0]/2
                player.pos.y = CANVAS_DIMS[1]/2
                player.radius = 50
                player.lives -=1


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

def enemyspawn(): #make this bigger to increase food
        radius1 = random.randint(1,50) # radius of the blob circles
        x = random.randint(radius1, WIDTH-radius1) #finding position of each circle
        y = random.randint(100, HEIGHT-radius1)
        if x > ((WIDTH/2)+55) or x < ((WIDTH/2)-55):
            if y > ((HEIGHT/2)+55) or y < ((HEIGHT/2)-55):
                balls.append(Food((x, y), radius1, 5, 'red', 'red',Vector(-1,-1)))

def ui(canvas):
    canvas.draw_text(("Score:", (int(player.radius) - 50)), [1200, 40], 20, "white")
    canvas.draw_text("Lives:", [10, 40], 20, "white")

    for i in range(0,player.lives):
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, (20*i*2+90,30), (40,40), img_rot)

def mainMenu(canvas):
    canvas.draw_image(BACKGROUNDIMG, (10, 10), (2650,1600), [10, 10], (2650,1600))
    canvas.draw_image(LOGO_IMAGE, (503, 117), LOGO_IMAGE_DIMS, (650, 300), (1007, 235), 0)
    canvas.draw_image(PRESSKEY_IMAGE, (570, 89), PRESSKEY_IMAGE_DIMS, (650, 450), (1139, 178), 0)

    #if kbd.one: 
        
    if kbd.two:
        sys.exit()

def gameOver(canvas):
    canvas.draw_image(BACKGROUNDIMG, (10, 10), (2650,1600), [10, 10], (2650,1600))
    canvas.draw_image(GAMEOVER_IMAGE, (426, 67), GAMEOVER_IMAGE_DIMS, (650, 250), (852, 135), 0)
    canvas.draw_image(PRESSKEY_IMAGE, (570, 89), PRESSKEY_IMAGE_DIMS, (650, 450), (1139, 178), 0)

    if kbd.one:
        os.execv(sys.executable, ['python'] + sys.argv)
    if kbd.two: 
        sys.exit()

def draw(canvas):

    newlist.clear()
    canvas.draw_image(BACKGROUNDIMG, (10, 10), (2650,1600), [10, 10], (2650,1600))
    #canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, ballpos, img_dest_dim, img_rot)
    #if player.radius < 1:
    #    player.radius = 20
    
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
        
    ui(canvas)
    print (len(balls))

    if player.lives == 0:
        gameOver(canvas)


for i in range(50):
    enemyspawn()


frame = simplegui.create_frame('CS1821 Osmos', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('Black')
frame.set_mousedrag_handler(mousehandler)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()