import flet as ft

class View:
    def __init__(self,page):
        #nel costruttore dovrei menzionare tutti gli elem menzionati nel carica interfaccia ma non siamo obbligati
        self._page = page
        self._controller = None
        self._page.title = "Tdp 2025 - Software Gestionale" #titolo pagina
        self._page.horizontal_alignment = "CENTER" #allineare al cenrtro
        self._page.theme_mode = ft.ThemeMode.LIGHT #Queste ce le danno gia all'esame
        self._txtInNomeP = None
        self.update_page() #ho creato il metodo sotto

    def carica_interfaccia(self):
        #se inizia per txt mi aspetto che quella variabile sia una stringa
        #in per ricevere input dall'utente
        #out per scrivere

        # Prodotto
        self._txtInNomeP = ft.TextField(label="Nome prodotto", width=200) #etichetta
        self._txtInPrezzo = ft.TextField(label="Prezzo", width=200)
        self._txtInQuantita = ft.TextField(label="Quantità", width=200)
        row1 = ft.Row(controls=[self._txtInNomeP, self._txtInPrezzo, self._txtInQuantita],
                      alignment=ft.MainAxisAlignment.CENTER) #metto questi text field tutti su una riga, passo una lista di controlli

        # Cliente
        self._txtInNomeC = ft.TextField(label="Nome Cliente", width=200)
        self._txtInMail = ft.TextField(label="Mail", width=200)
        self._txtInCategoria = ft.TextField(label="Categoria", width=200)
        row2 = ft.Row(controls=[self._txtInNomeC, self._txtInMail, self._txtInCategoria],
                      alignment=ft.MainAxisAlignment.CENTER)

        # # Buttons
        #testo e metodo che viene eseguito quando lo schiacciamo
        self._btnAdd = ft.ElevatedButton(text="Aggiungi ordine",
                                         on_click=self._controller.add_ordine,
                                         width=200) #add ordine senza () DEVO SCRIVERE QUESTI METODI NEL CONTROLLER
        self._btnGestisciOrdine = ft.ElevatedButton(text="Gestisci prox ordine",
                                                    on_click=self._controller.gestisci_ordine,
                                                    width=200)
        self._btnGestisciAllOrdini = ft.ElevatedButton(text="Gestisci tutti gli ordini",
                                                       on_click=self._controller.gestisci_all_ordini,
                                                       width=200)
        self._btnStampaInfo = ft.ElevatedButton(text="Stampa sommario",
                                                on_click=self._controller.stampa_sommario,
                                                width=200)
        row3 = ft.Row(controls=[self._btnAdd, self._btnGestisciOrdine,
                                self._btnGestisciAllOrdini,
                                self._btnStampaInfo],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._lvOut = ft.ListView(expand=True) #listview controlli che saranno visualizzati uno dopo l'altro
        self._page.add(row1, row2, row3, self._lvOut)

    def set_controller(self,c):
        self._controller = c

    def update_page(self):
        self._page.update() # creo questo metodo cosi posso chiamarlo nel controller

#ALL'ESAME CI DANNO GIA IL VIEW E NOI DOBBIAMO SCRIVERE I METODI