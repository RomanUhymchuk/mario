from pygame import *

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
    def reset (self): 
        window.blit(self.image,(self.rect.x , self.rect.y)) 

class Player(GameSprite):
    def update(self):
        global isJump ,jumpCount ,vel 
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x :
            self.rect.x += self.speed
        
        if isJump:
            if jumpCount >= -10:
                self.rect.y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False

        if not(isJump): 
            if keys[K_a] and self.rect.x > vel:
                self.rect.x += vel

            if keys[K_d] and self.rect.x > vel:
                self.rect.x += vel

            if keys[K_SPACE]:
                isJump = True
win_width = 1200
win_height = 600

#ігрова сцена:

window = display.set_mode((win_width, win_height))
back = ("1661354146_1-kartinkin-net-p-fon-mario-dlya-skretcha-krasivo-1.jpg") 
backk = transform.scale(image.load("1661354146_1-kartinkin-net-p-fon-mario-dlya-skretcha-krasivo-1.jpg"),(win_width, win_height))  

#прапорці, що відповідають за стан гри
game = True
finish = False
clock = time.Clock()
FPS = 30

mario = Player('mario-main/mario/Нова папка/smallmariosheet-removebg-preview_1.png', 100, 470, 10, 10, 10) 




vel = 5
isJump = False
jumpCount = 10

run = True

while run:
    time.delay(100)

    for e in event.get():
        if e.type == QUIT:
            run = False
        window.blit(backk,(0,0))
   
    

        mario.update()

        mario.reset()
       
    display.update()
    clock.tick(FPS)

