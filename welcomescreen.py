import simpleguitk as simplegui

def draw(canvas):
    canvas.draw_text("Welcome to Osmos!", [280, 300], 50, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 960, 540)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()