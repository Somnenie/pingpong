from pygame import *
from random import *
from typing import Any 



font.init()
font1 = font.SysFont(None, 36)
font2 = font.SysFont(None, 36)

start_ticks = time.get_ticks()
game_duration =  120

win_heidth = 455
win_wight = 802

passes_player = 0
passes_frends = 0

dx = 3
dy = 3

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

game = True 
class Enemy(GameSprite):
    def update(self):
        global dx, dy, finish, passes_frends, passes_player

        self.rect.x += dx
        self.rect.y += dy

        
        if self.rect.top <= 40 or self.rect.bottom >= win_heidth:
            dy *= -1

        
        if self.rect.colliderect(player.rect) or self.rect.colliderect(friend.rect):
            dx *= -1

        
        if self.rect.left <= 0:
            passes_player += 1
            time.delay(1000)
            self.rect.x = win_wight // 2 - self.rect.width // 2
            self.rect.y = win_heidth // 2 - self.rect.height // 2
            dx *= -1  

        if self.rect.right >= win_wight:
            passes_frends += 1
            time.delay(1000)
            self.rect.x = win_wight // 2 - self.rect.width // 2
            self.rect.y = win_heidth // 2 - self.rect.height // 2
            dx *= -1  

        if passes_frends == 10 or passes_player == 10:
            finish = True



player = Player('Computer.png', 80, 180, 18, 120, 10)
friend = Friend('Player.png', 700, 180, 18, 120, 10)
ball = Enemy('Ball.png', 400, 180, 45, 45, 3)
pass_1 = GameSprite('ScoreBar.png', 0, 0, 360, 40, 10)
pass_2 = GameSprite('ScoreBarm.png', 442, 0, 360, 40, 10)

finish = False

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
        pass_1.reset()
        pass_2.reset()


    text_lose = font1.render(str(passes_frends),1, (255, 255, 255))
    win.blit(text_lose, (600, 7))
    text_moni = font2.render(str(passes_player), 1, (255, 255, 255))
    win.blit(text_moni, (200, 7))

    if passes_player == 10:
        text_lose = font1.render('Победил игрок 2',1, (255, 255, 255))
        win.blit(text_lose, (330, 200))

    if passes_frends == 10:
        text_lose = font1.render('Победил игрок 1',1, (255, 255, 255))
        win.blit(text_lose, (330, 200))


    seconds_passed = (time.get_ticks() - start_ticks) // 1000
    time_left = max(0, game_duration - seconds_passed)

    
    if time_left == 0 and passes_player < passes_frends:
        text_lose = font1.render('Победил игрок 1',1, (255, 255, 255))
        win.blit(text_lose, (330, 200))
        finish = True

    if time_left == 0 and passes_frends < passes_player:
        text_lose = font1.render('Победил игрок 2',1, (255, 255, 255))
        win.blit(text_lose, (330, 200))
        finish = True

    if time_left == 0 and passes_frends == passes_player:
        text_lose = font1.render('Ничья',1, (255, 255, 255))
        win.blit(text_lose, (330, 200))
        finish = True

    
    timer_text = font1.render(f"{time_left}", 1, (255, 255, 255))
    win.blit(timer_text, (388, 7))
    
    
    display.update()
    clock.tick(FPS)

    