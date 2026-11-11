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
