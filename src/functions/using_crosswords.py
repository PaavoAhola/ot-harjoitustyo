import pygame

def create_crossword(crossword):
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((500,300))
    pygame.display.set_caption(crossword.name)

    font = pygame.font.Font(None, 36)
    advice_font = pygame.font.Font(None, 16)
    hint_font = pygame.font.Font(None, 14)

    active_x = 0
    active_y = 0
    active_square = crossword.squares[active_x][active_y]

    quit = False

    while not quit:
        change_requested = False
        screen.fill(pygame.Color(124,204,250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and active_y > 0:
                    active_y -= 1
                if event.key == pygame.K_DOWN and active_y < 9:
                    active_y += 1
                if event.key == pygame.K_RIGHT and active_x < 9:
                    active_x += 1
                if event.key == pygame.K_LEFT and active_x > 0:
                    active_x -= 1
                active_square = crossword.squares[active_x][active_y]
                if event.key == pygame.K_SPACE:
                    active_square.switch()
                if event.key == pygame.K_PLUS:
                    change_requested = True
                if event.key == pygame.K_BACKSPACE:
                    active_square.insert_letter(" ")
                letter = pygame.key.name(event.key)
                if letter in "abcdefghijklmnopqrstuvwxyzåäö":
                    active_square.insert_letter(letter)
        if quit:
            break


        advice_text1 = advice_font.render("Liiku nuolinäppäimillä", True, pygame.Color(0,0,0))
        advice_text2 = advice_font.render("Paina välilyöntiä peittääksesi/", True, pygame.Color(0,0,0))
        advice_text3 = advice_font.render("aktivoidaksesi ruudun", True, pygame.Color(0,0,0))
        advice_text4 = advice_font.render("Valitse hiirellä X, kun haluat julkaista/", True, pygame.Color(0,0,0))
        advice_text5 = advice_font.render("tallentaa/hylätä luomuksesi", True, pygame.Color(0,0,0))
        advice_text6 = advice_font.render("Paina '+' muokataksesi vihjettä", True, pygame.Color(0,0,0))

        advice_rect1 = advice_text1.get_rect(topleft=(301,190))
        advice_rect2 = advice_text2.get_rect(topleft=(301,210))
        advice_rect3 = advice_text3.get_rect(topleft=(301,220))
        advice_rect6 = advice_text6.get_rect(topleft=(301,240))
        advice_rect4 = advice_text4.get_rect(topleft=(301,260))
        advice_rect5 = advice_text5.get_rect(topleft=(301,270))

        screen.blit(advice_text1, advice_rect1)
        screen.blit(advice_text2, advice_rect2)
        screen.blit(advice_text3, advice_rect3)
        screen.blit(advice_text4, advice_rect4)
        screen.blit(advice_text5, advice_rect5)
        screen.blit(advice_text6, advice_rect6)

        for row in crossword.squares:
            for square in row:
                square.surface = pygame.Surface((30,30))
                if square.on:
                    square.surface.fill(pygame.Color(255,255,255))
                else:
                    square.surface.fill(pygame.Color(0,0,0))
                active_square.surface.fill(pygame.Color(238,249,84))
                square_text = font.render(square.letter, True, pygame.Color(0,0,0), None)
                square_rect = square.surface.get_rect(topleft=(30*square.position[0], 30*square.position[1]))
                screen.blit(square.surface, square_rect)
                screen.blit(square_text, square_rect)

        if not active_square.on:
            if change_requested:
                choice = input("Muokataanko vihjettä oikealle(1) vai alas(2)?")
                if choice == "1":
                    active_square.hint_right = input("Uusi vihje oikealle: ")
                elif choice == "2":
                    active_square.hint_down = input("Uusi vihje alas: ")
            right_hint_text = hint_font.render("Oikealle: " + active_square.hint_right, True, pygame.Color(0,0,0))
            down_hint_text = hint_font.render("Alas: " + active_square.hint_down, True, pygame.Color(0,0,0))
            right_hint_rect = right_hint_text.get_rect(topleft=(300,5))
            down_hint_rect = down_hint_text.get_rect(topleft=(300,15))
            screen.blit(right_hint_text, right_hint_rect)
            screen.blit(down_hint_text, down_hint_rect)

        pygame.display.flip()


    for row in crossword.squares:
        for square in row:
            square.surface = None

def play_crossword(crossword):
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((500,300))
    pygame.display.set_caption(crossword.name)

    font = pygame.font.Font(None, 36)
    advice_font = pygame.font.Font(None, 16)
    hint_font = pygame.font.Font(None, 14)

    active_x = 0
    active_y = 0
    active_square = crossword.squares[active_x][active_y]

    quit = False

    while not quit:
        screen.fill(pygame.Color(124,204,250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and active_y > 0:
                    active_y -= 1
                if event.key == pygame.K_DOWN and active_y < 9:
                    active_y += 1
                if event.key == pygame.K_RIGHT and active_x < 9:
                    active_x += 1
                if event.key == pygame.K_LEFT and active_x > 0:
                    active_x -= 1
                active_square = crossword.squares[active_x][active_y]
                if event.key == pygame.K_BACKSPACE:
                    active_square.insert_letter(" ")
                letter = pygame.key.name(event.key)
                if letter in "abcdefghijklmnopqrstuvwxyzåäö":
                    active_square.insert_letter(letter)
        if quit:
            break


        advice_text1 = advice_font.render("Liiku nuolinäppäimillä", True, pygame.Color(0,0,0))
        advice_text4 = advice_font.render("Valitse hiirellä X, kun olet valmis", True, pygame.Color(0,0,0))

        advice_rect1 = advice_text1.get_rect(topleft=(301,240))
        advice_rect4 = advice_text4.get_rect(topleft=(301,260))


        screen.blit(advice_text1, advice_rect1)
        screen.blit(advice_text4, advice_rect4)

        for row in crossword.squares:
            for square in row:
                square.surface = pygame.Surface((30,30))
                if square.on:
                    square.surface.fill(pygame.Color(255,255,255))
                else:
                    square.surface.fill(pygame.Color(0,0,0))
                active_square.surface.fill(pygame.Color(238,249,84))
                square_text = font.render(square.letter, True, pygame.Color(0,0,0), None)
                square_rect = square.surface.get_rect(topleft=(30*square.position[0], 30*square.position[1]))
                screen.blit(square.surface, square_rect)
                screen.blit(square_text, square_rect)

        if not active_square.on:
            right_hint_text = hint_font.render("Oikealle: " + active_square.hint_right, True, pygame.Color(0,0,0))
            down_hint_text = hint_font.render("Alas: " + active_square.hint_down, True, pygame.Color(0,0,0))
            right_hint_rect = right_hint_text.get_rect(topleft=(300,5))
            down_hint_rect = down_hint_text.get_rect(topleft=(300,15))
            screen.blit(right_hint_text, right_hint_rect)
            screen.blit(down_hint_text, down_hint_rect)

        pygame.display.flip()


    for row in crossword.squares:
        for square in row:
            square.surface = None

    return crossword
