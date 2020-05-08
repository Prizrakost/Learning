import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Something")

walkRight = [pygame.image.load('assets/right_1.png'), pygame.image.load('assets/right_2.png')]
walkLeft = [pygame.image.load('assets/left_1.png')]

bg = pygame.image.load('assets/bg.png')
playerStandLeft = pygame.image.load('assets/idle_left.png')
playerStandRight = pygame.image.load('assets/idle_right.png')

clock = pygame.time.Clock()

width = 36
height = 64
x = 250 - width/2
y = 500 - height
speed = 10

isJump = False
jumpCount = 10

left = False
leftStand = False
rightStand = True
right = False
animCount = 0


def drawWindow():
    global animCount, leftStand, rightStand
    # win.fill((140, 140, 140))
    win.blit(bg, (0, 0))
    if animCount + 1 >= 5:
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
    elif leftStand:
        win.blit(playerStandLeft, (x, y))
    elif rightStand:
        win.blit(playerStandRight, (x, y))

    pygame.display.update()


run = True
while run:
    clock.tick(30)
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
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
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

    drawWindow()

pygame.quit()
