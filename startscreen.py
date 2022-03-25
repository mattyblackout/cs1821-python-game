import simpleguitk as simplegui

BACKGROUND_IMAGE = simplegui.load_image('https://images2.imgbox.com/4a/38/b798aeH2_o.jpg')

LOGO_IMAGE = simplegui.load_image('https://images2.imgbox.com/1d/dd/4Kj7pUOr_o.png')
LOGO_IMAGE_DIMS = (1007, 235)

PRESSKEY_IMAGE = simplegui.load_image('https://images2.imgbox.com/4f/bc/cLxcNfmt_o.png')
PRESSKEY_IMAGE_DIMS = (1139, 178)

def draw(canvas):
    canvas.draw_image(BACKGROUND_IMAGE, (0, 0), (2650,1600), [10, 10], (2650,1600))
    canvas.draw_image(LOGO_IMAGE, (503, 117), LOGO_IMAGE_DIMS, (650, 300), (1007, 235), 0)
    canvas.draw_image(PRESSKEY_IMAGE, (570, 89), PRESSKEY_IMAGE_DIMS, (650, 450), (1139, 178), 0)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Main Menu", 1315, 790)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()