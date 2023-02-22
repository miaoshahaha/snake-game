import pygame
import random
pygame.init()

window = pygame.display.set_mode((510,510))
pygame.display.set_caption(u'我家的蛇蛇')
bg=pygame.image.load("images.jpg")
#遊戲的相關資訊，物件位置
head_x = 150
head_y = 300
head = [head_x,head_y]

body_x = 120
body_y = 300
body = [
    [body_x,body_y],
    [body_x-30,body_y],
    [body_x-60,body_y],

]
fireball = [[0,0]   #誰說要火球的

]

food =[
    [240,150]
]

posion =[
    [480,300]
]
n = 0
(IsUp, IsDown, IsLeft, IsRight) = (False, False, False, True)
#跑遊戲LOOP
run = True
pop = True

while run:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run=False
    window.blit(bg,(0,0))
    my_font=pygame.font.SysFont("arial",24)
    text_surface=my_font.render(u"Press 1 to Start. ",False,(0,0,0),bg)
    window.blit(text_surface,(180,250))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_1]:
        run=False
    pygame.display.update()
music=pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
run=True
while run:
    pygame.time.delay(42)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.blit(bg,(0,0))
    my_font=pygame.font.SysFont("arial",24)
    text_surface1=my_font.render(u"score: ",False,(0,0,0),bg)
    window.blit(text_surface1,(400,20))
    text_surface2=my_font.render(str(len(body)-3),False,(0,0,0),bg)
    window.blit(text_surface2,(470,20))
    #showFont('bc',8,20)

    if pop == True:
        body.pop()
    if IsUp:
        body.insert(0, [head_x, head_y])
        head_y -= 30
        picu = pygame.image.load("picu.png")
        pictureu = pygame.transform.scale(picu,(40,40))
        window.blit(pictureu,(head_x-8,head_y-5))
    if IsDown:
        body.insert(0, [head_x, head_y])
        head_y += 30
        picd = pygame.image.load("picd.png")
        pictured = pygame.transform.scale(picd,(40,40))
        window.blit(pictured,(head_x-8,head_y))
    if IsLeft:
        body.insert(0, [head_x, head_y])
        head_x -= 30
        picl = pygame.image.load("picl.png")
        picturel = pygame.transform.scale(picl,(40,40))
        window.blit(picturel,(head_x-8,head_y-8))
    if IsRight:
        body.insert(0, [head_x, head_y])
        head_x += 30
        picr = pygame.image.load("picr.png")
        picturer = pygame.transform.scale(picr,(40,40))
        window.blit(picturer,(head_x-8,head_y-8))

#穿牆
    if head_x <= -10:
        head_x += 510
        #print(head_x)
    elif head_x >= 490:
        head_x -= 510
        #print(head_x)
    if head_y <= -10:
        head_y += 510
        #print(head_x)
    elif head_y >= 510:
        head_y -= 510
        #print(head_x)

#蛇的身體


    for i in range(len(body)):
        pygame.draw.rect(window, (0, 255, 0), (body[i-1][0], body[i-1][1], 25, 25))

#吃
    #pygame.draw.rect(window,(0,255,255),(food[0][0],food[0][1],25,25))
    foodpic = pygame.image.load("超透明包子.png")
    pictureu = pygame.transform.scale(foodpic,(35,35))
    window.blit(pictureu,(food[0][0]-5,food[0][1]))
    for a in posion:
        #pygame.draw.rect(window,(255,255,0),(a[0],a[1],25,25))
        posionpic = pygame.image.load("透明維尼.png")
        pictureu = pygame.transform.scale(posionpic,(40,40))
        window.blit(pictureu,(a[0]-10,a[1]))
    x = random.randrange(0, 510, 30)
    y = random.randrange(0, 510, 30)
    x2 = random.randrange(0, 510, 30)
    y2 = random.randrange(0, 510, 30)
    if (head_x,head_y) == (food[0][0],food[0][1]):
        food.insert(0,[x,y])
        pop = False
        food.pop()
        n=n+1
        if n == 3:
            posion.insert(0,[x2,y2])
            n = 0
            if posion[0][0] in body:
                poison.pop()
                posion.insert(0,[x2,y2])
            
    else:
        pop = True
#毒
    #pygame.draw.rect(window,(255,255,0),(posion[0][0],posion[0][1],25,25))
    #x = random.randrange(0, 510, 30)
    #y = random.randrange(0, 510, 30)
    #if int(len(body-3)) % 3 == 0:
        #poison.insert(0,[x,y])

#按鍵相關

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and IsDown == False:
        (IsUp, IsDown, IsLeft, IsRight) = (True, False, False, False)
    elif keys[pygame.K_DOWN] and IsUp == False:
        (IsUp, IsDown, IsLeft, IsRight) = (False, True, False, False)
    elif keys[pygame.K_LEFT] and IsRight == False:
        (IsUp, IsDown, IsLeft, IsRight) = (False, False, True, False)
    elif keys[pygame.K_RIGHT] and IsLeft == False:
        (IsUp, IsDown, IsLeft, IsRight) = (False, False, False, True)


    if keys[pygame.K_SPACE]:
        if IsUp:
            fireball.insert(0,[head_x,head_y-60])
        if IsDown:
            fireball.insert(0,[head_x,head_y+60])
        if IsLeft:
            fireball.insert(0,[head_x-60,head_y])
        if IsRight:
            fireball.insert(0,[head_x+60,head_y])



        pygame.draw.rect(window,(255,0,0),(fireball[0][0],fireball[0][1],20,20))

# 死亡
    if [head_x, head_y] in body or [head_x, head_y] in posion:
        
        run = False
        
    print(x,y)
    
    pygame.display.update()
music=pygame.mixer.music.load("start23.mp3")
pygame.mixer.music.play()
run=True
while run:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run=False
    window.blit(bg,(0,0))
    my_font=pygame.font.SysFont("arial",24)
    text_surface=my_font.render(u"Gameover.",False,(0,0,0),bg)
    window.blit(text_surface,(180,250))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_2]:
        run=False
    pygame.display.update()

pygame.quit()

