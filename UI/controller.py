import flet as ft

from gestionale.gestoreOrdini import GestoreOrdini


class Controller:
    def __init__(self, v):
        self._view = v
        #per chiedere al modello (GestoreOrdini) di darmi questo ordini
        self._model = GestoreOrdini()


    def add_ordine(self, e): #  I METODI ASSOCIATI AI PULSANTI DEVONO AVERE DUE ARGOMENTI "e" è l'evento scatenato
        # Prodotto (nome, prezzo, qt)
        nomePstr = self._view._txtInNomeP.value  #value come proprieta non come metodo!!!!
        if nomePstr == "":#questo controllo devo farlo su tutti i campi
            self._view._lvOut.controls.append(ft.Text("Attenzione il campo non può essere vuoto", color = "red"))
            self._view.update_page()
            return
        try:
            prezzo = float(self._view._txtInPrezzo.value)
        except ValueError: #se non riesce a convertire in float
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! il prezzo deve essere un numero.",
                        color="red")
            )
            self._view.update_page()
            return
        try:
            quantita = int(self._view._txtInQuantita.value)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! la quantità deve essere un intero.",
                        color="red")
            )
            self._view.update_page()
            return

        # Cliente
        nomeC = self._view._txtInNomeC.value
        mail = self._view._txtInMail.value
        categoria = self._view._txtInCategoria.value

        ordine = self._model.crea_ordine(nomePstr, prezzo,
                                         quantita, nomeC,
                                         mail, categoria) #uso crea ordine passando i parametri passati dall'utente
        self._model.add_ordine(ordine) #aggiungo ordine o

        #per pulire quando creo l'ordine
        self._view._txtInNomeP.value = ""
        self._view._txtInPrezzo.value = ""
        self._view._txtInQuantita.value = ""
        self._view._txtInNomeC.value = ""
        self._view._txtInMail.value = ""
        self._view._txtInCategoria.value = ""

        self._view._lvOut.controls.append(
            ft.Text("Ordine correttamente inserito.",
                    color="green"))
        self._view._lvOut.controls.append(
            ft.Text("Dettagli dell'ordine:")
        )
        self._view._lvOut.controls.append(
            ft.Text(ordine.riepilogo()) #stringa formattata che avevamo fatto
        )

        self._view.update_page()

    def gestisci_ordine(self, e):
        self._view._lvOut.controls.clear() #devo pulire l'interfaccia grafica
        res, ordine = self._model.processa_prossimo_ordine()# fa return false se non ci sono ordini in coda, true se ordine è stato correttam processato

        if res:
            self._view._lvOut.controls.append(
                ft.Text("Ordine processato con successo.", color="green"))
            self._view._lvOut.controls.append(
                ft.Text(ordine.riepilogo())
            )
            self._view.update_page()
        else: #se res è false
            self._view._lvOut.controls.append(
                ft.Text("Non ci sono ordini in coda.", color="blue")
            )
            self._view.update_page()


    def gestisci_all_ordini(self, e):
        self._view._lvOut.controls.clear()
        ordini = self._model.processa_tutti_ordini()

        if not ordini:
            self._view._lvOut.controls.append(
                ft.Text("Non ci sono ordini in coda.", color="blue"))
            self._view.update_page()
        else:
            self._view._lvOut.controls.append(ft.Text("\n"))
            self._view._lvOut.controls.append(
                ft.Text(f"Ho processato correttamente {len(ordini)} ordini.",
                        color="green")
            )
            for o in ordini:
                self._view._lvOut.controls.append(ft.Text("\n"))
                self._view._lvOut.controls.append(ft.Text(o.riepilogo()))
            self._view.update_page()

    def stampa_sommario(self, e):
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(
            ft.Text("Di seguito il sommario dello stato del business.",
                    color="orange"))
        self._view._lvOut.controls.append(
            ft.Text(self._model.get_riepilogo()))
        self._view.update_page()