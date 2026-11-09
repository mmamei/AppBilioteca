import biblioteca
from guizero import App, PushButton, Text, TextBox



def main():
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

    

    app = App(title="Biblioteca", layout="grid")

    Text(app, text="Nome", grid=[0, 0])
    nome_input = TextBox(app, grid=[1, 0])

    Text(app, text="Cognome", grid=[0, 1])
    cognome_input = TextBox(app, grid=[1, 1])

    Text(app, text="Anno di nascita", grid=[0, 2])
    anno_input = TextBox(app, grid=[1, 2])

    PushButton(app,text="Aggiungi utente",command=aggiungi_utente,grid=[0, 3, 2, 1])

    risultato = Text(app, text="", grid=[0, 4, 2, 1])

    
    app.display()


if __name__ == "__main__":
    main()