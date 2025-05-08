import time
from pygame.locals import *
import pygame

AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fondo2.png'
MUSICA_FONS = 'assets/music.mp3'
WHITE = (255,255,255)
GREEN = (50,205,50)
MAGENTA = (255, 0, 255)
RED = (255,0,0)

guanyador = 0
# pantalles del joc
# pantalla 1 menu
# pantalla 2 credits
# pantalla 3 joc
# pantalla 4 game over
pantalla_actual = 1

# Jugador 1:
player_image = pygame.image.load('assets/nau.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 14


# Jugador 2:
player_image2 = pygame.image.load('assets/enemic.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 500))
velocitat_nau2 = 14

# vides:
vides_jugador1 = 3
vides_jugador2 = 3
vides_jugador1_image = pygame.image.load('assets/vida1.png')
vides_jugador2_image = pygame.image.load('assets/vida2.png')

# Bala rectangular blanca:
bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 14
temps_entre_bales = 10 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2


pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")

# Control de FPS
clock = pygame.time.Clock()
fps = 30

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

def show_menu():
    imprimir_pantalla_fons(BACKGROUND_IMAGE)
    text0 = "Yowi SPACE!"
    text1 = "1. Començar partida"
    text2 = "2. Veure crèdits"
    text3 = "3. Sortir"
    font0 = pygame.font.SysFont(None, 140)
    font1 = pygame.font.SysFont(None, 100)
    img0 = font0.render(text0, True, GREEN)
    img1 = font1.render(text1, True, MAGENTA)
    img2 = font1.render(text2, True, MAGENTA)
    img3 = font1.render(text3, True, RED)
    pantalla.blit(img0, (60, 60))
    pantalla.blit(img1, (60, 200))
    pantalla.blit(img2, (60, 300))
    pantalla.blit(img3, (60, 400))

def show_credits():
    imprimir_pantalla_fons(BACKGROUND_IMAGE)
    text0 = "SPACE GUARS"
    text1 = "Programació:"
    text2 = "Gràfics:"
    text3 = "Música:"
    text4 = "Sons:"
    text5 = "Joel Blanch - Xavi Sancho"
    text6 = "After Burner 3 - Sega"
    text7 = "Freesound.org"
    font0 = pygame.font.SysFont(None, 140)
    font1 = pygame.font.SysFont(None, 60)
    font2 = pygame.font.SysFont(None, 50)
    img0 = font0.render(text0, True, GREEN)
    img1 = font1.render(text1, True, MAGENTA)
    img2 = font1.render(text2, True, MAGENTA)
    img3 = font1.render(text3, True, MAGENTA)
    img4 = font1.render(text4, True, MAGENTA)
    img5 = font2.render(text5, True, RED)
    img6 = font2.render(text6, True, GREEN)
    img7 = font2.render(text7, True, GREEN)
    pantalla.blit(img0, (60, 60))
    pantalla.blit(img1, (60, 200))
    pantalla.blit(img5, (160, 250))
    pantalla.blit(img2, (60, 300))
    pantalla.blit(img5, (160, 350))
    pantalla.blit(img3, (60, 400))
    pantalla.blit(img6, (160, 450))
    pantalla.blit(img4, (60, 500))
    pantalla.blit(img7, (160, 550))

while True:
    #contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if pantalla_actual == 2:
            show_credits()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pantalla_actual = 1


        if pantalla_actual == 1:
            if event.type == KEYDOWN:
                if event.key == K_3:
                    pygame.quit()
                if event.key == K_1:
                    pantalla_actual = 3
                if event.key == K_2:
                    pantalla_actual = 2



        if pantalla_actual == 4:
            for i in bales_jugador1:
                bales_jugador1.remove(i)
            for i in bales_jugador2:
                bales_jugador2.remove(i)
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    vides_jugador1 = 3
                    vides_jugador2 = 3
                    pantalla_actual = 1


        if pantalla_actual == 3:
            # controlar trets de les naus
            if event.type == KEYDOWN:
                #jugador 1
                if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                    bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador1 = current_time
                # jugador 2
                if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                    bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                    temps_ultima_bala_jugador2 = current_time

    if pantalla_actual == 1:
        show_menu()

    if pantalla_actual == 2:
        show_credits()



    if pantalla_actual == 4:
        imprimir_pantalla_fons("assets/game_over.png")
        text = "Player " + str(guanyador) + " Wins!"
        font = pygame.font.SysFont(None, 64)
        img = font.render(text, True, GREEN)
        pantalla.blit(img, (250,0))


    if pantalla_actual == 1:
        show_menu()

    if pantalla_actual == 3:
        # Moviment del jugador 1
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            player_rect.x -= velocitat_nau
        if keys[K_d]:
            player_rect.x += velocitat_nau
        # Moviment del jugador 2
        if keys[K_LEFT]:
            player_rect2.x -= velocitat_nau2
        if keys[K_RIGHT]:
            player_rect2.x += velocitat_nau2



        # Mantenir al jugador dins de la pantalla:
        player_rect.clamp_ip(pantalla.get_rect())
        player_rect2.clamp_ip(pantalla.get_rect())

        #dibuixar el fons:
        imprimir_pantalla_fons(BACKGROUND_IMAGE)

        #Actualitzar i dibuixar les bales del jugador 1:
        for bala in bales_jugador1: # bucle que recorre totes les bales
            bala.y -= velocitat_bales # mou la bala
            if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
                bales_jugador1.remove(bala) # si ha sortit elimina la bala
            else:
                pantalla.blit(bala_imatge, bala) # si no ha sortit la dibuixa
            # Detectar col·lisions jugador 2:
            if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 1!")
                bales_jugador1.remove(bala)  # eliminem la bala
                vides_jugador2 = vides_jugador2 -1
                print("vides jugador 2:", vides_jugador2)
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador2:
            bala.y += velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador2.remove(bala)
            else:
                pantalla.blit(bala_imatge, bala)
            # Detectar col·lisions jugador 1:
            if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 2!")
                bales_jugador2.remove(bala)  # eliminem la bala
                vides_jugador1 = vides_jugador1 - 1
                print("vides jugador 1:",vides_jugador1)
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        #dibuixar els jugadors:
        pantalla.blit(player_image, player_rect)
        pantalla.blit(player_image2, player_rect2)

        #dibuixar vides
        if vides_jugador1 >= 3:
            pantalla.blit(vides_jugador1_image,(620,550))
        if vides_jugador1 >= 2:
            pantalla.blit(vides_jugador1_image, (680, 550))
        if vides_jugador1 >= 1:
            pantalla.blit(vides_jugador1_image, (740, 550))

        if vides_jugador2 >= 1:
            pantalla.blit(vides_jugador2_image,(0,0))
        if vides_jugador2 >= 2:
            pantalla.blit(vides_jugador2_image, (60, 0))
        if vides_jugador2 >= 3:
            pantalla.blit(vides_jugador2_image, (120, 0))



        # comprobem si ha perdut
        if vides_jugador1 <=0 or vides_jugador2<= 0:
            guanyador = 1
            if vides_jugador1 <= 0:
                guanyador = 2

            pantalla_actual = 4

    pygame.display.update()
    clock.tick(fps)
