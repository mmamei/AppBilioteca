
from guizero import App, PushButton, Text, TextBox
import biblioteca

def aggiungi_utente_gui(app, i,j):
        def aggiungi_utente():
                nome = nome_input.value.strip()
                cognome = cognome_input.value.strip()
                anno = anno_input.value.strip()
        
                if not nome or not cognome:
                    risultato.value = "Inserisci nome e cognome."
                    return
        
                try:
                    anno_nascita = int(anno)
                except ValueError:
                    risultato.value = "L'anno di nascita deve essere un numero intero."
                    return
        
                id_utente = biblioteca.aggiungi_utente(nome, cognome, anno_nascita)
                risultato.value = f"Utente aggiunto con ID {id_utente}."
        

        Text(app, text="Aggiungi Utente", grid=[i, j, 2, 1])
        
        Text(app, text="Nome", grid=[i, j + 1])
        nome_input = TextBox(app, grid=[i + 1, j + 1])

        Text(app, text="Cognome", grid=[i, j + 2])
        cognome_input = TextBox(app, grid=[i + 1, j + 2])

        Text(app, text="Anno di nascita", grid=[i, j + 3])
        anno_input = TextBox(app, grid=[i + 1, j + 3])

        PushButton(app,text="Aggiungi utente",command=aggiungi_utente,grid=[i, j + 4, 2, 1])

        risultato = Text(app, text="", grid=[i, j + 5, 2, 1])

        return nome_input, cognome_input, anno_input, risultato


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
    