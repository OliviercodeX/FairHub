# Example file showing a basic pygame "game loop"
import pygame

HEIGHT = 1280
WIDTH = 720 

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()

running = True

font_text = pygame.font.Font(None, 40)
button_text = font_text.render('screen', True, (0,0,0))
button =  button_text.get_rect(center=(screen.get_width()//2,
                             screen.get_height()//2))


text_welcome = font_text.render('Bienvenido al sistema de gestión de la feria Iglesia Metodista' \
' Espiritu de Vida',
          
                                True, (0,0,0))
text_center = text_welcome.get_rect(topright=(1200,100))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.rect(screen, (255,255,0), button)

    screen.blit(button_text,button)
    screen.blit(text_welcome,text_center)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()