import simpleguitk as simplegui

def draw(canvas):
    canvas.draw_text("Welcome to CS1821 Osmos!", [320, 200], 60, "White")
    canvas.draw_text("Press 1 to start a new game", [320, 400], 40, "Red")
    canvas.draw_text("Press 2 to exit", [320, 600], 40, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 1280, 720)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()