from numpy.char import center
import pygame, pygame_gui
from pathlib import Path
from ui.constants import *

class Splash():
    def __init__(self, app):
        self.app = app
        self.color = PURPLE
        self.button_start = pygame.Rect(0, 0, 0, 0)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.app.change_screen(Main_menu_screen(self.app))
        if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_start.collidepoint(event.pos):
                    self.app.change_screen(Main_menu_screen(self.app))

    def update(self):
        pass

    def draw(self, surface):
        global button_start
        surface.fill(self.color)

        
        path_logo_img = pygame.image.load(str(ruta_image))
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
        self.button_start = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 + 100, 200, 50)
        text_button_start = FONT_LARGE.render('Iniciar', True, WHITE)
        
        #correr botones
        pygame.draw.rect(surface, GREEN, self.button_start)
        txt_btn_start_rect = text_button_start.get_rect(center=self.button_start.center)
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
                if chinamo_button.collidepoint(event.pos):
                    self.app.change_screen(Chinamo_screen(self.app))
                if history_button.collidepoint(event.pos):
                    self.app.change_screen(History_screen(self.app))
                if credits_button.collidepoint(event.pos):
                    self.app.change_screen(Credits_screen(self.app))
    def update(self):
        pass

    def draw(self, surface):
        global exit_button
        global sell_button
        global chinamo_button
        global history_button
        global credits_button
        surface.fill(self.color)

        #dibujar titulo ventana de principal
        title_text = FONT_TITLE.render('Menu de gestión', True, (WHITE))
        surface.blit(title_text, (self.cor_x, self.cor_y))

        #crear serie de botones
        sell_button = pygame.Rect(self.cor_x + 50, self.cor_y + 90, 200, 50)
        chinamo_button = pygame.Rect(self.cor_x + 50, self.cor_y + 160, 200, 50)
        history_button = pygame.Rect(self.cor_x + 50, self.cor_y + 230, 200, 50)
        credits_button = pygame.Rect(self.cor_x + 50, self.cor_y + 300, 200, 50)
        exit_button = pygame.Rect(self.cor_x + 50, self.cor_y + 370, 200, 50)

        #dibujar botones
        pygame.draw.rect(surface, GREEN, sell_button)
        pygame.draw.rect(surface, BLUE, chinamo_button)
        pygame.draw.rect(surface, ORANGE, history_button)
        pygame.draw.rect(surface, PURPLE, credits_button)
        pygame.draw.rect(surface, RED, exit_button)
        
        #crear texto botones
        sell_button_txt = FONT_MEDIUM.render('Ventas', True, (WHITE))
        chinamo_button_txt = FONT_MEDIUM.render('Chinamos', True, (WHITE))
        history_button_txt = FONT_MEDIUM.render('Historial', True, (WHITE)) 
        credits_button_txt = FONT_MEDIUM.render('Creditos', True, (WHITE))  
        exit_button_txt = FONT_MEDIUM.render('Salir', True, (WHITE))    


        #dibujar texto botones (centrado)
        sell_txt_rect = sell_button_txt.get_rect(center=sell_button.center)
        chinamo_txt_rect = chinamo_button_txt.get_rect(center=chinamo_button.center)
        history_txt_rect = history_button_txt.get_rect(center=history_button.center)
        credits_txt_rect = credits_button_txt.get_rect(center=credits_button.center)
        exit_txt_rect = exit_button_txt.get_rect(center=exit_button.center)

        surface.blit(sell_button_txt, sell_txt_rect)
        surface.blit(chinamo_button_txt, chinamo_txt_rect)
        surface.blit(history_button_txt, history_txt_rect)
        surface.blit(credits_button_txt, credits_txt_rect)
        surface.blit(exit_button_txt, exit_txt_rect)

