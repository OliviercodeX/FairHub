import pygame, pygame_gui
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
        txt_btn_start_rect = text_button_start.get_rect(center=button_start.center)
        surface.blit(text_button_start, txt_btn_start_rect)


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
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    self.app.running = False
                if sell_button.collidepoint(event.pos):
                    self.app.change_screen(Buy_screen(self.app))
                if create_chinamo_button.collidepoint(event.pos):
                    self.app.change_screen(Create_chinamo_screen(self.app))
                if history_button.collidepoint(event.pos):
                    self.app.change_screen(History_screen(self.app))
                if credits_button.collidepoint(event.pos):
                    self.app.change_screen(Credits_screen(self.app))
    def update(self):
        pass

    def draw(self, surface):
        global exit_button
        global sell_button
        global create_chinamo_button
        global history_button
        global credits_button
        surface.fill(self.color)

        #dibujar titulo ventana de principal
        title_text = FONT_TITLE.render('Menu de gestión', True, (WHITE))
        surface.blit(title_text, (self.cor_x, self.cor_y))

        #crear serie de botones
        sell_button = pygame.Rect(self.cor_x + 50, self.cor_y + 90, 200, 50)
        create_chinamo_button = pygame.Rect(self.cor_x + 50, self.cor_y + 160, 200, 50)
        history_button = pygame.Rect(self.cor_x + 50, self.cor_y + 230, 200, 50)
        credits_button = pygame.Rect(self.cor_x + 50, self.cor_y + 300, 200, 50)
        exit_button = pygame.Rect(self.cor_x + 50, self.cor_y + 370, 200, 50)

        #dibujar botones
        pygame.draw.rect(surface, GREEN, sell_button)
        pygame.draw.rect(surface, YELLOW, create_chinamo_button)
        pygame.draw.rect(surface, ORANGE, history_button)
        pygame.draw.rect(surface, PURPLE, credits_button)
        pygame.draw.rect(surface, RED, exit_button)
        
        #crear texto botones
        sell_button_txt = FONT_MEDIUM.render('Ventas', True, (WHITE))
        create_chinamo_button_txt = FONT_MEDIUM.render('Crear Chinamo', True, (WHITE))
        history_button_txt = FONT_MEDIUM.render('Historial', True, (WHITE)) 
        credits_button_txt = FONT_MEDIUM.render('Creditos', True, (WHITE))  
        exit_button_txt = FONT_MEDIUM.render('Salir', True, (WHITE))    


        #dibujar texto botones (centrado)
        sell_txt_rect = sell_button_txt.get_rect(center=sell_button.center)
        create_ch_txt_rect = create_chinamo_button_txt.get_rect(center=create_chinamo_button.center)
        history_txt_rect = history_button_txt.get_rect(center=history_button.center)
        credits_txt_rect = credits_button_txt.get_rect(center=credits_button.center)
        exit_txt_rect = exit_button_txt.get_rect(center=exit_button.center)

        surface.blit(sell_button_txt, sell_txt_rect)
        surface.blit(create_chinamo_button_txt, create_ch_txt_rect)
        surface.blit(history_button_txt, history_txt_rect)
        surface.blit(credits_button_txt, credits_txt_rect)
        surface.blit(exit_button_txt, exit_txt_rect)

