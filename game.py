import math, random, sys, simpleguitk as simplegui
from vectorclass import Vector

WIDTH, HEIGHT = 1315, 790
CANVAS_DIMS = (WIDTH, HEIGHT)

ballpos = [CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2]
ballradius = 20 # edit to make the sprite big/small

# Player sprite image
IMG = simplegui.load_image('https://is1-ssl.mzstatic.com/image/thumb/Purple113/v4/05/8d/e8/058de8d2-7963-1c7b-8865-02d52b222aa2/OsmosOSX.png/1200x630bb.png')
IMG_CENTRE, IMG_DIMS = (300, 300), (610,610)

# Game background image
BACKGROUNDIMG = simplegui.load_image('https://images2.imgbox.com/4a/38/b798aeH2_o.jpg')

# Images for menu screen and game over screen
LOGO_IMAGE = simplegui.load_image('https://images2.imgbox.com/1d/dd/4Kj7pUOr_o.png')
GAMEOVER_IMAGE = simplegui.load_image('https://images2.imgbox.com/39/fb/U2OMmElb_o.png')
PRESSKEY_IMAGE = simplegui.load_image('https://images2.imgbox.com/4f/bc/cLxcNfmt_o.png')
LOGO_IMAGE_DIMS, PRESSKEY_IMAGE_DIMS, GAMEOVER_IMAGE_DIMS = (1007, 235), (1139, 178), (852, 135)

STEP = 0

# Global variables
radius = 100
img_dest_dim = (radius,radius) # size of sprite
img_pos = CANVAS_DIMS[0]/2, 2*CANVAS_DIMS[1]/3
img_rot = 0

newlist, balls = [], []

# player class
class Player:
    global radius
    def __init__(self, pos, radius, lives, score):
        self.pos = pos
        self.vel = Vector()
        self.radius = radius
        self.colour = 'White'
        self.lives = lives
        self.score = score

    def draw(self, canvas):
        global img_rot
        img_rot += STEP
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, self.pos.get_p(), (self.radius,self.radius), img_rot)

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)

# keyboard class
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

# interaction class
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
player = Player(Vector(CANVAS_DIMS[0]/2, CANVAS_DIMS[1]/2), 50 , 3, 0)
inter = Interaction(player, kbd)

# circle class
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

# food (enemy) class
class Food():
    def __init__(self, centerpoint, radius1, linewidth, linecolor, fillcolor, vel):
        Circle.__init__(self, centerpoint, radius1, linewidth, linecolor, fillcolor, vel)
        self.is_visible = True
        
    def draw(self, canvas):
        if self.is_visible:
            Circle.draw(self, canvas)

    def update(self):
        global ballradius

        if self.is_visible and distance(newlist, self.centerpoint) <= player.radius*0.5 + self.radius1: #checks if the main sprite has touched the center point of the smaller balls
            if player.radius*0.5 >= self.radius1:
                self.is_visible = False
                player.radius = math.sqrt(player.radius**2 + self.radius1**2)
                player.score += int(player.radius) - 50
                balls.remove(self) #so radius1 is the radius of the
                enemyspawn()
            else:
                player.radius = 0.001
                player.pos.x = CANVAS_DIMS[0]/2
                player.pos.y = CANVAS_DIMS[1]/2
                player.radius = 50
                player.lives -=1

# powerup class
class PowerUp():
    def __init__(self, centerpoint, radius1, linewidth, linecolor, fillcolor, vel):
        Circle.__init__(self, centerpoint, radius1, linewidth, linecolor, fillcolor, vel)
        self.is_visible = True

    def powers(self):
        p = random.randint(1,3)
        if p == 1:
            player.lives += 1
        elif p == 2:
            player.vel.multiply(1.1)
        else:
            player.radius *= 1.2

    def draw(self, canvas):
        if self.is_visible:
            Circle.draw(self, canvas)

    def update(self):
        global ballradius

        if self.is_visible and distance(newlist, self.centerpoint) <= player.radius*0.5 + self.radius1: #checks if the main sprite has touched the center point of the smaller balls
            if player.radius*0.5 >= self.radius1:
                self.is_visible = False
                self.powers()
                
                balls.remove(self) #so radius1 is the radius of the
                
            else:
                player.radius = 0.001
                player.pos.x = CANVAS_DIMS[0]/2
                player.pos.y = CANVAS_DIMS[1]/2
                player.radius = 50
                player.lives -=1

def distance(a, b): #finds radius and increases it y the size of the
    return math.sqrt( (a[1] - b[1]) ** 2 + (a[0] - b[0]) ** 2)

# mouse handler
def mousehandler(pos):#this allows the mouse to drag
    global ballpos, ballcolour
    ballpos= list(pos)
    ballcolour = "Blue"
    print (ballpos)

# enemy spawn function
def enemyspawn(): #make this bigger to increase food
        radius1 = random.randint(1,50) # radius of the blob circles
        x = random.randint(radius1, WIDTH-radius1) #finding position of each circle
        y = random.randint(100, HEIGHT-radius1)
        if x > ((WIDTH/2)+55) or x < ((WIDTH/2)-55):
            if y > ((HEIGHT/2)+55) or y < ((HEIGHT/2)-55):
                balls.append(Food((x, y), radius1, 5, 'grey', 'red',Vector(-1,-1)))

# power up spawn function
def powerupspawn():
    radius1 = random.randint(1,50)
    x = random.randint(radius1, WIDTH-radius1) #finding position of each circle
    y = random.randint(100, HEIGHT-radius1)
    balls.append(PowerUp((x, y), 20, 5, 'green', 'green',Vector(-1,-1)))

# ui function
def ui(canvas):
    canvas.draw_text(("Score:", player.score), [1200, 40], 20, "white")
    canvas.draw_text("Lives:", [10, 40], 20, "white")

    for i in range(0,player.lives):
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, (20*i*2+90,30), (40,40), img_rot)

# main menu function
def mainMenu(canvas):
    
    canvas.draw_image(BACKGROUNDIMG, (10, 10), (2650,1600), [10, 10], (2650,1600))
    canvas.draw_image(LOGO_IMAGE, (503, 117), LOGO_IMAGE_DIMS, (650, 300), (1007, 235), 0)
    canvas.draw_image(PRESSKEY_IMAGE, (570, 89), PRESSKEY_IMAGE_DIMS, (650, 450), (1139, 178), 0)

    if kbd.one:
        frame.set_draw_handler(draw)

    if kbd.two:
        sys.exit()

# game over function
def gameOver(canvas):
    canvas.draw_image(BACKGROUNDIMG, (10, 10), (2650,1600), [10, 10], (2650,1600))
    canvas.draw_image(GAMEOVER_IMAGE, (426, 67), GAMEOVER_IMAGE_DIMS, (650, 250), (852, 135), 0)
    canvas.draw_image(PRESSKEY_IMAGE, (570, 89), PRESSKEY_IMAGE_DIMS, (650, 450), (1139, 178), 0)

    if kbd.one:
        balls.clear()
        for i in range(50):
            enemyspawn()
        for j in range(10):
            powerupspawn()
        player.score = 0
        player.lives = 3
        draw(canvas)

    if kbd.two: 
        sys.exit()

# draw handler
def draw(canvas): 
    newlist.clear()

    canvas.draw_image(BACKGROUNDIMG, (10, 10), (2650,1600), [10, 10], (2650,1600))
    
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
for j in range(10):
    powerupspawn()

player.score = 0

frame = simplegui.create_frame('CS1821 Osmos', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('Black')
frame.set_mousedrag_handler(mousehandler)
frame.set_draw_handler(mainMenu)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()