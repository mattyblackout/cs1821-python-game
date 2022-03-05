import simpleguitk as simplegui

def draw(canvas):
    canvas.draw_text("Welcome to CS1821 Osmos!", [150, 200], 60, "White")
    canvas.draw_text("Press any key to start a new game", [220, 400], 40, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 1024, 576)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()