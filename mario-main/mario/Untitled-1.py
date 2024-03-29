from pygame import *
from random import randint 
mixer.init() 
mixer.music.load("mario-main/01. Ground Theme.mp3") 
mixer.music.play() 
jump= mixer.Sound("sfx-13.mp3") 
#make window
win_width = 1200
win_height = 600
window = display.set_mode((1200, 600))


player_l = [transform.scale(image.load('mariosheet-removebg-preview_11-removebg-preview.png','mariosheet-removebg-preview_12-removebg-preview (1).png'), (50, 50)),
            transform.scale(image.load('mariosheet-removebg-preview_13-removebg-preview (12).png'), (50, 50))]
player_r = [transform.scale(image.load('mario-main/mario/Нова папка (4)/mariosheet-removebg-preview_1.png','mario-main/mario/Нова папка (4)/mariosheet-removebg-preview_13.png'), (50, 50)),
            transform.scale(image.load('mario-main/mario/Нова папка (4)/mariosheet-removebg-preview_13.png'), (50, 50))]
#make class
class GameSprite(sprite.Sprite): 
    init()
    def __init__(self, player_image , player_x , player_y, size_x, size_y, player_speed): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(size_x , size_y))  
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
        elif keys[K_d] and self.rect.x :
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
            self.count = (self.count + 1) % len(player_r)  
            window.blit(player_r[self.count], (self.rect.x, self.rect.y))
        else:
            self.count=0
            window.blit(player_r[self.count], (self.rect.x, self.rect.y))

back = transform.scale(image.load("1661354146_1-kartinkin-net-p-fon-mario-dlya-skretcha-krasivo-1.jpg"),(win_width, win_height))  
display.set_caption("Mario Game ")
#class enemy
mario = Player('mario-main/mario/Нова папка (4)/mariosheet-removebg-preview_1.png', 250, 470, 50, 50, 5) 
bullet_x = 1100
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
        if self.rect.x == 0:
            self.kill()
score = 0
lakiblock_x=0
lakiblock = Enemy("wip-new-question-block-animation-made-for-fan-made-mario-v0-5unqv87oj8y91.png", 550, 400, 30,30,0)
bullet = 'mario-main/imgonline-com-ua-Mirror-gZ5dwLoVeP3Q5o-removebg-preview.png'
monsters = sprite.Group()
blockcegla = "1692637191_art-oir-mobi-p-mario-kirpichiki-arti-pinterest-2.png"
mariojump = "mario-main/mario/Нова папка (4)/mariosheet-removebg-preview_7.png"
font1 = font.Font(None,80)
text_lose = font1.render("YOU LOSE" ,True ,(255, 0, 0))
font2 = font.Font(None,50)
text_score = font2.render("YOUR SCORE",score ,True ,(0 , 255, 0))
window.blit(text_score, (1100, 400))
for i in range(1,8): 
    monster = Enemy(bullet, 600,1200, 50, 50, 5) 
    monsters.add(monster) 
         
#СТВОРЕННЯ БЛОКІВ
blocks = sprite.Group()
for i in range(1):
    #ОДИНОЧНІ БЛОКИ
    block = Enemy(blockcegla, 500, 350, 50, 50,0)
    blocks.add(block)  
    block = Enemy(blockcegla, 400, 350, 50, 50,0)
    blocks.add(block)  
    block = Enemy(blockcegla, 420, 100, 50, 50,0)
    blocks.add(block) 

    block = Enemy(blockcegla, 600, 400, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 650, 400, 50, 50,0)
    blocks.add(block) 
    block = Enemy(blockcegla, 700, 400, 50, 50,0)
    blocks.add(block) 
    block = Enemy(blockcegla, 850, 350, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 900,350, 50, 50,0)
    blocks.add(block) 
    block = Enemy(blockcegla, 950, 350, 50, 50,0)
    blocks.add(block) 
    block = Enemy(blockcegla, 150, 350, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 200,350, 50, 50,0)
    blocks.add(block) 
    block = Enemy(blockcegla, 250, 350, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 250, 180, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 300, 180, 50, 50,0)
    blocks.add(block) 
    block = Enemy(blockcegla, 350, 180, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 500, 180, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 550, 180, 50, 50,0)
    blocks.add(block) 
    block = Enemy(blockcegla, 600, 180, 50, 50,0)
    blocks.add(block) 

    block = Enemy(blockcegla, 700, 270, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 750, 270, 50, 50,0)
    blocks.add(block) 

    block = Enemy(blockcegla, 10, 410, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 50, 410, 50, 50,0)
    blocks.add(block) 

    block = Enemy(blockcegla, 850, 190, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 900, 190, 50, 50,0)
    blocks.add(block)

    block = Enemy(blockcegla, 10, 150, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 60, 150, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 110, 150, 50, 50,0)
    blocks.add(block)

    block = Enemy(blockcegla, 1000, 150, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 1050, 150, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 1100, 150, 50, 50,0)
    blocks.add(block)
    block = Enemy(blockcegla, 670, 100, 50, 50,0)
    blocks.add(block) 
    block = Enemy(blockcegla, 720, 100, 50, 50,0)
    blocks.add(block) 
# Змінні для стрибків
jump_count = 8
jump_height = 8
jumping = False


x_bg = 0
y_bg = 0
finish = False
# Запуск гри
run = True
while run:
    keys = key.get_pressed()
    window.blit(back,(x_bg,0))
    window.blit(back,(x_bg - win_width,0))
    window.blit(back,(x_bg + win_width,0)) # Додана додаткова копія фону для оновлення в іншому напрямку
    window.blit(text_score, (900, 30))
    if sprite.spritecollide(mario, monsters, False):
        #run = False
        window.blit(text_lose, (200, 200))
    #if sprite.spritecollide(mario, monsters, True):
        #finish = False
        #window.blit(text_lose, (200, 200))
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not jumping:
        if keys[K_SPACE]:
            jumping = True 
            jump.play() 
            mariojump
    else:
        if jump_count >= -jump_height:
            neg = 1
            if jump_count < 0:
                neg = -1

            mario.rect.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 0.8
        else:
            jumping = False
            jump_count = jump_height

    # Перевірка, щоб персонаж не виходив за межі екрану
    if mario.rect.y > 470:
        mario.rect.y = 470
    if x_bg >= win_width or x_bg <= -win_width:
        x_bg = 0

    # Переміщення фону



    monsters.update()
    monsters.draw(window)

    mario.update()

    lakiblock.update()
    lakiblock.reset()
    blocks.update()
    blocks.draw(window)
    mario.animation()
    if monster.rect.x <=0:
        for i in range(1): 
            monster = Enemy(bullet, bullet_x-100, 470, 50, 50, 5) 
            monsters.add(monster) 
            monster = Enemy(bullet, bullet_x + 150 ,360, 50, 50, 5) 
            monsters.add(monster)  
            monster = Enemy(bullet, bullet_x -300 ,390, 50, 50, 5) 
            monsters.add(monster)       
    # Перевірка закінчення фону в обидва боки

    time.delay(40)
    display.update()
quit()
