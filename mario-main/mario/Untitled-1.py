from pygame import *
from random import randint 
mixer.init() 
mixer.music.load("mario-main/01. Ground Theme.mp3") 
mixer.music.play() 
fire = mixer.Sound("mario-main/01. Ground Theme.mp3") 
#make window
win_width = 1200
win_height = 600
window = display.set_mode((1200, 600))

player_l = [image.load('mario-main/mario/Нова папка (4)/mariosheet-removebg-preview_1.png'), image.load('mario-main/mario/Нова папка (4)/mariosheet-removebg-preview_3.png')]

player_r = [image.load('mario-main/mario/Нова папка (4)/mariosheet-removebg-preview_13.png'), image.load('mario-main/mario/Нова папка (4)/mariosheet-removebg-preview_14.png')]

#make class
class GameSprite(sprite.Sprite): 
    init()
    def __init__(self, player_image , player_x , player_y, size_x, size_y, player_speed): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(50 , 50))  
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
        self.size_x = size_x
        self.size_y = size_y
        self.left = False
        self.right = False
        self.count = 0
 
    def reset (self): 
        window.blit(self.image,(self.rect.x , self.rect.y)) 
#class player
class Player(GameSprite):
    def update(self):

        keys = key.get_pressed()
        if keys[K_a] and self.rect.x:
            if self.rect.x < 1:
                self.rect.x = 1
            self.rect.x -= self.speed
            self.left = True
            self.right = False
        if keys[K_d] and self.rect.x :
            self.rect.x += self.speed
            self.left = False
            self.right = True
        else:            
            self.right = self.left = False


    def animation(self):
        if self.left:
            self.count = (self.count + 1) % len(player_l)  
            window.blit(player_l[self.count], (self.rect.x, self.rect.y))
        elif self.right:
            self.count = (self.count + 1) % len(player_l)  
            window.blit(player_r[self.count], (self.rect.x, self.rect.y))
        else:
            self.count=0
            window.blit(player_r[self.count], (self.rect.x, self.rect.y))

back = transform.scale(image.load("1661354146_1-kartinkin-net-p-fon-mario-dlya-skretcha-krasivo-1.jpg"),(win_width, win_height))  
display.set_caption("Mario Game ")
#class enemy
mario = Player('mario-main/mario/Нова папка (4)/mariosheet-removebg-preview_1.png', 250, 470, 10, 10, 3) 

class Enemy (GameSprite):
    def update(self):
        self.rect.y += self.speed 
        #znukae aikscho diyde  do kraay ekrana
        if self.rect.y < 0:
            self.kill()


class Enemy(GameSprite): 
    def update(self): 
        self.rect.x -= self.speed 
        if self.rect.x> win_width: 
            self.rect.x = randint(80, win_height +80) 
            self.rect.x = 0 


bullet = 'mario-main/imgonline-com-ua-Mirror-gZ5dwLoVeP3Q5o-removebg-preview.png'
monsters = sprite.Group()
for i in range(1, 3): 
    monster = Enemy(bullet, randint(800, 1200), 470, 80, 50, randint(1, 5)) 
    monsters.add(monster)            
# Створення гравця



# Змінні для стрибків
jump_count = 8
jump_height = 8
jumping = False

# Переміщення фону
x_bg = 0 

x_bg = 0
y_bg = 0

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
    if x_bg >= win_width or x_bg <= -win_width:
        x_bg = 0
    
    # Переміщення фону

    if keys[K_d]:
        x_bg -= 10

    mario.update()
    monsters.update()
    mario.reset()
    monsters.draw(window)
   

    # Перевірка закінчення фону в обидва боки

    time.delay(30)
    display.update()
quit()
