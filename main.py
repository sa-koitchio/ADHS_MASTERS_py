import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
## load sprites
spr_note_right = pygame.image.load('sprites/spr_rightNote_0.png')
spr_note_left = pygame.image.load('sprites/spr_leftNote_0.png')
spr_note_up = pygame.image.load('sprites/spr_upNote_0.png')

bg_default = pygame.image.load('backgrounds/bg_main.png')

class MainWindow:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.display=pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Caption")

    def background(self, background):
        self.display.blit(background, (0,0))


# setup
gameDisplay = MainWindow(1920,1080)
gameDisplay.background(bg_default)


pygame.display.set_caption('ADHS*MASTERS')
clock = pygame.time.Clock()


def game_loop():

    gameExit = False

    while not gameExit:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        #

        ####


        ####

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
