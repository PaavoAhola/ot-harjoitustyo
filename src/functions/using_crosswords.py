import pygame

def launch_crossword(crossword):
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((300,300))
    pygame.display.set_caption("Crossword")

    font = pygame.font.Font(None, 36)

    active_x = 0
    active_y = 0

    quit = False

    while not quit:
        screen.fill(pygame.Color(250,250,250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
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
                if event.key == pygame.K_SPACE:
                    crossword.squares[active_x][active_y].switch()
                letter =  pygame.key.name(event.key)
                if letter in "abcdefghijklmnopqrstuvwxyzåäö":
                    crossword.squares[active_x][active_y].insert_letter(letter)
        for row in crossword.squares:
            for square in row:
                square.surface = pygame.Surface((30,30))
                if square.on:
                    square.surface.fill(pygame.Color(0,0,0))
                else:
                    square.surface.fill(pygame.Color(100,30,30))
                square_text = font.render(square.letter, True, pygame.Color(30,30,80), None)
                square_rect = square.surface.get_rect(topleft=(30*square.position[0], 30*square.position[1]))
                screen.blit(square_text, square_rect)
        pygame.display.flip()
