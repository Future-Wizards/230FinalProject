import pygame, sys, time
from pygame.locals import *

pygame.init()

FPS = 30
clock = pygame.time.Clock()

w = 800
h = 500
screen = pygame.display.set_mode((w, h), 0, 32)
pygame.display.set_caption('Animation')

bif = "megamanBG.jpg"
plyr = "megaman.png"

background = pygame.image.load(bif)
player = pygame.image.load(plyr)

playerx = 100
playery = 130


width = 0
height = 0
newWidth = 0
newHeight = 0

keepGoing = True
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[K_LEFT]:
        newWidth += 5
        screen.blit(background, (newWidth, newHeight))

    if keys_pressed[K_RIGHT]:
        newWidth -= 5
        screen.blit(background, (newWidth, newHeight))

    screen.blit(background, (width, height))
    screen.blit(background, (newWidth, newHeight))
    screen.blit(player, (playerx,playery))
    if width > w:
        width = -w
    if newWidth > w:
        newWidth = -w

    pygame.display.flip()
    clock.tick(FPS)
