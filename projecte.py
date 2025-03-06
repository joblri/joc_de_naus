import pygame, sys
from pygame.locals import *

AMPLE = 800
ALT = 600
TAMANY = (AMPLE,ALT)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
INDIGO = (75,0,130)
ORANGE = (255,102,0)
YELLOW = (255,213,0)
VIOLET = (127,0,255)
GREY = (150,150,150)
MAROON = (172,127,1)
BLACK = (0,0,0)
WHITE = (255,255,255)
OLIVE = (128,128,0)
CYAN = (0,255,255)
PINK = (255,192,203)
MAGENTA = (255,0,255)
TAN = (210,180,140)
TEAL = (0,128,128)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Color de fons')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(YELLOW)
    pygame.draw.circle(pantalla, WHITE, (450, 150), 100, )
    pygame.draw.circle(pantalla, BLACK, (450, 150), 100, 10)
    pygame.draw.circle(pantalla, BLACK, (300, 150), 100, 10)
    pygame.draw.rect(pantalla, YELLOW, (340, 170, 100, 80))
    pygame.draw.rect(pantalla, YELLOW, (340, 170, 100, 80))
    pygame.draw.rect(pantalla, BLACK, (340, 170, 100, 80),10)
    pygame.draw.rect(pantalla, YELLOW, (400, 170, 100, 80))
    pygame.draw.rect(pantalla, BLACK, (400, 170, 100, 80),10)
    pygame.draw.circle(pantalla, WHITE, (300, 150), 100, )
    pygame.draw.circle(pantalla, BLACK, (300, 150), 100, 10)
    pygame.draw.circle(pantalla, BLACK, (530, 150), 10, )
    pygame.draw.circle(pantalla, BLACK, (380, 150), 10, )


    pygame.draw.rect(pantalla, YELLOW, (395, 180, 60, 60))
    pygame.draw.rect(pantalla, WHITE, (490, 180, 10, 40))
    pygame.draw.circle(pantalla, BLACK, (460,210 ), 40,10 )
    pygame.draw.rect(pantalla, YELLOW, (395, 180, 60, 60))
    pygame.draw.rect(pantalla, YELLOW, (339, 240, 80, 80))
    pygame.draw.rect(pantalla, WHITE, (485, 170, 30, 5))
    pygame.draw.rect(pantalla, WHITE, (485, 175, 30, 5))
    pygame.draw.rect(pantalla, BLACK, (400, 170, 30, 9))
    pygame.draw.rect(pantalla, YELLOW, (480, 240, 20, 30))
    pygame.draw.circle(pantalla, MAROON, (400,380), 150)
    pygame.draw.circle(pantalla, BLACK, (450,350),(50))

    pygame.display.update()
