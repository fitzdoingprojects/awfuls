import pygame
from pygame.locals import *
from buttonsPC import * # For PC use
#from buttonsLinux import * # For Linux use

pygame.init()
width  = 1000
height = 500
size   = [width, height]
pygame.init()
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
effect1 = pygame.mixer.Sound('effect1.wav')
effect2 = pygame.mixer.Sound('effect2.wav')
effect3 = pygame.mixer.Sound('effect3.wav')
effect4 = pygame.mixer.Sound('effect4.wav')

pump = pygame.sprite.Sprite() # create sprite
pump.image = pygame.image.load("gaspumpstencil.png").convert() # load ball image
pygame.display.set_caption('Awfuls Gas')
location = [200, 200]
icon = pygame.image.load('ball.png')
pygame.display.set_icon(icon)
speed = 20

def buttonRight():
    effect3.play()
    location[0] = location[0]+speed
    if location[0]>width:
        location[0] = width


def buttonLeft():
    effect4.play()
    location[0] = location[0]-speed
    if location[0]<0:
        location[0] = 0


def buttonDown():
    effect1.play()
    location[1] = location[1]+speed
    if location[1]>height:
        location[0] = height


def buttonUp():
    effect2.play()
    location[1] = location[1]-speed
    if location[1]<0:
        location[1] = 0

while True: # main game loop
    while True:  # main game loop
        screen.fill((255, 255, 255))

        getButtons()
        if buttons[0] == b'1':
            buttonUp()
        if buttons[1] == b'1':
            buttonDown()
        if buttons[2] == b'1':
            buttonLeft()
        if buttons[3] == b'1':
            buttonRight()





        for event in pygame.event.get():


            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    buttonLeft()
                if event.key == pygame.K_RIGHT:
                    buttonRight()
                if event.key == pygame.K_UP:
                    buttonUp()

                if event.key == pygame.K_DOWN:
                    buttonDown()
        screen.blit(pump.image, location)
        pygame.display.update()