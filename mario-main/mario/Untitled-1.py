from pygame import *
from random import randint 
class GameSprite(sprite.Sprite): 

    def __init__(self, player_image , player_x , player_y, size_x, size_y, player_speed): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(50 , 50))  
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
        self.size_x = size_x
        self.size_y = size_y

#ФУНКЦІЇ ПЕРСОНАЖІВ 
    def reset (self): 
        window.blit(self.image,(self.rect.x , self.rect.y)) 

class Player(GameSprite):
    def update(self):

        keys = key.get_pressed()
        if keys[K_a] and self.rect.x:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x :
            self.rect.x += self.speed
class Block(GameSprite):
    pass
# Ініціалізація Pygame
class Enemy(GameSprite): 
    def update(self): 
        self.rect.x -= self.speed 
        global lost  
 
        if self.rect.x> win_width: 
            self.rect.x = randint(80, win_height +80) 
            self.rect.x = 0 
           
init()

# Встановлення розмірів вікна
win_width = 1200
win_height = 600
window = display.set_mode((1200, 600))
back = transform.scale(image.load("1661354146_1-kartinkin-net-p-fon-mario-dlya-skretcha-krasivo-1.jpg"),(win_width, win_height))  
display.set_caption("Mario Game ")
# Створення гравця
mario = Player('mario-main/mario/Нова папка/smallmariosheet-removebg-preview_1.png', 100, 470, 10, 10, 3) 
#block = Block("mario-main/mapsheet-removebg-previewgggggg.png", 300, 470, 10, 10, 3)
Bullet = Enemy('mario-main/imgonline-com-ua-Mirror-gZ5dwLoVeP3Q5o-removebg-preview.png',1200, 470, 10, 10, 3)

# Змінні для стрибків
jump_count = 8
jump_height = 8
jumping = False

# Переміщення фону
x_bg = 0 

# Запуск гри
run = True
while run:
    keys = key.get_pressed()
    window.blit(back,(x_bg,0))
    window.blit(back,(x_bg - win_width,0))
    window.blit(back,(x_bg + win_width,0)) # Додана додаткова копія фону для оновлення в іншому напрямку

    for e in event.get():
        if e.type == QUIT:
            run = False

    if not jumping:
        if keys[K_SPACE]:
            jumping = True

    else:
        if jump_count >= -jump_height:
            neg = 1
            if jump_count < 0:
                neg = -1
            mario.rect.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = jump_height

    # Перевірка, щоб персонаж не виходив за межі екрану
    if mario.rect.y > 470:
        mario.rect.y = 470

        Bullet.kill()
    mario.update()
    Bullet.update()
    #block.update()
    mario.reset()
    Bullet.reset()
    #block.reset()

    # Перевірка закінчення фону в обидва боки
    if x_bg >= win_width or x_bg <= -win_width:
        x_bg = 0
    
    # Переміщення фону
    if keys[K_a]:
        x_bg += 10
    if keys[K_d]:
        x_bg -= 10

    time.delay(30)
    display.update()
quit()
