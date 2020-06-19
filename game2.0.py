import pygame
from pygame.locals import *

pygame.init()  # initialise modules

screen = pygame.display.set_mode((1250, 650))   # screen
pygame.display.set_caption("VCS")  # game name


def game():

    Black = (0, 0, 0)  # colour for the font
    score = 0  # initial score value

    backvelocity = 5  # background velocity only 5 and 10 work
    backx = 0  # background position x
    backy = 0  # background position y
    bluex = 600  # blue obstacle position x
    bluey = 505  # blue obstacle position y
    mariox = 10  # mario obstacle position x
    marioy = 500  # mario obstacle position y
    runningpoint = 0  # index for running
    duckpoint = 0   # index for ducking

    duck = False  # to check if the character is ducking
    temp = False  # to check if the character is running
    jump = False  # to check if the character is jumping
    g = 5       # for falling down
    over = False

    font = pygame.font.Font('freesansbold.ttf', 35)     # score font

    background = pygame.image.load("background2.jpg")   # load the images
    mario1 = pygame.image.load("mario1.v3.png")
    mario2 = pygame.image.load("mario2.v3.png")
    mario3 = pygame.image.load("mario3.v3.png")
    mario4 = pygame.image.load("mario4.v3.png")
    mario5 = pygame.image.load("mario5.v3.png")
    mario6 = pygame.image.load("mario6.v3.png")

    run = [mario1, mario2, mario2, mario2, mario2, mario2, mario2, mario2, mario2, mario2, mario2,
           mario3, mario3, mario3, mario3, mario3, mario3, mario3, mario3, mario3, mario3,
           mario4, mario4, mario4, mario4, mario4, mario4, mario4, mario4, mario4, mario4,
           ]  # make running animation look normal

    duckrun = [mario5, mario5, mario5, mario5, mario5, mario5, mario5, mario5, mario5, mario5,
              mario6, mario6, mario6, mario6, mario6, mario6, mario6, mario6, mario6, mario6,]
             # make ducking animation look normal

    brown = pygame.image.load("brown2.png")  # obstacles images
    blue = pygame.image.load("blue.png")
    orange = pygame.image.load("orange.png")
    green = pygame.image.load("green.png")
    spike = pygame.image.load("spike.png")
    rocket = pygame.image.load("rocket.png")
    bullet = pygame.image.load("bullet.png")

    while True:         # main loop
        for event in pygame.event.get():    # loop to keep it running

            if event.type == QUIT:   # to quit
                pygame.quit()

            if event.type == KEYDOWN:   # if a key is pressed
                if event.key == K_UP:   # up arrow key
                    jump = True         # jumps
                    temp = True         # runs
                    duck = False

                if event.key == K_DOWN:
                    duck = True         # ducks

                if event.key == K_SPACE:
                    game()              # restarts the game

        if temp:                        # running animation
            runningpoint += 1
            if runningpoint > 20:
                runningpoint = 2

        if 501 > marioy > 300:          # mario's height is within this range
            if jump:
                screen.blit(run[0], [mariox, marioy])       # to display the animation
                marioy -= g              # to go up

        else:
            jump = False

        if marioy < 500:        # to come down
            if not jump:
                marioy += g

        if duck:                        # ducking animation
            duckpoint += 1
            if duckpoint > 19:
                duckpoint = 1

        else:
            duck = False

        if backx == -1250:              # to keep the background repeating
            backx = 0

        if bluex == -2400:              # to keep obstacles repeating
            bluex = 600

        if bluex < mariox + 57 < bluex + 77 and bluey < marioy + 94 < bluey + 93:   # positions of obstacles along x, y
            backvelocity = 0                                                        # background stops
            runningpoint = 21
            screen.blit(run[runningpoint], [mariox, marioy])                        # display the collided mario
            duck = False
            temp = False
            over = True

        if bluex + 400 < mariox + 57 < bluex + 535 and 0 < marioy < 510:    # condition is different when needed to duck
            if duck:                                                       # because the height of the character changes
                duck = True
            else:
                backvelocity = 0
                runningpoint = 21
                screen.blit(run[runningpoint], [mariox, marioy])
                duck = False
                temp = False
                over = True

        if bluex + 800 < mariox + 57 < bluex + 877 and bluey + 8 < marioy + 94 < bluey + 93:
            backvelocity = 0
            runningpoint = 21
            screen.blit(run[runningpoint], [mariox, marioy])
            duck = False
            temp = False
            over = True

        if bluex + 1200 < mariox + 57 < bluex + 1277 and bluey < marioy + 94 < bluey + 93:
            backvelocity = 0
            runningpoint = 21
            screen.blit(run[runningpoint], [mariox, marioy])
            duck = False
            temp = False
            over = True

        if bluex + 1600 < mariox + 57 < bluex + 1735 and bluey + 35 < marioy + 94 < bluey + 93:
            backvelocity = 0
            runningpoint = 21
            screen.blit(run[runningpoint], [mariox, marioy])
            duck = False
            temp = False
            over = True

        if bluex + 2000 < mariox + 57 < bluex + 2077 and 0 < marioy < 510:
            if duck:
                duck = True
            else:
                backvelocity = 0
                runningpoint = 21
                screen.blit(run[runningpoint], [mariox, marioy])
                duck = False
                temp = False
                over = True

        if bluex + 2400 < mariox + 57 < bluex + 2477 and bluey + 40 < marioy + 94 < bluey + 93:
            backvelocity = 0
            runningpoint = 21
            screen.blit(run[runningpoint], [mariox, marioy])
            duck = False
            temp = False
            over = True

        if temp:            # increment the score
            score += 1

        text = font.render("SCORE : "+ str(score), True, Black)     # text for the score
        text2 = font.render("GAME OVER :(  SPACE TO START AGAIN", True, Black)   # text for game over
        backx -= backvelocity       # background moves
        bluex -= backvelocity       # obstacle moves along with background

        screen.blit(background, [backx, backy])  # display background
        screen.blit(background, [backx + 1250, backy])      # 2nd background for it to repeat

        if not over:
            screen.blit(text, [538, 150])       # display the score

        if over:
            screen.blit(text, [538, 150])       # display the score
            screen.blit(text2, [300, 200])      # display game over

        if jump:          # animation for jump
            screen.blit(run[0], [mariox, marioy])

        if duck:           # animation for duck
            screen.blit(duckrun[duckpoint], [10, 530])

        if not jump and not duck:   # animation for running
            screen.blit(run[runningpoint], [mariox, marioy])

        screen.blit(blue, [bluex, bluey])           # display obstacles
        screen.blit(rocket, [bluex + 400, bluey - 85])
        screen.blit(brown, [bluex + 800, bluey + 8])
        screen.blit(spike, [bluex + 1200, bluey])
        screen.blit(orange, [bluex + 1600, bluey + 35])
        screen.blit(bullet, [bluex + 2000, bluey - 85])
        screen.blit(green, [bluex + 2400, bluey + 40])

        pygame.display.update()  # update
game()