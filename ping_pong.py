from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, w, h, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.speed_x = player_speed
        self.speed_y = int(player_speed / 2)
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
        global c1, c2
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 1 or self.rect.y > height - 101:
            pong.play()
            self.speed_y *= -1
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            pong.play()
            self.speed_x *= -1
        if self.rect.x < -101:
            c2 += 1
            count = font.SysFont('Times', 36).render(str(c1) + ' : ' + str(c2), 0, (0, 0, 0))
            self.rect.x = weight / 2 - 50
            self.rect.y = height / 2 - 50
            self.speed_x = 5
            self.speed_y = 5
        if self.rect.x > weight:
            c1 += 1
            count = font.SysFont('Times', 36).render(str(c1) + ' : ' + str(c2), 0, (0, 0, 0))
            self.rect.x = weight / 2 - 50
            self.rect.y = height / 2 - 50
            self.speed_x = -5
            self.speed_y = 5
            


weight = 1000
height = 600

c1 = 0
c2 = 0

window = display.set_mode((weight, height))
display.set_caption("Ping-Pong")

clock = time.Clock()

pong_sound = 'pong.ogg'
ball_png = 'ball.png'
paket = 'wall.png'

player1 = Player1(paket, 40, 100, 10, height / 2 - 50, 5)
player2 = Player2(paket, 40, 100, weight - 50, height / 2 - 50, 5)
ball = Ball(ball_png, 100, 100, weight / 2 - 50, height / 2 - 50, 5)

mixer.init()
pong = mixer.Sound(pong_sound)

font.init()
count = font.SysFont('Times', 36).render(str(c1) + ' : ' + str(c2), 0, (0, 0, 0))

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

        window.blit(count, (weight / 2 - 50, 50))    
        
    clock.tick(120)
    display.update()
    
