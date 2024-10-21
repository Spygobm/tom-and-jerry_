import pgzrun
import random

HEIGHT = 720
WIDTH = 1080

TITLE = "tom and jerry"

tom = Actor("tom")
tom.pos = (WIDTH//2,HEIGHT//2)
jerry = Actor("jerry")
jerry.pos = (random.randint(0,WIDTH),random.randint(0,HEIGHT))
score = 0
is_game_over = False

def move_jerry():
    jerry.pos =(random.randint(20,WIDTH - 20),random.randint(20,HEIGHT - 20))

def draw():
    screen.blit("backround",(0,0))
    tom.draw()
    jerry.draw()


    #adding text on the screen 
    screen.draw.text("score = {}".format(score),color = "black",topleft = (540,50),fontsize = 35)
    if is_game_over:
        screen.fill(color = "red")
        screen.draw.text("Game over score - {}".format(score),color = "black",midtop = (540,0),fontsize = 50)


def update():
    global score
    if keyboard.left:
        tom.x -= 2
    if keyboard.right:
        tom.x += 2
    if keyboard.up:
        tom.y -= 2
    if keyboard.down:
        tom.y += 2
    #check collision between 2 actors
    if tom.colliderect(jerry):
        score += 10
        move_jerry()

def game_over():
    global is_game_over
    is_game_over = True

clock.schedule(game_over,60.0)
pgzrun.go()