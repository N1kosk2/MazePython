import time
import pygame
pygame.init()
screen = pygame.display.set_mode((1024,768))
done = False
x=30
y=30
a = 200
b = 200
l = 80
k = 80
n = 240
q = 240
m = 333
r = 333
t = 900
i = 600
clock = pygame.time.Clock()
ts1 = time.time()
ts2 = time.time()
tol1 = 0
tol2 = 0
koukou = 1
def lvl1():
    global x,y,a,b,l,k,n,q,m,r,t,i,ts1,ts2,tol1,tol2,koukou
    pygame.display.flip()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:y-=5
    if pressed[pygame.K_DOWN]:y+=5
    if pressed[pygame.K_LEFT]:x-=5
    if pressed[pygame.K_RIGHT]:x+=5
    screen.fill((0,0,0))
    IMAGE=pygame.image.load("Panathinaikos_FC_logo.svg.png").convert()
    pl1 = IMAGE.get_rect()
    pl1.center = (x,y)
    screen.blit(IMAGE,pl1)
    IMAGE2=pygame.image.load("Olympiacos_FC_logo.svg.png").convert()
    pl2 = IMAGE2.get_rect()
    pl2.center = (a,b)
    screen.blit(IMAGE2,pl2)
    w1 = pygame.draw.rect(screen,(255,0,0),pygame.Rect(l,k,280,10))
    w2 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(n, q, 100, 400))
    w3 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(n, q, 400, 380))
    f = pygame.draw.rect(screen,(60,60,0), pygame.Rect(t, i,900, 600))
    if pressed[pygame.K_w]: b -= 5
    if pressed[pygame.K_s]: b += 5
    if pressed[pygame.K_a]: a -= 5
    if pressed[pygame.K_d]: a += 5

    Font = pygame.font.SysFont("comicsansms", 170, True,True)
    Title = Font.render("Maze Race", True,(0,0,90))
    screen.blit(Title,(100,100))
    if pl1.colliderect(w1) or pl1.colliderect(w2) or pl1.colliderect(w3):
        if pressed[pygame.K_UP]: y += 10
        if pressed[pygame.K_LEFT]: x += 10
        if pressed[pygame.K_RIGHT]: x -= 10
        if pressed[pygame.K_DOWN]: y -= 10

    if pl2.colliderect(w1) or pl2.colliderect(w2) or pl2.colliderect(w3):
        if pressed[pygame.K_w]: b += 10
        if pressed[pygame.K_a]: a += 10
        if pressed[pygame.K_d]: a -= 10
        if pressed[pygame.K_s]: b -= 10

    if pl1.colliderect(f) or pl1.colliderect(f) or pl1.colliderect(f):
        if pressed[pygame.K_UP]: y=30
        if pressed[pygame.K_LEFT]: x=30
        if pressed[pygame.K_RIGHT]: x=30
        if pressed[pygame.K_DOWN]: y=30

    if pl2.colliderect(f) or pl2.colliderect(f) or pl2.colliderect(f):
        if pressed[pygame.K_w]: b=200
        if pressed[pygame.K_a]: a=200
        if pressed[pygame.K_d]: a=200
        if pressed[pygame.K_s]: b=200

    if pl1.colliderect(f):
        x=30
        y=30
        te1 = time.time()
        tol1 = round(te1 - ts1 , 2)
        ts1 = time.time()


    Font1 = pygame.font.SysFont("comicsansms",20,True, True)
    Time1 = Font1.render("Time for PAO:" + str(tol1), True, (50, 50, 50))
    screen.blit(Time1, (50, 650))

    if pl2.colliderect(f):
        a = 120
        b = 120
        te2 = time.time()
        tol2 = round(te2 - ts2, 2)
        ts2 = time.time()

    Font2 = pygame.font.SysFont("comicsansms",20,True, True)
    Time2 = Font1.render("Time for OLY:" + str(tol2), True, (0, 255, 0))
    screen.blit(Time2, (80, 680))

def lvl2():
    global x,y,a,b,l,k,n,q,m,r,t,i,ts1,ts2,tol1,tol2,koukou
    pygame.display.flip()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:y-=5
    if pressed[pygame.K_DOWN]:y+=5
    if pressed[pygame.K_LEFT]:x-=5
    if pressed[pygame.K_RIGHT]:x+=5
    screen.fill((0,0,0))
    IMAGE=pygame.image.load("Panathinaikos_FC_logo.svg.png").convert()
    pl1 = IMAGE.get_rect()
    pl1.center = (x,y)
    screen.blit(IMAGE,pl1)
    IMAGE2=pygame.image.load("Olympiacos_FC_logo.svg.png").convert()
    pl2 = IMAGE2.get_rect()
    pl2.center = (a,b)
    screen.blit(IMAGE2,pl2)
    w1 = pygame.draw.rect(screen,(255,0,0),pygame.Rect(l,k,280,10))
    w2 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(n, q, 100, 400))
    w3 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(n, q, 400, 380))
    f = pygame.draw.rect(screen,(60,60,0), pygame.Rect(t, i,900, 600))
    if pressed[pygame.K_w]: b -= 5
    if pressed[pygame.K_s]: b += 5
    if pressed[pygame.K_a]: a -= 5
    if pressed[pygame.K_d]: a += 5

    Font = pygame.font.SysFont("comicsansms", 170, True,True)
    Title = Font.render("Maze Race", True,(0,0,90))
    screen.blit(Title,(100,100))
    if pl1.colliderect(w1) or pl1.colliderect(w2) or pl1.colliderect(w3):
        if pressed[pygame.K_UP]: y += 10
        if pressed[pygame.K_LEFT]: x += 10
        if pressed[pygame.K_RIGHT]: x -= 10
        if pressed[pygame.K_DOWN]: y -= 10

    if pl2.colliderect(w1) or pl2.colliderect(w2) or pl2.colliderect(w3):
        if pressed[pygame.K_w]: b += 10
        if pressed[pygame.K_a]: a += 10
        if pressed[pygame.K_d]: a -= 10
        if pressed[pygame.K_s]: b -= 10

    if pl1.colliderect(f) or pl1.colliderect(f) or pl1.colliderect(f):
        if pressed[pygame.K_UP]: y=30
        if pressed[pygame.K_LEFT]: x=30
        if pressed[pygame.K_RIGHT]: x=30
        if pressed[pygame.K_DOWN]: y=30

    if pl2.colliderect(f) or pl2.colliderect(f) or pl2.colliderect(f):
        if pressed[pygame.K_w]: b=200
        if pressed[pygame.K_a]: a=200
        if pressed[pygame.K_d]: a=200
        if pressed[pygame.K_s]: b=200

    if pl1.colliderect(f):
        x=30
        y=30
        te1 = time.time()
        tol1 = round(te1 - ts1 , 2)
        ts1 = time.time()


    Font1 = pygame.font.SysFont("comicsansms",20,True, True)
    Time1 = Font1.render("Time for PAO:" + str(tol1), True, (50, 50, 50))
    screen.blit(Time1, (50, 650))

    if pl2.colliderect(f):
        a = 120
        b = 120
        te2 = time.time()
        tol2 = round(te2 - ts2, 2)
        ts2 = time.time()

    Font2 = pygame.font.SysFont("comicsansms",20,True, True)
    Time2 = Font1.render("Time for OLY:" + str(tol2), True, (0, 255, 0))
    screen.blit(Time2, (80, 680))
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    if koukou==1:
     lvl1()
    elif koukou==2:
        lvl2()



    pygame.display.flip()
    clock.tick(60)




