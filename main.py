from ui.menu import Menu
from ui.screens import *

if __name__ == "__main__":
    app = Menu()
    app.change_screen(Splash(app))
    app.run()
    