from guizero import App, PushButton, Text, TextBox
import biblioteca


def aggiungi_libro_gui(app, i,j):

        def aggiungi_libro():
            titolo = titolo_input.value.strip()
            autore = autore_input.value.strip()

            if not titolo or not autore:
                risultato_libro.value = "Inserisci titolo e autore."
                return

            id_libro = biblioteca.aggiungi_libro(titolo, autore)
            risultato_libro.value = f"Libro aggiunto con ID {id_libro}."

        Text(app, text="Aggiungi Libro", grid=[i, j, 2, 1])

        Text(app, text="Titolo", grid=[i, j + 1])
        titolo_input = TextBox(app, grid=[i + 1, j + 1])

        Text(app, text="Autore", grid=[i, j + 2])
        autore_input = TextBox(app, grid=[i + 1, j + 2])

        PushButton(app, text="Aggiungi libro", command=aggiungi_libro, grid=[i, j + 3, 2, 1])

        risultato_libro = Text(app, text="", grid=[i, j + 4, 2, 1])

        return titolo_input, autore_input, risultato_libro
    