from pygame import *
from random import *
from typing import Any 

win_heidth = 455
win_wight = 802

#dx = 3
#dy = 3

win = display.set_mode((802, 455))
background = transform.scale(image.load('Board.png'),(802, 455))
display.set_caption('Ping pong for Nikito4ka')

clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, says_x, says_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (says_x, says_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < win_heidth - 150 :
            self.rect.y += self.speed

class Friend(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < win_heidth - 150:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        global popusk
        
        dx = 3
        dy = 3

        if self.rect.y < win_heidth:
            self.rect.x += self.speed
            self.rect.y -= self.speed
            
        if ball.rect.colliderect(friend.rect):
            self.speed *= -1
            
        if ball.rect.colliderect(player.rect):
            self.speed *= -1
            
        if ball.rect.y > 450 or ball.rect.y <0:
            self.speed *= -1
            

player = Player('Computer.png', 80, 180, 18, 120, 10)
friend = Friend('Player.png', 700, 180, 18, 120, 10)
ball = Enemy('Ball.png', 400, 180, 45, 45, 3)

finish = False
game = True 
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        win.blit(background,(0, 0))

       

    player.reset()
    player.update()
    friend.reset()
    friend.update()
    ball.reset()
    ball.update()

 

     
    
    display.update()
    clock.tick(FPS)

    