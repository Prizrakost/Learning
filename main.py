import pygame
import sys
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Something")

walkRight = [pygame.image.load('assets/right_1.png'), pygame.image.load('assets/right_2.png')]
walkLeft = [pygame.image.load('assets/left_1.png'), pygame.image.load('assets/left_2.png')]

bg = [pygame.image.load('assets/bg_1.png'), pygame.image.load('assets/bg_2.png')]
playerStandLeft = pygame.image.load('assets/idle_left.png')
playerStandRight = pygame.image.load('assets/idle_right.png')
playerHitLeft = [pygame.image.load('assets/hit_left_1.png'), pygame.image.load('assets/hit_left_2.png')]
playerHitRight = [pygame.image.load('assets/hit_right_1.png'), pygame.image.load('assets/hit_right_2.png')]

clock = pygame.time.Clock()

width = 48
height = 64
x = 250 - width/2
y = 500 - height
speed = 10

isJump = False
jumpCount = 10

left = False
right = False
leftStand = False
rightStand = True
leftHit = False
rightHit = False
animCount = 0

if len(sys.argv) > 1:
    if sys.argv[1] == '-d':
        d = sys.argv[2]
        if d != '':
            fps = int(d)
        else:
            fps = 30
else:
    fps = 30


def drawWindow():
    global animCount, leftStand, rightStand
    # win.fill((140, 140, 140))
    win.blit(bg[0], (0, 0))
    win.blit(bg[1], (0, 0))
    if animCount + 1 >= 10:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
        leftStand = True
        rightStand = False
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
        leftStand = False
        rightStand = True
    elif leftHit:
        win.blit(playerHitLeft[animCount // 5], (x, y))
        animCount += 1
    elif rightHit:
        win.blit(playerHitRight[animCount // 5], (x, y))
        animCount += 1
    else:
        if leftStand:
            win.blit(playerStandLeft, (x, y))
        elif rightStand:
            win.blit(playerStandRight, (x, y))

    pygame.display.update()


run = True
while run:
    clock.tick(fps)
    # pygame.time.delay(10)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not isJump:
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    if keys[pygame.K_SPACE]:
        if leftStand:
            leftHit = True
            rightHit = False
        elif rightStand:
            leftHit = False
            rightHit = True
    else:
        leftHit = False
        rightHit = False
        animCount = 0

    drawWindow()

pygame.quit()
