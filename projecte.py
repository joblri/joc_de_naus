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
