import pygame
import sys
# TODO: align center quit statemnet



# initializing the constructor
pygame.init()

# screen resolution
res = (720, 720)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

mouse = pygame.mouse.get_pos()

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
text = smallfont.render('Quit', True, color)

while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
        break

    if ev.type == pygame.MOUSEBUTTONDOWN:

        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.quit()
            break

    # fills the screen with a color
    screen.fill((60, 25, 60))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade

    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

    # superimposing the text onto our button
    screen.blit(text, (width / 2 + 40, height / 2 + 5))

    # updates the frames of the game
    pygame.display.update()
