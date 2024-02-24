from pygame import *

class GameSprite(sprite.Sprite): 

    def __init__(self, player_image , player_x , player_y, size_x, syze_y, player_speed): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(50 , 50))  
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset (self): 
        window.blit(self.image,(self.rect.x , self.rect.y)) 

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
win_width = 1200
win_height = 600

#ігрова сцена:

window = display.set_mode((win_width, win_height))
back = ("1661354146_1-kartinkin-net-p-fon-mario-dlya-skretcha-krasivo-1.jpg") 
backk = transform.scale(image.load("1661354146_1-kartinkin-net-p-fon-mario-dlya-skretcha-krasivo-1.jpg"),(win_width, win_height))  
window.blit(backk,(0,0))
 
#прапорці, що відповідають за стан гри
game = True
finish = False
clock = time.Clock()
FPS = 30

mario = Player('mario-main/mario/Нова папка (4)/mariosheet-removebg-preview_1.png', 100, 470, 200, 200, 150) 








while game:
    for e in event.get():
        if e.type == QUIT:
                game = False 



        mario.reset()

    display.update()
    clock.tick(FPS)