class Buy_screen():
    def __init__(self, app, x=100, y=100, w=200, h=30, opciones=None):
        self.app = app
        self.color = GREEN
        self.cor_x = 250
        self.cor_y = 20
        self.rect = pygame.Rect(x, y, w, h)
        self.opciones = opciones if opciones is not None else ["Opción 1", "Opción 2", "Opción 3"]
        self.color_base = (200, 200, 200)
        self.color_hover = (170, 170, 170)
        self.abierto = False
        self.seleccionada = "Seleccionar..."
        
        # Botón de salida/volver
        self.exit_button = pygame.Rect(self.cor_x + 50, self.cor_y + 370, 200, 50)
        
        # Carrito (por ahora no funcional)
        carrito_ancho = 250
        carrito_alto = 300
        carrito_x = WIDTH - carrito_ancho - 20  # 20 píxeles de margen desde la derecha
        carrito_y = 80  # Un poco abajo del título
        self.carrito_rect = pygame.Rect(carrito_x, carrito_y, carrito_ancho, carrito_alto)

        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.change_screen(Main_menu_screen(self.app))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic izquierdo
                # Verificar clic en botón de salida
                if self.exit_button.collidepoint(event.pos):
                    self.app.change_screen(Main_menu_screen(self.app))
                # Verificar clic en el dropdown principal
                elif self.rect.collidepoint(event.pos):
                    self.abierto = not self.abierto
                # Verificar clic en una opción del dropdown
                elif self.abierto:
                    for i, opcion in enumerate(self.opciones):
                        rect_opcion = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.h, self.rect.w, self.rect.h)
                        if rect_opcion.collidepoint(event.pos):
                            self.seleccionada = opcion
                            self.abierto = False
                            break
                # Si se hace clic fuera del dropdown, cerrarlo
                else:
                    self.abierto = False

    def update(self):
        pass

    def draw(self, surface):
        surface.fill(self.color)
        
        # Título
        title_text = FONT_TITLE.render('Pantalla de Ventas', True, (WHITE))
        surface.blit(title_text, (self.cor_x, self.cor_y))
        
        # Dibujar carrito
        # Texto "Carrito" arriba del cuadro
        carrito_titulo = FONT_MEDIUM.render('Carrito', True, (WHITE))
        carrito_titulo_x = self.carrito_rect.x + (self.carrito_rect.w - carrito_titulo.get_width()) // 2
        surface.blit(carrito_titulo, (carrito_titulo_x, self.carrito_rect.y - 35))
        
        # Cuadro del carrito: área interna grisácea
        pygame.draw.rect(surface, LIGHT_GRAY, self.carrito_rect)
        # Perímetro (borde) negro
        pygame.draw.rect(surface, BLACK, self.carrito_rect, 2)
        
        # Dibujar dropdown
        color_actual = self.color_hover if self.rect.collidepoint(pygame.mouse.get_pos()) else self.color_base
        pygame.draw.rect(surface, color_actual, self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2) # Borde
        
        texto = FONT_SMALL.render(self.seleccionada, True, (0, 0, 0))
        surface.blit(texto, (self.rect.x + 5, self.rect.y + 5))
        
        # Dibujar flechita (triángulo) - invertido cuando está abierto
        tri_x = self.rect.x + self.rect.w - 20
        tri_y = self.rect.y + 10
        if self.abierto:
            # Triángulo hacia arriba cuando está abierto
            pygame.draw.polygon(surface, (0, 0, 0), [[tri_x, tri_y + 10], [tri_x + 10, tri_y + 10], [tri_x + 5, tri_y]])
        else:
            # Triángulo hacia abajo cuando está cerrado
            pygame.draw.polygon(surface, (0, 0, 0), [[tri_x, tri_y], [tri_x + 10, tri_y], [tri_x + 5, tri_y + 10]])

        # Si está abierto, dibujar las opciones
        if self.abierto:
            for i, opcion in enumerate(self.opciones):
                rect_opcion = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.h, self.rect.w, self.rect.h)
                
                # Efecto hover en las opciones
                mouse_pos = pygame.mouse.get_pos()
                color = self.color_hover if rect_opcion.collidepoint(mouse_pos) else (255, 255, 255)
                
                pygame.draw.rect(surface, color, rect_opcion)
                pygame.draw.rect(surface, (0, 0, 0), rect_opcion, 1) # Borde fino
                
                txt_opcion = FONT_SMALL.render(opcion, True, (0, 0, 0))
                surface.blit(txt_opcion, (rect_opcion.x + 5, rect_opcion.y + 5))

                

        # Botón de salida
        pygame.draw.rect(surface, RED, self.exit_button)
        exit_button_txt = FONT_MEDIUM.render('Volver', True, (WHITE))
        exit_txt_rect = exit_button_txt.get_rect(center=self.exit_button.center)
        surface.blit(exit_button_txt, exit_txt_rect)
        



class History_screen():
    def __init__(self, app):
        self.app = app
        self.color = ORANGE
        self.cor_x = 250
        self.cor_y = 20
        
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.change_screen(Main_menu_screen(self.app))
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    self.app.running = False


    def update(self):
        pass

    def draw(self, surface):
        surface.fill(self.color)
        

class Credits_screen():
    def __init__(self, app):
        self.app = app
        self.color = PURPLE
        self.cor_x = 250
        self.cor_y = 20
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.change_screen(Main_menu_screen(self.app))
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    self.app.running = False

    def update(self):
        
        pass

    def draw(self, surface):
        surface.fill(self.color)


class Create_chinamo_screen():
    def __init__(self, app):
        self.app = app
        self.color = YELLOW
        self.cor_x = 250
        self.cor_y = 20
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.change_screen(Main_menu_screen(self.app))
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    self.app.running = False

    def update(self):
        pass

    def draw(self, surface):
        surface.fill(self.color)



