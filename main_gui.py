import biblioteca
from guizero import App, PushButton, Text, TextBox
from gui_widgets import aggiungi_utente_gui, aggiungi_libro_gui


def main():
    app = App(title="Biblioteca", layout="grid")
    nome_input, cognome_input, anno_input, risultato = aggiungi_utente_gui(app, 0,0)
    titolo_input, autore_input, risultato_libro = aggiungi_libro_gui(app, 2,0)
    app.display()


if __name__ == "__main__":
    main()