import pygame
from pathlib import Path
from ui.constants import *
class Splash():
    def __init__(self, app):
        self.app = app
        self.color = PURPLE
        

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.app.change_screen(Main_menu_screen(self.app))
        if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint(event.pos):
                    self.app.change_screen(Main_menu_screen(self.app))

    def update(self):
        pass

    def draw(self, surface):
        global button_start
        surface.fill(self.color)

        
        path_logo_img = pygame.image.load('FairHub/data/assets/image/church_brand.jpeg')
        img_scale_log = pygame.transform.smoothscale(path_logo_img, (200,200))

        surface.blit(img_scale_log, (WIDTH / 2 - 100, HEIGHT / 2 - 120))
        


        #texto de titlo
        titulo = 'Bienvenidos al sistema de la feria \n' \
        '    Iglesia Evangelica Metodista \n       ' \
        '         Espiritu De Vida'
        lines = titulo.split("\n")

        cor_x = 100
        cor_y = 20

        #Estableciendo el titulo con un espaciado
        line_height = FONT_TITLE.get_height()
        for i, line in enumerate(lines):
         surface_title = FONT_TITLE.render(line, True, (WHITE))
         surface.blit(surface_title, (cor_x, cor_y + i * line_height))



        #dibujar botones de inicio
        button_start = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 + 100, 200, 50)
        text_button_start = FONT_LARGE.render('Iniciar', True, WHITE)
        
        #correr botones
        pygame.draw.rect(surface, GREEN, button_start)
        surface.blit(text_button_start,(button_start.x + 60 , button_start.y + 10))


class Main_menu_screen():
    def __init__(self, app):
        self.app = app
        self.color = CYAN
        self.cor_x = 250
        self.cor_y = 20
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.change_screen(Splash(self.app))

    def update(self):
        pass

    def draw(self, surface):
        surface.fill(self.color)

        #dibujar titulo ventana de principal
        title_text = FONT_TITLE.render('Menu de gestión', True, (WHITE))
        surface.blit(title_text, (self.cor_x, self.cor_y))

        #d

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





