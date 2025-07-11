#import pgzrun
from random import randint

mydot = Actor("dot")

WIDTH = 400
HEIGHT = 400

dots = []
lines = []
next_dot = 0
game_won = False

#Create dots list pg. 74
#Draw 10 dots to connect
for dot in range(0, 15):    
    mydot = Actor("dot")
    mydot.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(mydot)

def draw():
    #Create game windows with dots displayed pg. 75
    screen.fill("black")
    number = 1
    #Plot dots on the game screen
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()        
        number += 1

    #Draw lines connecting dots when clicked
    for line in lines:
        screen.draw.line(line[0], line[1], ("purple")) #(100,0,0)
    
    if game_won:
        screen.draw.text("You win!", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="yellow")

#Built-in functions using pgzrun to determine with mouse is clicked
def on_mouse_down(pos):
    #Create mouse_down function pg. 77
    global next_dot
    global lines
    global game_won

    if dots[next_dot].collidepoint(pos):
        if next_dot:
            fromDot = dots[next_dot - 1].pos
            toDot = dots[next_dot].pos
            toConnect = (fromDot,toDot)

            lines.append(toConnect)

            totLineLength = len(lines)
            totDotsLength = len(dots)-1

            #Check that all dots have been connected
            if totLineLength == totDotsLength:
                game_won = True
        next_dot += 1
    else:
        #Start over if clicked on wrong dot
        lines = []
        next_dot = 0

#pgzrun.go()