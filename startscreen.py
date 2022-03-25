import simpleguitk as simplegui

BACKGROUNDIMG = simplegui.load_image('https://images2.imgbox.com/4a/38/b798aeH2_o.jpg')

LOGOIMG = simplegui.load_image('https://images2.imgbox.com/1d/dd/4Kj7pUOr_o.png')
LOGOIMG_DIMS = (1007, 235)

TEXTIMG = simplegui.load_image('https://images2.imgbox.com/4f/bc/cLxcNfmt_o.png')
TEXTIMG_DIMS = (1139, 178)


def draw(canvas):
    canvas.draw_image(BACKGROUNDIMG, (0, 0), (2650,1600), [10, 10], (2650,1600))
    canvas.draw_image(LOGOIMG, (503, 117), LOGOIMG_DIMS, (650, 300), (1007, 235), 0)
    canvas.draw_image(TEXTIMG, (570, 89), TEXTIMG_DIMS, (650, 450), (1139, 178), 0)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 1315, 790)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()