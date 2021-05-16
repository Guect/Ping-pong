from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, w, h, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.speed_x = player_speed
        self.speed_y = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed() 
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < height - 100:
            self.rect.y += self.speed
    
class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed() 
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < height - 100:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


weight = 800
height = 600

window = display.set_mode((weight, height))
display.set_caption("Ping-Pong")

clock = time.Clock()

player1 = Player1('wall.png', 40, 100, 10, height / 2 - 50, 5)
player2 = Player2('wall.png', 40, 100, weight - 50, height / 2 - 50, 5)
ball = Ball('ball.png', 100, 100, weight / 2 - 50, height / 2 - 50, 25)

#font.init()
#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()

'''font.init()
wiwin = font.SysFont('Times', 36).render("YOU WIN!!!",1,(0,255,0))
lolose = font.SysFont('Times', 36).render("YOU lose!!!",1,(255,0,0))
lilive = font.SysFont('Times', 36).render (str(live),0,(0,255,0))'''

finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if not(finish):
        window.fill((255, 255, 255))

        player1.update()
        player2.update()
        ball.update()

        player1.reset()
        player2.reset()
        ball.reset()
    
        
    clock.tick(120)
    display.update()
    
