import pygame
from ui.screens import Splash, Main_menu_screen, Buy_screen, History_screen, Credits_screen
from ui import constants
class Menu():
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((constants.WIDTH,constants.HEIGHT))
        pygame.display.set_caption("Mi app")

        self.clock = pygame.time.Clock()
        self.running = True

        #pantalla actual
        self.current_screen = None

    def change_screen(self, new_screen):
        self.current_screen = new_screen


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if self.current_screen:
                    self.current_screen.handle_event(event)

            if self.current_screen:
                self.current_screen.update()
                self.current_screen.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


    