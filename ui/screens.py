import pygame
from ui.constants import *
class Splash():
    def __init__(self, app):
        self.app = app
        self.color = BLUE

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.app.change_screen(Main_menu_screen(self.app))

    def update(self):
        pass

    def draw(self, surface):
        surface.fill(self.color)

class Main_menu_screen():
    def __init__(self, app):
        self.app = app
        self.color = YELLOW

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.change_screen(Splash(self.app))

    def update(self):
        pass

    def draw(self, surface):
        surface.fill(self.color)

class Buy_screen():
    def __init__(self):
        pass

    def handle_event(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

class History_screen():
    def __init__(self):
        pass
        
    def handle_event(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

class Credits_screen():
    def __init__(self):
        pass
    
    def handle_event(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass





