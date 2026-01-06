import pygame
from pathlib import Path
from ui.constants import *
class Splash():
    def __init__(self, app):
        self.app = app
        self.color = CYAN
        

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.app.change_screen(Main_menu_screen(self.app))

    def update(self):
        pass

    def draw(self, surface):
        surface.fill(self.color)
        #TODO quitar sección de cargar imagen
        # localizar ruta del proyecto y cargar la imagen del logo de la iglesia
        project_root = Path(__file__).resolve().parents[1]
        image_path = project_root / 'data' / 'assets' / 'image' / 'church_brand.jpeg'

        # alternativas comunes si la ruta anterior no existe
        if not image_path.exists():
            alt = project_root / 'data' / 'church_brand.jpeg'
            if alt.exists():
                image_path = alt

        if image_path.exists():
            image = pygame.image.load(str(image_path))
            # escalar el logo a un tamaño razonable (ajusta si hace falta)
            image = pygame.transform.smoothscale(image, (220, 220))
            image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
            surface.blit(image, image_rect)
        else:
            # texto de fallback si no se encuentra la imagen
            no_image = FONT_NORMAL.render('Logo no encontrado', True, WHITE)
            surface.blit(no_image, (WIDTH // 2 - no_image.get_width() // 2, HEIGHT // 2 - 10))
        
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
        self.color = YELLOW

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.change_screen(Splash(self.app))

    def update(self):
        pass

    def draw(self, surface):
        surface.fill(self.color)

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





