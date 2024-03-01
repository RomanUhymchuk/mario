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

        keys = key.get_pressed()
        if keys[K_a] and self.rect.x:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x :
            self.rect.x += self.speed


        
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
FPS = 60

mario = Player('mario-main/mario/Нова папка/smallmariosheet-removebg-preview_1.png', 100, 470, 10, 10, 10) 


jump_count =8
jump_height =8
jumping = False
x_bg =0 
run = True
while run:
    keys = key.get_pressed()
    window.blit(backk,(x_bg,0))
    window.blit(backk,(x_bg-win_height,0))

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
    

    mario.update()

    mario.reset()
    if keys[K_a] :
        x_bg+=5
    if keys[K_d] :
        x_bg-=5
    if x_bg == -win_width:
        x_bg=0
    time.delay(30)
    display.update()
    clock.tick(FPS)

