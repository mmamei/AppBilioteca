import biblioteca
from guizero import App, PushButton, Text, TextBox
from gui_widgets.aggiungi_utente import aggiungi_utente_gui
from gui_widgets.aggiungi_libro import aggiungi_libro_gui

def main():
    app = App(title="Biblioteca", layout="grid")
    aggiungi_utente_gui(app, 0,0)
    aggiungi_libro_gui(app, 2,0)
    app.display()


if __name__ == "__main__":
    main()