class Chinamo_screen():
    def __init__(self, app):
        self.app = app
        self.color = CYAN
        self.title = 'Chinamos'
        self.selected_id = None
        self.showing_detail = False
        self.sidebar_items = []
        self.sidebar_delete_buttons = []
        self.product_delete_buttons = []
        self.back_button = pygame.Rect(20, HEIGHT - 70, 200, 50)
        self.list_panel_rect = pygame.Rect(380, 80, WIDTH - 400, HEIGHT - 160)
        self.detail_back_button = pygame.Rect(self.list_panel_rect.x + 20, self.list_panel_rect.y + 15, 120, 35)
        self.list_scroll_offset = 0
        self.list_item_height = 55
        self.list_item_gap = 10
        self.list_top_padding = 55
        self.ui_manager = pygame_gui.UIManager((WIDTH, HEIGHT))
        self.confirm_delete_target = None

        self.seller_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(40, 140, 280, 35), manager=self.ui_manager)
        self.create_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(40, 185, 280, 35), text='Crear Chinamo', manager=self.ui_manager)

        self.rename_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(40, 260, 280, 35), manager=self.ui_manager)
        self.rename_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(40, 305, 280, 35), text='Actualizar nombre', manager=self.ui_manager)

        self.product_name_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(40, 370, 170, 35), manager=self.ui_manager)
        self.product_price_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(220, 370, 100, 35), manager=self.ui_manager)
        self.add_product_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(40, 415, 280, 35), text='Agregar producto', manager=self.ui_manager)

    def handle_event(self, event):
        if self.confirm_delete_target:
            if event.type == pygame.KEYDOWN:
                key_text = event.unicode.lower() if event.unicode else ''
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_n or key_text == 'n':
                    self.confirm_delete_target = None
                    return
                if event.key == pygame.K_y or key_text in ('y', 's'):
                    target = self.confirm_delete_target
                    self.confirm_delete_target = None
                    if target['type'] == 'chinamo':
                        removed = self.app.fair_manager.remove_chinamo(target['chinamo_id'])
                        if removed:
                            if self.selected_id == target['chinamo_id']:
                                self.selected_id = None
                                self.showing_detail = False
                            self.app.fair_manager.save_data()
                    elif target['type'] == 'product' and self.selected_id:
                        removed = self.app.fair_manager.remove_product_from_chinamo(
                            self.selected_id,
                            target['product_index']
                        )
                        if removed:
                            self.app.fair_manager.save_data()
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return

        self.ui_manager.process_events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.change_screen(Main_menu_screen(self.app))
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.create_button:
                seller_name = self.seller_input.get_text().strip()
                if seller_name:
                    self.app.fair_manager.create_chinamo(seller_name)
                    self.seller_input.set_text('')
                    self.app.fair_manager.save_data()
            elif event.ui_element == self.rename_button:
                if self.selected_id:
                    new_name = self.rename_input.get_text().strip()
                    if new_name:
                        chinamo = self.app.fair_manager.chinamos[self.selected_id]
                        chinamo.update_seller_name(new_name)
                        self.rename_input.set_text('')
                        self.app.fair_manager.save_data()
            elif event.ui_element == self.add_product_button:
                if self.selected_id:
                    product_name = self.product_name_input.get_text().strip()
                    price_text = self.product_price_input.get_text().strip()
                    try:
                        price = float(price_text)
                    except ValueError:
                        price = None
                    if product_name and price is not None and price >= 0:
                        chinamo = self.app.fair_manager.chinamos[self.selected_id]
                        chinamo.add_product(product_name, price)
                        self.product_name_input.set_text('')
                        self.product_price_input.set_text('')
                        self.app.fair_manager.save_data()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.back_button.collidepoint(event.pos):
                    self.app.change_screen(Main_menu_screen(self.app))
                elif self.showing_detail and self.detail_back_button.collidepoint(event.pos):
                    self.showing_detail = False
                elif not self.showing_detail:
                    for chinamo_id, delete_rect in self.sidebar_delete_buttons:
                        if delete_rect.collidepoint(event.pos):
                            self.confirm_delete_target = {
                                'type': 'chinamo',
                                'chinamo_id': chinamo_id
                            }
                            return
                    for chinamo_id, rect in self.sidebar_items:
                        if rect.collidepoint(event.pos):
                            self.selected_id = chinamo_id
                            self.showing_detail = True
                            break
                elif self.showing_detail and self.selected_id:
                    for product_index, delete_rect in self.product_delete_buttons:
                        if delete_rect.collidepoint(event.pos):
                            self.confirm_delete_target = {
                                'type': 'product',
                                'product_index': product_index
                            }
                            return
        elif event.type == pygame.MOUSEWHEEL:
            if not self.showing_detail and self.list_panel_rect.collidepoint(pygame.mouse.get_pos()):
                total_chinamos = len(self.app.fair_manager.chinamos)
                visible_slots = self._get_visible_list_slots()
                max_scroll = max(0, total_chinamos - visible_slots)
                self.list_scroll_offset -= int(event.y)
                self.list_scroll_offset = max(0, min(self.list_scroll_offset, max_scroll))

    def update(self):
        self.ui_manager.update(0.016)
        total_chinamos = len(self.app.fair_manager.chinamos)
        visible_slots = self._get_visible_list_slots()
        max_scroll = max(0, total_chinamos - visible_slots)
        self.list_scroll_offset = max(0, min(self.list_scroll_offset, max_scroll))

        if self.selected_id and self.selected_id not in self.app.fair_manager.chinamos:
            self.selected_id = None
            self.showing_detail = False

    def _get_visible_list_slots(self):
        available_height = self.list_panel_rect.h - self.list_top_padding - 20
        row_size = self.list_item_height + self.list_item_gap
        return max(1, available_height // row_size)

    def draw(self, surface):
        surface.fill(self.color)

        title_text = FONT_TITLE.render(self.title, True, WHITE)
        surface.blit(title_text, (20, 20))

        create_rect = pygame.Rect(20, 80, 340, HEIGHT - 160)
        pygame.draw.rect(surface, LIGHT_GRAY, create_rect)
        pygame.draw.rect(surface, BLACK, create_rect, 2)

        create_title = FONT_MEDIUM.render('Crear y editar', True, BLACK)
        surface.blit(create_title, (create_rect.x + 20, create_rect.y + 20))

        seller_label = FONT_SMALL.render('Nombre del Vendedor:', True, BLACK)
        surface.blit(seller_label, (create_rect.x + 20, create_rect.y + 115))

        rename_label = FONT_SMALL.render('Renombrar vendedor:', True, BLACK)
        surface.blit(rename_label, (create_rect.x + 20, create_rect.y + 235))

        product_label = FONT_SMALL.render('Agregar producto:', True, BLACK)
        surface.blit(product_label, (create_rect.x + 20, create_rect.y + 345))

        price_label = FONT_SMALL.render('Precio:', True, BLACK)
        surface.blit(price_label, (create_rect.x + 220, create_rect.y + 345))

        detail_rect = self.list_panel_rect
        pygame.draw.rect(surface, LIGHT_GRAY, detail_rect)
        pygame.draw.rect(surface, BLACK, detail_rect, 2)

        self.sidebar_items = []
        self.sidebar_delete_buttons = []
        self.product_delete_buttons = []
        if not self.showing_detail:
            list_title = FONT_MEDIUM.render('Lista de chinamos', True, BLACK)
            surface.blit(list_title, (detail_rect.x + 20, detail_rect.y + 15))

            chinamos_items = list(self.app.fair_manager.chinamos.items())
            visible_slots = self._get_visible_list_slots()
            visible_items = chinamos_items[self.list_scroll_offset:self.list_scroll_offset + visible_slots]

            y = detail_rect.y + self.list_top_padding
            for chinamo_id, chinamo in visible_items:
                item_rect = pygame.Rect(detail_rect.x + 10, y, detail_rect.w - 20, self.list_item_height)
                color = (180, 220, 255) if chinamo_id == self.selected_id else WHITE
                pygame.draw.rect(surface, color, item_rect)
                pygame.draw.rect(surface, BLACK, item_rect, 1)

                label = FONT_MEDIUM.render(f'{chinamo_id} - {chinamo.seller_name}', True, BLACK)
                surface.blit(label, (item_rect.x + 10, item_rect.y + 13))
                self.sidebar_items.append((chinamo_id, item_rect))

                delete_rect = pygame.Rect(item_rect.right - 34, item_rect.y + 10, 24, 24)
                pygame.draw.rect(surface, RED, delete_rect)
                delete_text = FONT_SMALL.render('X', True, WHITE)
                delete_text_rect = delete_text.get_rect(center=delete_rect.center)
                surface.blit(delete_text, delete_text_rect)
                self.sidebar_delete_buttons.append((chinamo_id, delete_rect))
                y += self.list_item_height + self.list_item_gap

            if len(chinamos_items) > visible_slots:
                scroll_track = pygame.Rect(detail_rect.right - 12, detail_rect.y + self.list_top_padding, 8, detail_rect.h - self.list_top_padding - 20)
                pygame.draw.rect(surface, (220, 220, 220), scroll_track)

                max_scroll = len(chinamos_items) - visible_slots
                thumb_h = max(24, int(scroll_track.h * (visible_slots / len(chinamos_items))))
                thumb_range = scroll_track.h - thumb_h
                thumb_y = scroll_track.y + int(thumb_range * (self.list_scroll_offset / max_scroll))
                thumb = pygame.Rect(scroll_track.x, thumb_y, scroll_track.w, thumb_h)
                pygame.draw.rect(surface, (120, 120, 120), thumb)
                pygame.draw.rect(surface, BLACK, thumb, 1)

            if not chinamos_items:
                empty_text = FONT_MEDIUM.render('No hay chinamos registrados.', True, BLACK)
                surface.blit(empty_text, (detail_rect.x + 20, detail_rect.y + 70))

        elif self.selected_id and self.selected_id in self.app.fair_manager.chinamos:
            pygame.draw.rect(surface, BLUE, self.detail_back_button)
            detail_back_text = FONT_SMALL.render('< Volver a lista', True, WHITE)
            detail_back_rect = detail_back_text.get_rect(center=self.detail_back_button.center)
            surface.blit(detail_back_text, detail_back_rect)

            chinamo = self.app.fair_manager.chinamos[self.selected_id]
            stats = self.app.fair_manager.get_chinamo_stats(self.selected_id)
            detail_title = FONT_TITLE.render('Detalle del Chinamo', True, BLACK)
            surface.blit(detail_title, (detail_rect.x + 20, detail_rect.y + 55))

            detail_lines = [
                f'ID: {self.selected_id}',
                f'Vendedor: {chinamo.seller_name}',
                f'Total ventas: {stats["total"]}',
                f'Total fiados: {stats["fiados"]}',
                f'Total comprado: {stats["bought"]}'
            ]
            line_y = detail_rect.y + 120
            for text in detail_lines:
                line_surf = FONT_MEDIUM.render(text, True, BLACK)
                surface.blit(line_surf, (detail_rect.x + 20, line_y))
                line_y += 35

            products = chinamo.products.get(self.selected_id, {}).get('products', [])
            products_title = FONT_MEDIUM.render('Productos disponibles:', True, BLACK)
            surface.blit(products_title, (detail_rect.x + 20, line_y + 10))
            line_y += 40
            if products:
                for index, product in enumerate(products[:8]):
                    product_text = f'- {product["name"]} (${product["price_product"]})'
                    product_surf = FONT_SMALL.render(product_text, True, BLACK)
                    surface.blit(product_surf, (detail_rect.x + 30, line_y))

                    delete_rect = pygame.Rect(detail_rect.right - 42, line_y - 2, 24, 24)
                    pygame.draw.rect(surface, RED, delete_rect)
                    delete_text = FONT_SMALL.render('X', True, WHITE)
                    delete_text_rect = delete_text.get_rect(center=delete_rect.center)
                    surface.blit(delete_text, delete_text_rect)
                    self.product_delete_buttons.append((index, delete_rect))
                    line_y += 25
                    if line_y > detail_rect.y + detail_rect.h - 40:
                        break
            else:
                no_products = FONT_SMALL.render('Sin productos registrados.', True, BLACK)
                surface.blit(no_products, (detail_rect.x + 20, line_y))
                line_y += 30

            sales = [sale for sale in self.app.fair_manager.sales if sale.chinamo_id == self.selected_id]
            sales_title = FONT_MEDIUM.render('Ventas recientes:', True, BLACK)
            surface.blit(sales_title, (detail_rect.x + 20, line_y + 10))
            line_y += 40
            for sale in sales[-5:]:
                sale_text = f'{sale.timestamp} | {sale.sale_type} | {sale.total}'
                sale_surf = FONT_SMALL.render(sale_text, True, BLACK)
                surface.blit(sale_surf, (detail_rect.x + 20, line_y))
                line_y += 30
                if line_y > detail_rect.y + detail_rect.h - 40:
                    break
        else:
            fallback_text = FONT_MEDIUM.render('Selecciona un chinamo desde la lista.', True, BLACK)
            surface.blit(fallback_text, (detail_rect.x + 20, detail_rect.y + 70))

        pygame.draw.rect(surface, RED, self.back_button)
        back_text = FONT_MEDIUM.render('Volver', True, WHITE)
        back_rect = back_text.get_rect(center=self.back_button.center)
        surface.blit(back_text, back_rect)

        if self.confirm_delete_target:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 170))
            surface.blit(overlay, (0, 0))
            modal = pygame.Rect(WIDTH // 2 - 250, HEIGHT // 2 - 85, 500, 170)
            pygame.draw.rect(surface, LIGHT_GRAY, modal)
            pygame.draw.rect(surface, BLACK, modal, 2)
            l1 = FONT_MEDIUM.render('Seguro que quieres eliminar este dato?', True, BLACK)
            l2 = FONT_SMALL.render('Si lo eliminas, los datos se perderan.', True, BLACK)
            l3 = FONT_SMALL.render('Y = Si, N = No (o ESC)', True, BLACK)
            surface.blit(l1, (modal.x + 20, modal.y + 40))
            surface.blit(l2, (modal.x + 20, modal.y + 80))
            surface.blit(l3, (modal.x + 20, modal.y + 110))

        self.ui_manager.draw_ui(surface)


class Buy_screen():
    def __init__(self, app):
        self.app = app
        self.color = GREEN
        self.cor_x = 250
        self.cor_y = 20
        self.exit_button = pygame.Rect(20, HEIGHT - 70, 200, 50)
        self.fiar_button = pygame.Rect(WIDTH - 440, HEIGHT - 70, 200, 50)
        self.buy_button = pygame.Rect(WIDTH - 220, HEIGHT - 70, 200, 50)

        self.products_rect = pygame.Rect(20, 80, WIDTH - 410, HEIGHT - 170)
        self.carrito_rect = pygame.Rect(WIDTH - 380, 80, 350, HEIGHT - 170)

        self.product_row_h = 50
        self.cart_row_h = 36
        self.product_scroll = 0
        self.cart_scroll = 0

        self.product_click_areas = []
        self.cart_delete_areas = []
        self.carrito = []

        self.confirmation_msj = ''
        self.confirmation_time = 0
        self.asking_debtor_name = False
        self.debtor_name_input = ''
        self.confirm_existing_name = False
        self.asking_payment_method = False
        self.asking_sinpe_name = False
        self.sinpe_name_input = ''

    def _get_available_products(self):
        products = []
        for chinamo_id, chinamo_data in self.app.fair_manager.chinamos.items():
            product_items = chinamo_data.products.get(chinamo_id, {}).get('products', [])
            seller_name = chinamo_data.seller_name
            for product in product_items:
                products.append({
                    'chinamo_id': chinamo_id,
                    'seller': seller_name,
                    'name': product['name'],
                    'price': float(product['price_product'])
                })
        return products

    def _add_to_cart(self, product_data):
        for item in self.carrito:
            if item['chinamo_id'] == product_data['chinamo_id'] and item['name'] == product_data['name']:
                item['qty'] += 1
                return
        self.carrito.append({
            'chinamo_id': product_data['chinamo_id'],
            'seller': product_data['seller'],
            'name': product_data['name'],
            'unit_price': product_data['price'],
            'qty': 1
        })

    def _register_sale(self, sale_type, debtor_name=None, allow_existing_fiado=False, payment_method='efectivo', payer_name=None):
        if not self.carrito:
            self.confirmation_msj = 'El carrito está vacío.'
            self.confirmation_time = pygame.time.get_ticks()
            return

        grouped_items = {}
        for item in self.carrito:
            chinamo_id = item['chinamo_id']
            grouped_items.setdefault(chinamo_id, [])
            grouped_items[chinamo_id].append({
                'name': item['name'],
                'qty': item['qty'],
                'unit_price': item['unit_price']
            })

        for chinamo_id, items in grouped_items.items():
            sale = self.app.fair_manager.register_sale(chinamo_id, items)
            sale.categorize_sale(
                sale_type,
                debtor_name=debtor_name,
                payment_method=payment_method,
                payer_name=payer_name
            )
        if sale_type == 'fiado':
            fiado_items = []
            for item in self.carrito:
                fiado_items.append({
                    'chinamo_id': item['chinamo_id'],
                    'name': item['name'],
                    'qty': item['qty'],
                    'unit_price': item['unit_price']
                })
            self.app.fair_manager.add_fiado(
                debtor_name,
                fiado_items,
                allow_existing=allow_existing_fiado
            )

        self.app.fair_manager.save_data()
        self.carrito = []
        self.cart_scroll = 0
        action = 'fiada' if sale_type == 'fiado' else 'registrada'
        self.confirmation_msj = f'Venta {action} correctamente.'
        self.confirmation_time = pygame.time.get_ticks()

    def handle_event(self, event):
        if self.confirm_existing_name:
            if event.type == pygame.KEYDOWN:
                key_text = event.unicode.lower() if event.unicode else ''
                if event.key == pygame.K_ESCAPE:
                    self.confirm_existing_name = False
                    return
                if event.key == pygame.K_y or key_text in ('y', 's'):
                    debtor_name = self.debtor_name_input.strip()
                    self.confirm_existing_name = False
                    self.asking_debtor_name = False
                    self._register_sale('fiado', debtor_name=debtor_name, allow_existing_fiado=True)
                    self.debtor_name_input = ''
                    return
                if event.key == pygame.K_n or key_text == 'n':
                    self.confirm_existing_name = False
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return
        elif self.asking_payment_method:
            if event.type == pygame.KEYDOWN:
                key_text = event.unicode.lower() if event.unicode else ''
                if event.key == pygame.K_ESCAPE:
                    self.asking_payment_method = False
                    return
                if event.key == pygame.K_1 or key_text == 'e':
                    self.asking_payment_method = False
                    self._register_sale('bought', payment_method='efectivo')
                    return
                if event.key == pygame.K_2 or key_text == 's':
                    self.asking_payment_method = False
                    self.asking_sinpe_name = True
                    self.sinpe_name_input = ''
                    return #l
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return
        elif self.asking_sinpe_name:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.asking_sinpe_name = False
                    self.sinpe_name_input = ''
                    return
                if event.key == pygame.K_RETURN:
                    payer_name = self.sinpe_name_input.strip()
                    if not payer_name:
                        self.confirmation_msj = 'Debes ingresar nombre para pago por sinpe.'
                        self.confirmation_time = pygame.time.get_ticks()
                        return
                    self.asking_sinpe_name = False
                    self._register_sale('bought', payment_method='sinpe', payer_name=payer_name)
                    self.sinpe_name_input = ''
                    return
                if event.key == pygame.K_BACKSPACE:
                    self.sinpe_name_input = self.sinpe_name_input[:-1]
                    return
                if event.unicode and event.unicode.isprintable():
                    self.sinpe_name_input += event.unicode
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return
        elif self.asking_debtor_name:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.asking_debtor_name = False
                    self.debtor_name_input = ''
                    return
                if event.key == pygame.K_RETURN:
                    debtor_name = self.debtor_name_input.strip()
                    if not debtor_name:
                        self.confirmation_msj = 'Debes ingresar nombre para fiar.'
                        self.confirmation_time = pygame.time.get_ticks()
                        return
                    if self.app.fair_manager.debtor_name_exists(debtor_name):
                        self.confirm_existing_name = True
                        return
                    self.asking_debtor_name = False
                    self._register_sale('fiado', debtor_name=debtor_name)
                    self.debtor_name_input = ''
                    return
                if event.key == pygame.K_BACKSPACE:
                    self.debtor_name_input = self.debtor_name_input[:-1]
                    return
                if event.unicode and event.unicode.isprintable():
                    self.debtor_name_input += event.unicode
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.app.change_screen(Main_menu_screen(self.app))

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.exit_button.collidepoint(event.pos):
                self.app.change_screen(Main_menu_screen(self.app))
                return
            if self.fiar_button.collidepoint(event.pos):
                if not self.carrito:
                    self.confirmation_msj = 'El carrito está vacío.'
                    self.confirmation_time = pygame.time.get_ticks()
                    return
                self.asking_debtor_name = True
                self.debtor_name_input = ''
                return
            if self.buy_button.collidepoint(event.pos):
                if not self.carrito:
                    self.confirmation_msj = 'El carrito está vacío.'
                    self.confirmation_time = pygame.time.get_ticks()
                    return
                self.asking_payment_method = True
                return

            for product_data, rect in self.product_click_areas:
                if rect.collidepoint(event.pos):
                    self._add_to_cart(product_data)
                    return

            for index, rect in self.cart_delete_areas:
                if rect.collidepoint(event.pos):
                    self.carrito.pop(index)
                    return

        elif event.type == pygame.MOUSEWHEEL:
            available_products = self._get_available_products()
            products_visible = max(1, (self.products_rect.h - 20) // self.product_row_h)
            max_product_scroll = max(0, len(available_products) - products_visible)
            max_cart_scroll = max(0, len(self.carrito) - max(1, (self.carrito_rect.h - 20) // self.cart_row_h))

            mouse_pos = pygame.mouse.get_pos()
            if self.products_rect.collidepoint(mouse_pos):
                self.product_scroll -= int(event.y)
                self.product_scroll = max(0, min(self.product_scroll, max_product_scroll))
            elif self.carrito_rect.collidepoint(mouse_pos):
                self.cart_scroll -= int(event.y)
                self.cart_scroll = max(0, min(self.cart_scroll, max_cart_scroll))

    def update(self):
        if self.confirmation_msj and pygame.time.get_ticks() - self.confirmation_time > 2500:
            self.confirmation_msj = ''

    def draw(self, surface):
        surface.fill(self.color)
        title_text = FONT_TITLE.render('Pantalla de Ventas', True, WHITE)
        surface.blit(title_text, (self.cor_x, self.cor_y))

        pygame.draw.rect(surface, LIGHT_GRAY, self.products_rect)
        pygame.draw.rect(surface, BLACK, self.products_rect, 2)
        products_title = FONT_MEDIUM.render('Productos disponibles ', True, BLACK)
        surface.blit(products_title, (self.products_rect.x + 12, self.products_rect.y + 8))

        pygame.draw.rect(surface, LIGHT_GRAY, self.carrito_rect)
        pygame.draw.rect(surface, BLACK, self.carrito_rect, 2)
        carrito_titulo = FONT_MEDIUM.render('Carrito', True, BLACK)
        surface.blit(carrito_titulo, (self.carrito_rect.x + 12, self.carrito_rect.y + 8))

        available_products = self._get_available_products()
        products_visible = max(1, (self.products_rect.h - 45) // self.product_row_h)
        self.product_scroll = max(0, min(self.product_scroll, max(0, len(available_products) - products_visible)))
        visible_products = available_products[self.product_scroll:self.product_scroll + products_visible]

        self.product_click_areas = []
        y = self.products_rect.y + 40
        for product in visible_products:
            row_rect = pygame.Rect(self.products_rect.x + 8, y, self.products_rect.w - 16, self.product_row_h - 6)
            row_color = (230, 245, 230) if row_rect.collidepoint(pygame.mouse.get_pos()) else WHITE
            pygame.draw.rect(surface, row_color, row_rect)
            pygame.draw.rect(surface, BLACK, row_rect, 1)

            name_text = FONT_MEDIUM.render(f'{product["name"]}  -  ${product["price"]}', True, BLACK)
            meta_text = FONT_SMALL.render(f'{product["seller"]} | {product["chinamo_id"]}', True, (90, 90, 90))
            surface.blit(name_text, (row_rect.x + 10, row_rect.y + 6))
            surface.blit(meta_text, (row_rect.x + 10, row_rect.y + 28))

            self.product_click_areas.append((product, row_rect))
            y += self.product_row_h

        if not available_products:
            empty_text = FONT_MEDIUM.render('No hay productos registrados \n en los chinamos.', True, BLACK)
            surface.blit(empty_text, (self.products_rect.x + 12, self.products_rect.y + 55))

        cart_visible = max(1, (self.carrito_rect.h - 45) // self.cart_row_h)
        self.cart_scroll = max(0, min(self.cart_scroll, max(0, len(self.carrito) - cart_visible)))
        visible_cart = self.carrito[self.cart_scroll:self.cart_scroll + cart_visible]
        self.cart_delete_areas = []

        cart_y = self.carrito_rect.y + 40
        for offset, item in enumerate(visible_cart):
            row_rect = pygame.Rect(self.carrito_rect.x + 8, cart_y, self.carrito_rect.w - 16, self.cart_row_h - 4)
            pygame.draw.rect(surface, WHITE, row_rect)
            pygame.draw.rect(surface, BLACK, row_rect, 1)

            total_line = item['qty'] * item['unit_price']
            text = FONT_SMALL.render(
                f'{item["qty"]}x {item["name"]} (${item["unit_price"]})',
                True,
                BLACK
            )
            meta = FONT_SMALL.render(f'{item["chinamo_id"]}  Total:${total_line}', True, (90, 90, 90))
            surface.blit(text, (row_rect.x + 6, row_rect.y + 2))
            surface.blit(meta, (row_rect.x + 6, row_rect.y + 18))

            delete_rect = pygame.Rect(row_rect.right - 22, row_rect.y + 7, 16, 16)
            pygame.draw.rect(surface, RED, delete_rect)
            delete_txt = FONT_SMALL.render('X', True, WHITE)
            surface.blit(delete_txt, delete_txt.get_rect(center=delete_rect.center))
            self.cart_delete_areas.append((self.cart_scroll + offset, delete_rect))
            cart_y += self.cart_row_h

        if self.confirmation_msj:
            confirmation = FONT_MEDIUM.render(self.confirmation_msj, True, RED)
            surface.blit(confirmation, (30, HEIGHT - 150))

        pygame.draw.rect(surface, RED, self.exit_button)
        exit_button_txt = FONT_MEDIUM.render('Volver', True, WHITE)
        surface.blit(exit_button_txt, exit_button_txt.get_rect(center=self.exit_button.center))

        pygame.draw.rect(surface, ORANGE, self.fiar_button)
        fiar_btn_txt = FONT_MEDIUM.render('Fiar', True, WHITE)
        surface.blit(fiar_btn_txt, fiar_btn_txt.get_rect(center=self.fiar_button.center))

        pygame.draw.rect(surface, BLUE, self.buy_button)
        buy_btn_txt = FONT_MEDIUM.render('Comprar', True, WHITE)
        surface.blit(buy_btn_txt, buy_btn_txt.get_rect(center=self.buy_button.center))

        if self.asking_debtor_name:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            surface.blit(overlay, (0, 0))

            modal_rect = pygame.Rect(WIDTH // 2 - 220, HEIGHT // 2 - 90, 440, 180)
            pygame.draw.rect(surface, LIGHT_GRAY, modal_rect)
            pygame.draw.rect(surface, BLACK, modal_rect, 2)

            title = FONT_MEDIUM.render('Nombre para fiado (obligatorio)', True, BLACK)
            surface.blit(title, (modal_rect.x + 20, modal_rect.y + 20))

            input_rect = pygame.Rect(modal_rect.x + 20, modal_rect.y + 65, modal_rect.w - 40, 40)
            pygame.draw.rect(surface, WHITE, input_rect)
            pygame.draw.rect(surface, BLACK, input_rect, 2)

            typed_text = FONT_MEDIUM.render(self.debtor_name_input, True, BLACK)
            surface.blit(typed_text, (input_rect.x + 10, input_rect.y + 8))

            help_text = FONT_SMALL.render('ENTER para confirmar | ESC para cancelar', True, BLACK)
            surface.blit(help_text, (modal_rect.x + 20, modal_rect.y + 125))

        if self.confirm_existing_name:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 170))
            surface.blit(overlay, (0, 0))

            confirm_rect = pygame.Rect(WIDTH // 2 - 260, HEIGHT // 2 - 85, 520, 170)
            pygame.draw.rect(surface, LIGHT_GRAY, confirm_rect)
            pygame.draw.rect(surface, BLACK, confirm_rect, 2)
            line1 = FONT_SMALL.render('Ese nombre ya existe.', True, BLACK)
            line2 = FONT_SMALL.render('Seguro que quieres agregar este fiado a la misma persona?', True, BLACK)
            line3 = FONT_SMALL.render('Presiona Y = Si, N = No', True, BLACK)
            surface.blit(line1, (confirm_rect.x + 20, confirm_rect.y + 35))
            surface.blit(line2, (confirm_rect.x + 20, confirm_rect.y + 65))
            surface.blit(line3, (confirm_rect.x + 20, confirm_rect.y + 105))

        if self.asking_payment_method:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 170))
            surface.blit(overlay, (0, 0))
            modal_rect = pygame.Rect(WIDTH // 2 - 240, HEIGHT // 2 - 100, 480, 190)
            pygame.draw.rect(surface, LIGHT_GRAY, modal_rect)
            pygame.draw.rect(surface, BLACK, modal_rect, 2)
            title = FONT_MEDIUM.render('Selecciona metodo de pago para compra', True, BLACK)
            info1 = FONT_SMALL.render('1 o E: Efectivo', True, BLACK)
            info2 = FONT_SMALL.render('2 o S: Sinpe', True, BLACK)
            info3 = FONT_SMALL.render('ESC: Cancelar', True, BLACK)
            surface.blit(title, (modal_rect.x + 20, modal_rect.y + 28))
            surface.blit(info1, (modal_rect.x + 20, modal_rect.y + 80))
            surface.blit(info2, (modal_rect.x + 20, modal_rect.y + 110))
            surface.blit(info3, (modal_rect.x + 20, modal_rect.y + 140))

        if self.asking_sinpe_name:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 170))
            surface.blit(overlay, (0, 0))
            modal_rect = pygame.Rect(WIDTH // 2 - 250, HEIGHT // 2 - 90, 500, 180)
            pygame.draw.rect(surface, LIGHT_GRAY, modal_rect)
            pygame.draw.rect(surface, BLACK, modal_rect, 2)
            title = FONT_MEDIUM.render('Nombre del titular de sinpe (obligatorio)', True, BLACK)
            surface.blit(title, (modal_rect.x + 20, modal_rect.y + 20))
            input_rect = pygame.Rect(modal_rect.x + 20, modal_rect.y + 65, modal_rect.w - 40, 40)
            pygame.draw.rect(surface, WHITE, input_rect)
            pygame.draw.rect(surface, BLACK, input_rect, 2)
            typed_text = FONT_MEDIUM.render(self.sinpe_name_input, True, BLACK)
            surface.blit(typed_text, (input_rect.x + 10, input_rect.y + 8))
            help_text = FONT_SMALL.render('ENTER para confirmar | ESC para cancelar', True, BLACK)
            surface.blit(help_text, (modal_rect.x + 20, modal_rect.y + 125))



    



class History_screen():
    def __init__(self, app):
        self.app = app
        self.color = ORANGE
        self.cor_x = 200
        self.cor_y = 20
        self.back_button = pygame.Rect(20, HEIGHT - 70, 200, 50)
        self.return_button = pygame.Rect(20, 80, 180, 45)
        self.fiados_button = pygame.Rect(WIDTH // 2 - 150, 200, 300, 55)
        self.general_button = pygame.Rect(WIDTH // 2 - 150, 275, 300, 55)
        self.sales_button = pygame.Rect(WIDTH // 2 - 150, 350, 300, 55)
        self.sinpe_button = pygame.Rect(WIDTH // 2 - 150, 425, 300, 55)
        self.list_rect = pygame.Rect(20, 140, 360, HEIGHT - 220)
        self.detail_rect = pygame.Rect(400, 80, WIDTH - 420, HEIGHT - 160)
        self.active_view = 'none'
        self.list_scroll = 0
        self.detail_scroll = 0
        self.selected_fiado_id = None
        self.fiado_click_areas = []
        self.paid_click_areas = []
        self.sales_scroll = 0
        self.sale_delete_areas = []
        self.confirm_delete_sale = False
        self.sale_to_delete = None

    def _get_sales_entries(self, sinpe_only=False):
        entries = []
        for idx, sale in enumerate(self.app.fair_manager.sales):
            payment_method = getattr(sale, 'payment_method', 'efectivo')
            if sinpe_only and payment_method != 'sinpe':
                continue
            entries.append((idx, sale))
        return entries

    def handle_event(self, event):
        if self.confirm_delete_sale:
            if event.type == pygame.KEYDOWN:
                key_text = event.unicode.lower() if event.unicode else ''
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_n or key_text == 'n':
                    self.confirm_delete_sale = False
                    self.sale_to_delete = None
                    return
                if event.key == pygame.K_y or key_text in ('y', 's'):
                    if self.sale_to_delete is not None:
                        self.app.fair_manager.remove_sale(self.sale_to_delete)
                        self.app.fair_manager.save_data()
                    self.confirm_delete_sale = False
                    self.sale_to_delete = None
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.change_screen(Main_menu_screen(self.app))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.back_button.collidepoint(event.pos):
                    self.app.change_screen(Main_menu_screen(self.app))
                    return
                if self.active_view != 'none' and self.return_button.collidepoint(event.pos):
                    self.active_view = 'none'
                    self.selected_fiado_id = None
                    self.detail_scroll = 0
                    self.sales_scroll = 0
                    return
                if self.active_view == 'none' and self.fiados_button.collidepoint(event.pos):
                    self.active_view = 'fiados'
                    self.list_scroll = 0
                    self.detail_scroll = 0
                    return
                if self.active_view == 'none' and self.general_button.collidepoint(event.pos):
                    self.active_view = 'general'
                    return
                if self.active_view == 'none' and self.sales_button.collidepoint(event.pos):
                    self.active_view = 'sales'
                    self.sales_scroll = 0
                    return
                if self.active_view == 'none' and self.sinpe_button.collidepoint(event.pos):
                    self.active_view = 'sinpe'
                    self.sales_scroll = 0
                    return
                if self.active_view == 'fiados':
                    for fiado_id, rect in self.fiado_click_areas:
                        if rect.collidepoint(event.pos):
                            self.selected_fiado_id = fiado_id
                            self.detail_scroll = 0
                            return

                    for fiado_id, item_index, rect in self.paid_click_areas:
                        if rect.collidepoint(event.pos):
                            if self.app.fair_manager.mark_fiado_item_paid(fiado_id, item_index):
                                self.app.fair_manager.save_data()
                                if self.selected_fiado_id == fiado_id:
                                    still_exists = any(
                                        entry.get('id') == fiado_id for entry in self.app.fair_manager.get_fiados()
                                    )
                                    if not still_exists:
                                        self.selected_fiado_id = None
                                        self.detail_scroll = 0
                            return
                elif self.active_view in ('sales', 'sinpe'):
                    for sale_index, rect in self.sale_delete_areas:
                        if rect.collidepoint(event.pos):
                            self.sale_to_delete = sale_index
                            self.confirm_delete_sale = True
                            return
                else:
                    return
        elif event.type == pygame.MOUSEWHEEL:
            mouse_pos = pygame.mouse.get_pos()
            if self.active_view == 'fiados' and self.list_rect.collidepoint(mouse_pos):
                fiados = self.app.fair_manager.get_fiados()
                visible_rows = max(1, (self.list_rect.h - 20) // 70)
                max_scroll = max(0, len(fiados) - visible_rows)
                self.list_scroll -= int(event.y)
                self.list_scroll = max(0, min(self.list_scroll, max_scroll))
            elif self.active_view == 'fiados' and self.detail_rect.collidepoint(mouse_pos) and self.selected_fiado_id:
                selected_entry = next(
                    (entry for entry in self.app.fair_manager.get_fiados() if entry.get('id') == self.selected_fiado_id),
                    None
                )
                if selected_entry:
                    visible_items = max(1, (self.detail_rect.h - 90) // 52)
                    max_scroll = max(0, len(selected_entry.get('items', [])) - visible_items)
                    self.detail_scroll -= int(event.y)
                    self.detail_scroll = max(0, min(self.detail_scroll, max_scroll))
            elif self.active_view in ('sales', 'sinpe'):
                sales_rect = pygame.Rect(20, 150, WIDTH - 40, HEIGHT - 240)
                if sales_rect.collidepoint(mouse_pos):
                    entries = self._get_sales_entries(sinpe_only=self.active_view == 'sinpe')
                    visible_rows = max(1, (sales_rect.h - 20) // 62)
                    max_scroll = max(0, len(entries) - visible_rows)
                    self.sales_scroll -= int(event.y)
                    self.sales_scroll = max(0, min(self.sales_scroll, max_scroll))

    def update(self):
        fiados = self.app.fair_manager.get_fiados()
        visible_rows = max(1, (self.list_rect.h - 20) // 70)
        self.list_scroll = max(0, min(self.list_scroll, max(0, len(fiados) - visible_rows)))
        if self.selected_fiado_id and not any(entry.get('id') == self.selected_fiado_id for entry in fiados):
            self.selected_fiado_id = None
            self.detail_scroll = 0

    def draw(self, surface):
        surface.fill(self.color)
        title_text = FONT_TITLE.render('Historial', True, WHITE)
        surface.blit(title_text, (self.cor_x, self.cor_y))
        if self.active_view == 'none':
            pygame.draw.rect(surface, BLUE, self.fiados_button)
            pygame.draw.rect(surface, BLUE, self.general_button)
            pygame.draw.rect(surface, BLUE, self.sales_button)
            pygame.draw.rect(surface, BLUE, self.sinpe_button)
            surface.blit(FONT_MEDIUM.render('Historial fiados', True, WHITE), FONT_MEDIUM.render('Historial fiados', True, WHITE).get_rect(center=self.fiados_button.center))
            surface.blit(FONT_MEDIUM.render('Historial general', True, WHITE), FONT_MEDIUM.render('Historial general', True, WHITE).get_rect(center=self.general_button.center))
            surface.blit(FONT_MEDIUM.render('Historial ventas', True, WHITE), FONT_MEDIUM.render('Historial ventas', True, WHITE).get_rect(center=self.sales_button.center))
            surface.blit(FONT_MEDIUM.render('Historial sinpes', True, WHITE), FONT_MEDIUM.render('Historial sinpes', True, WHITE).get_rect(center=self.sinpe_button.center))
            return
        else:
            pygame.draw.rect(surface, BLUE, self.return_button)
            return_text = FONT_MEDIUM.render('Regresar', True, WHITE)
            surface.blit(return_text, return_text.get_rect(center=self.return_button.center))

        if self.active_view == 'general':
            summary_rect = pygame.Rect(20, 150, WIDTH - 40, HEIGHT - 240)
            pygame.draw.rect(surface, LIGHT_GRAY, summary_rect)
            pygame.draw.rect(surface, BLACK, summary_rect, 2)

            total_fiados = self.app.fair_manager.get_total_fiados()
            total_bought = self.app.fair_manager.get_total_bought()
            total_sinpe = self.app.fair_manager.get_total_sinpe()
            total_global = total_fiados + total_bought
            top_chinamos = self.app.fair_manager.get_top_chinamos()

            card_w = (summary_rect.w - 65) // 4
            card_h = 100
            card_y = summary_rect.y + 20
            cards = [
                (pygame.Rect(summary_rect.x + 10, card_y, card_w, card_h), 'Total fiado', total_fiados, ORANGE),
                (pygame.Rect(summary_rect.x + 20 + card_w, card_y, card_w, card_h), 'Total comprado', total_bought, GREEN),
                (pygame.Rect(summary_rect.x + 30 + card_w * 2, card_y, card_w, card_h), 'Total sinpe', total_sinpe, PURPLE),
                (pygame.Rect(summary_rect.x + 40 + card_w * 3, card_y, card_w, card_h), 'Total general', total_global, BLUE)
            ]
            for card_rect, title, amount, color in cards:
                pygame.draw.rect(surface, color, card_rect)
                pygame.draw.rect(surface, BLACK, card_rect, 2)
                title_txt = FONT_SMALL.render(title, True, WHITE)
                value_txt = FONT_MEDIUM.render(f'${amount}', True, WHITE)
                surface.blit(title_txt, (card_rect.x + 10, card_rect.y + 15))
                surface.blit(value_txt, (card_rect.x + 10, card_rect.y + 55))

            top_rect = pygame.Rect(summary_rect.x + 10, summary_rect.y + 135, summary_rect.w - 20, summary_rect.h - 145)
            pygame.draw.rect(surface, WHITE, top_rect)
            pygame.draw.rect(surface, BLACK, top_rect, 1)
            top_title = FONT_MEDIUM.render('Top chinamos mas vendedores', True, BLACK)
            surface.blit(top_title, (top_rect.x + 10, top_rect.y + 10))

            if top_chinamos:
                y = top_rect.y + 45
                for pos, chinamo_id in enumerate(top_chinamos[:8], start=1):
                    chinamo = self.app.fair_manager.chinamos.get(chinamo_id)
                    seller_name = chinamo.seller_name if chinamo else 'Sin nombre'
                    stats = self.app.fair_manager.get_chinamo_stats(chinamo_id)
                    total = stats['total']
                    row = f'{pos}. {chinamo_id} - {seller_name} - ${total}'
                    row_txt = FONT_SMALL.render(row, True, BLACK)
                    surface.blit(row_txt, (top_rect.x + 10, y))
                    y += 30
                    if y > top_rect.bottom - 20:
                        break
            else:
                empty_top = FONT_MEDIUM.render('Aun no hay ventas registradas.', True, BLACK)
                surface.blit(empty_top, (top_rect.x + 10, top_rect.y + 50))

            pygame.draw.rect(surface, RED, self.back_button)
            back_text = FONT_MEDIUM.render('Volver', True, WHITE)
            surface.blit(back_text, back_text.get_rect(center=self.back_button.center))
            return

        if self.active_view in ('sales', 'sinpe'):
            sales_rect = pygame.Rect(20, 150, WIDTH - 40, HEIGHT - 240)
            pygame.draw.rect(surface, LIGHT_GRAY, sales_rect)
            pygame.draw.rect(surface, BLACK, sales_rect, 2)
            title = 'Historial de sinpes' if self.active_view == 'sinpe' else 'Historial de ventas'
            title_txt = FONT_MEDIUM.render(title, True, BLACK)
            surface.blit(title_txt, (sales_rect.x + 12, sales_rect.y + 10))

            entries = self._get_sales_entries(sinpe_only=self.active_view == 'sinpe')
            visible_rows = max(1, (sales_rect.h - 20) // 62)
            self.sales_scroll = max(0, min(self.sales_scroll, max(0, len(entries) - visible_rows)))
            visible_entries = entries[self.sales_scroll:self.sales_scroll + visible_rows]
            self.sale_delete_areas = []

            y = sales_rect.y + 40
            for sale_index, sale in visible_entries:
                row_rect = pygame.Rect(sales_rect.x + 10, y, sales_rect.w - 20, 54)
                pygame.draw.rect(surface, WHITE, row_rect)
                pygame.draw.rect(surface, BLACK, row_rect, 1)
                item_names = ', '.join(item.get('name', '') for item in sale.items[:3])
                if len(sale.items) > 3:
                    item_names += '...'
                payment = getattr(sale, 'payment_method', 'efectivo')
                payer_name = getattr(sale, 'payer_name', None)
                payer_info = f' | Nombre: {payer_name}' if payer_name else ''
                main = f'{sale.timestamp} | {sale.chinamo_id} | {sale.sale_type} | {payment}{payer_info} | Total ${sale.total}'
                detail = f'Productos: {item_names}'
                surface.blit(FONT_SMALL.render(main, True, BLACK), (row_rect.x + 8, row_rect.y + 6))
                surface.blit(FONT_SMALL.render(detail, True, (70, 70, 70)), (row_rect.x + 8, row_rect.y + 28))

                delete_rect = pygame.Rect(row_rect.right - 26, row_rect.y + 16, 16, 16)
                pygame.draw.rect(surface, RED, delete_rect)
                x_txt = FONT_SMALL.render('X', True, WHITE)
                surface.blit(x_txt, x_txt.get_rect(center=delete_rect.center))
                self.sale_delete_areas.append((sale_index, delete_rect))
                y += 62

            if not entries:
                empty_txt = FONT_MEDIUM.render('No hay registros para mostrar.', True, BLACK)
                surface.blit(empty_txt, (sales_rect.x + 12, sales_rect.y + 60))

            if self.confirm_delete_sale:
                overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 170))
                surface.blit(overlay, (0, 0))
                modal = pygame.Rect(WIDTH // 2 - 250, HEIGHT // 2 - 80, 500, 160)
                pygame.draw.rect(surface, LIGHT_GRAY, modal)
                pygame.draw.rect(surface, BLACK, modal, 2)
                l1 = FONT_MEDIUM.render('Seguro que quieres eliminar este dato?', True, BLACK)
                l2 = FONT_SMALL.render('Y = Si, N = No (o ESC)', True, BLACK)
                surface.blit(l1, (modal.x + 20, modal.y + 45))
                surface.blit(l2, (modal.x + 20, modal.y + 90))
            return

        pygame.draw.rect(surface, LIGHT_GRAY, self.list_rect)
        pygame.draw.rect(surface, BLACK, self.list_rect, 2)
        list_title = FONT_MEDIUM.render('Fiados activos', True, BLACK)
        surface.blit(list_title, (self.list_rect.x + 10, self.list_rect.y + 8))

        fiados = self.app.fair_manager.get_fiados()
        visible_rows = max(1, (self.list_rect.h - 20) // 70)
        visible_fiados = fiados[self.list_scroll:self.list_scroll + visible_rows]

        self.fiado_click_areas = []
        row_y = self.list_rect.y + 40
        for entry in visible_fiados:
            row_rect = pygame.Rect(self.list_rect.x + 8, row_y, self.list_rect.w - 16, 62)
            selected = entry.get('id') == self.selected_fiado_id
            pygame.draw.rect(surface, (200, 230, 255) if selected else WHITE, row_rect)
            pygame.draw.rect(surface, BLACK, row_rect, 1)

            name_txt = FONT_MEDIUM.render(entry.get('debtor_name', 'Sin nombre'), True, BLACK)
            total_txt = FONT_SMALL.render(f'Total pendiente: ${entry.get("total", 0)}', True, BLACK)
            date_txt = FONT_SMALL.render(entry.get('timestamp', ''), True, (80, 80, 80))
            surface.blit(name_txt, (row_rect.x + 8, row_rect.y + 4))
            surface.blit(total_txt, (row_rect.x + 8, row_rect.y + 28))
            surface.blit(date_txt, (row_rect.x + 8, row_rect.y + 44))
            self.fiado_click_areas.append((entry.get('id'), row_rect))
            row_y += 70

        if not fiados:
            empty = FONT_MEDIUM.render('No hay fiados pendientes.', True, BLACK)
            surface.blit(empty, (self.list_rect.x + 10, self.list_rect.y + 50))

        pygame.draw.rect(surface, LIGHT_GRAY, self.detail_rect)
        pygame.draw.rect(surface, BLACK, self.detail_rect, 2)
        detail_title = FONT_MEDIUM.render('Detalle del fiado', True, BLACK)
        surface.blit(detail_title, (self.detail_rect.x + 10, self.detail_rect.y + 8))

        self.paid_click_areas = []
        selected_entry = None
        if self.selected_fiado_id:
            for entry in fiados:
                if entry.get('id') == self.selected_fiado_id:
                    selected_entry = entry
                    break

        if selected_entry:
            header = FONT_MEDIUM.render(
                f'{selected_entry.get("debtor_name")} - Total: ${selected_entry.get("total", 0)}',
                True,
                BLACK
            )
            surface.blit(header, (self.detail_rect.x + 10, self.detail_rect.y + 35))
            y = self.detail_rect.y + 70
            items = selected_entry.get('items', [])
            visible_items = max(1, (self.detail_rect.h - 90) // 52)
            self.detail_scroll = max(0, min(self.detail_scroll, max(0, len(items) - visible_items)))
            shown_items = items[self.detail_scroll:self.detail_scroll + visible_items]
            for offset, item in enumerate(shown_items):
                item_index = self.detail_scroll + offset
                status = 'Pagado' if item.get('paid') else 'Pendiente'
                line = (
                    f'{item["qty"]}x {item["name"]} | ${item["unit_price"]} '
                    f'| Chinamo: {item.get("chinamo_id", "-")} | {status}'
                )
                text = FONT_SMALL.render(line, True, BLACK)
                surface.blit(text, (self.detail_rect.x + 10, y))

                if not item.get('paid'):
                    paid_rect = pygame.Rect(self.detail_rect.x + 10, y + 20, 88, 24)
                    pygame.draw.rect(surface, GREEN, paid_rect)
                    paid_txt = FONT_SMALL.render('Pagado', True, WHITE)
                    surface.blit(paid_txt, paid_txt.get_rect(center=paid_rect.center))
                    self.paid_click_areas.append((selected_entry.get('id'), item_index, paid_rect))
                y += 52
        else:
            hint = FONT_MEDIUM.render('Selecciona un fiado para ver detalle.', True, BLACK)
            surface.blit(hint, (self.detail_rect.x + 10, self.detail_rect.y + 45))

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



