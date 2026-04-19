from numpy.char import center
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
        self.opciones = opciones if opciones is not None else ["Arroz con pollo", "Pollo a la brasa", "Ceviche"]
        self.color_base = (200, 200, 200)
        self.color_hover = (170, 170, 170)
        self.abierto = False
        self.seleccionada = "Seleccionar..."
        # Scroll para el dropdown
        self.scroll_offset = 0
        self.max_opciones_visibles = 8  # Máximo de opciones visibles a la vez
        
        # Botón de salida/volver (esquina inferior izquierda)
        self.exit_button = pygame.Rect(20, HEIGHT - 70, 200, 50)
        self.fiar_button = pygame.Rect(WIDTH - 440, HEIGHT - 70, 200, 50)
        self.buy_button = pygame.Rect(WIDTH - 220, HEIGHT - 70, 200, 50)
        
        # Carrito (por ahora no funcional)
        carrito_ancho = 250
        carrito_alto = 300
        carrito_x = WIDTH - carrito_ancho - 20  # 20 píxeles de margen desde la derecha
        carrito_y = 80  # Un poco abajo del título
        self.carrito_rect = pygame.Rect(carrito_x, carrito_y, carrito_ancho, carrito_alto)

        #confimación de compra
        self.carrito = [] #lista de productos
        self.confirmation_msj = None
        
        # Scroll para el carrito
        self.scroll_offset_carrito = 0
        self.max_productos_visibles = (carrito_alto - 40) // 30
        
        # Delay para eliminación de productos
        self.delete_delay = 250  # 1 segundo en milisegundos (ajustable)
        self.delete_start_time = None
        self.product_to_delete = None
        
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
                # Verificar clic en el botón fiar
                elif self.fiar_button.collidepoint(event.pos):
                    pass  # Por ahora no hace nada
                # Verificar clic en una opción del dropdown
                elif self.abierto:
                    total_opciones = len(self.opciones)
                    clic_en_scroll = False
                    
                    # Verificar clic en la barra de scroll
                    if total_opciones > self.max_opciones_visibles:
                        scroll_area_height = self.max_opciones_visibles * self.rect.h
                        scroll_bar_x = self.rect.x + self.rect.w - 15
                        scroll_bar_y = self.rect.y + self.rect.h
                        scroll_bar_width = 12
                        scroll_bar_rect = pygame.Rect(scroll_bar_x, scroll_bar_y, scroll_bar_width, scroll_area_height)
                        
                        if scroll_bar_rect.collidepoint(event.pos):
                            # Calcular nueva posición del scroll basada en el clic
                            max_scroll = max(0, total_opciones - self.max_opciones_visibles)
                            click_y_relativo = event.pos[1] - scroll_bar_y
                            self.scroll_offset = int((click_y_relativo / scroll_area_height) * max_scroll)
                            self.scroll_offset = max(0, min(self.scroll_offset, max_scroll))
                            clic_en_scroll = True
                    
                    # Verificar clic en las opciones visibles (solo si no se hizo clic en la barra de scroll)
                    if not clic_en_scroll:
                        for i in range(min(self.max_opciones_visibles, total_opciones - self.scroll_offset)):
                            indice_real = i + self.scroll_offset
                            if indice_real >= total_opciones:
                                break
                            rect_opcion = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.h, self.rect.w, self.rect.h)
                            if rect_opcion.collidepoint(event.pos):
                                self.seleccionada = self.opciones[indice_real]
                                self.carrito.append(self.opciones[indice_real])
                                self.abierto = False
                                self.scroll_offset = 0  # Resetear scroll al seleccionar
                                break
                # Si se hace clic fuera del dropdown, cerrarlo
                else:
                    self.abierto = False
        elif event.type == pygame.MOUSEWHEEL:
            # Scroll con la rueda del mouse cuando el dropdown está abierto
            if self.abierto:
                total_opciones = len(self.opciones)
                if total_opciones > self.max_opciones_visibles:
                    max_scroll = max(0, total_opciones - self.max_opciones_visibles)
                    # event.y es positivo hacia arriba, negativo hacia abajo
                    self.scroll_offset -= int(event.y)  # Invertir para que sea intuitivo
                    self.scroll_offset = max(0, min(self.scroll_offset, max_scroll))
            # Scroll para el carrito
            if self.carrito_rect.collidepoint(pygame.mouse.get_pos()):
                total_productos = len(self.carrito)
                if total_productos > self.max_productos_visibles:
                    max_scroll = max(0, total_productos - self.max_productos_visibles)
                    self.scroll_offset_carrito -= int(event.y)
                    self.scroll_offset_carrito = max(0, min(self.scroll_offset_carrito, max_scroll))
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                # Resetear delay de eliminación si se suelta el botón
                self.product_to_delete = None
                self.delete_start_time = None



    def update(self):
        # Manejar delay para eliminación de productos
        if self.product_to_delete is not None and self.delete_start_time is not None:
            current_time = pygame.time.get_ticks()
            if current_time - self.delete_start_time >= self.delete_delay:
                self.carrito.pop(self.product_to_delete)
                self.product_to_delete = None
                self.delete_start_time = None

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

        # Si está abierto, dibujar las opciones con scroll
        if self.abierto:
            # Calcular cuántas opciones mostrar
            total_opciones = len(self.opciones)
            opciones_a_mostrar = min(self.max_opciones_visibles, total_opciones - self.scroll_offset)
            
            # Asegurar que scroll_offset no sea negativo ni mayor que el máximo
            max_scroll = max(0, total_opciones - self.max_opciones_visibles)
            self.scroll_offset = max(0, min(self.scroll_offset, max_scroll))
            
            # Dibujar solo las opciones visibles
            for i in range(opciones_a_mostrar):
                indice_real = i + self.scroll_offset
                if indice_real >= total_opciones:
                    break
                    
                opcion = self.opciones[indice_real]
                rect_opcion = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.h, self.rect.w, self.rect.h)
                
                # Efecto hover en las opciones
                mouse_pos = pygame.mouse.get_pos()
                color = self.color_hover if rect_opcion.collidepoint(mouse_pos) else (255, 255, 255)
                
                pygame.draw.rect(surface, color, rect_opcion)
                pygame.draw.rect(surface, (0, 0, 0), rect_opcion, 1) # Borde fino
                
                txt_opcion = FONT_SMALL.render(opcion, True, (0, 0, 0))
                surface.blit(txt_opcion, (rect_opcion.x + 5, rect_opcion.y + 5))
            
            # Dibujar barra de scroll si hay más opciones de las visibles
            if total_opciones > self.max_opciones_visibles:
                scroll_area_height = self.max_opciones_visibles * self.rect.h
                scroll_bar_x = self.rect.x + self.rect.w - 15
                scroll_bar_y = self.rect.y + self.rect.h
                scroll_bar_width = 12
                
                # Fondo de la barra de scroll
                pygame.draw.rect(surface, (220, 220, 220), 
                               (scroll_bar_x, scroll_bar_y, scroll_bar_width, scroll_area_height))
                
                # Calcular posición y tamaño del thumb (barra deslizante)
                thumb_height = max(20, int(scroll_area_height * (self.max_opciones_visibles / total_opciones)))
                thumb_y_range = scroll_area_height - thumb_height
                thumb_y = scroll_bar_y + int(thumb_y_range * (self.scroll_offset / max(1, max_scroll)))
                
                # Dibujar thumb
                pygame.draw.rect(surface, (100, 100, 100), 
                               (scroll_bar_x, thumb_y, scroll_bar_width, thumb_height))
                pygame.draw.rect(surface, (0, 0, 0), 
                               (scroll_bar_x, thumb_y, scroll_bar_width, thumb_height), 1)

                

        # Botón de salida
        pygame.draw.rect(surface, RED, self.exit_button)
        exit_button_txt = FONT_MEDIUM.render('Volver', True, (WHITE))
        exit_txt_rect = exit_button_txt.get_rect(center=self.exit_button.center)
        surface.blit(exit_button_txt, exit_txt_rect)
        
        #boton fiar
        pygame.draw.rect(surface, ORANGE, self.fiar_button)
        fiar_btn_txt = FONT_MEDIUM.render('Fiar', True, (WHITE))
        fiar_btn_rect = fiar_btn_txt.get_rect(center=self.fiar_button.center)
        surface.blit(fiar_btn_txt, fiar_btn_rect)

        #boton de compra
        pygame.draw.rect(surface, BLUE, self.buy_button)
        buy_btn_txt = FONT_MEDIUM.render('Comprar', True, (WHITE))
        buy_btn_rect = buy_btn_txt.get_rect(center=self.buy_button.center)
        surface.blit(buy_btn_txt, buy_btn_rect)

        # Dibujar productos en el carrito con scroll si es necesario
        total_productos = len(self.carrito)
        if total_productos > 0:
            productos_a_mostrar = min(self.max_productos_visibles, total_productos - self.scroll_offset_carrito)
            for j in range(productos_a_mostrar):
                idx = j + self.scroll_offset_carrito
                if idx >= total_productos:
                    break
                producto = self.carrito[idx]
                producto_txt = FONT_SMALL.render(producto, True, (0, 0, 0))
                surface.blit(producto_txt, (self.carrito_rect.x + 10, self.carrito_rect.y + 10 + j * 30))
                
                # Símbolo de eliminación (X) al lado de cada producto visible
                eliminar_color = (255, 0, 0) if self.product_to_delete == idx else (255, 255, 255)  # Rojo si en delay
                eliminar_rect = pygame.Rect(self.carrito_rect.x + self.carrito_rect.w - 30, self.carrito_rect.y + 10 + j * 30, 20, 20)
                pygame.draw.rect(surface, eliminar_color, eliminar_rect)
                eliminar_txt = FONT_SMALL.render('X', True, (WHITE))
                eliminar_txt_rect = eliminar_txt.get_rect(center=eliminar_rect.center)
                surface.blit(eliminar_txt, eliminar_txt_rect)
                
                # Verificar clic en el botón de eliminación
                mouse_pos = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0] and eliminar_rect.collidepoint(mouse_pos):
                    if self.product_to_delete != idx:
                        self.product_to_delete = idx
                        self.delete_start_time = pygame.time.get_ticks()
                else:
                    if self.product_to_delete == idx:
                        self.product_to_delete = None
                        self.delete_start_time = None
            
            # Dibujar barra de scroll si hay más productos de los visibles
            if total_productos > self.max_productos_visibles:
                scroll_area_height = self.max_productos_visibles * 30
                scroll_bar_x = self.carrito_rect.x - 15  # Posición a la izquierda del carrito
                scroll_bar_y = self.carrito_rect.y + 10
                scroll_bar_width = 12
                
                # Fondo de la barra de scroll
                pygame.draw.rect(surface, (220, 220, 220), 
                               (scroll_bar_x, scroll_bar_y, scroll_bar_width, scroll_area_height))
                
                # Calcular posición y tamaño del thumb
                thumb_height = max(20, int(scroll_area_height * (self.max_productos_visibles / total_productos)))
                thumb_y_range = scroll_area_height - thumb_height
                thumb_y = scroll_bar_y + int(thumb_y_range * (self.scroll_offset_carrito / max(1, total_productos - self.max_productos_visibles)))
                
                # Dibujar thumb
                pygame.draw.rect(surface, (100, 100, 100), 
                               (scroll_bar_x, thumb_y, scroll_bar_width, thumb_height))
                pygame.draw.rect(surface, (0, 0, 0), 
                               (scroll_bar_x, thumb_y, scroll_bar_width, thumb_height), 1)



    



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



