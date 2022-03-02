import simpleguitk as simplegui, random

i = 50
w = -1

def draw_handler(canvas):
    global w
    global i
    i += w

    canvas.draw_circle([50, 50], i, 1, 'red' , 'red')
    if i <= 10:
        w = 1
    if i >= 50:
        w= -1

frame = simplegui.create_frame('Testing', 100, 100)
frame.set_draw_handler(draw_handler)
frame.start()