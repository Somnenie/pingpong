from pygame import *

win = display.set_mode((802, 455))
background = transform.scale(image.load('Board.png'),(802, 455))
display.set_caption('Ping pong for Nikito4ka')

clock = time.Clock()
FPS = 60

finish = False
game = True 
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        win.blit(background,(0, 0))

    display.update()
    clock.tick(FPS)