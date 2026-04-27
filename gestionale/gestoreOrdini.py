"""
Scrivere un software gestionale che abbia le seguenti funzionalità:
1) supportare l'arrivo e la gestione di ordini.
1bis) quando arriva un nuovo ordine, lo aggiungo ad una coda,
assicurandomi che sia eseguito solo dopo gli altri.
2) avere delle funzionalità per avere statistiche sugli ordini
3) fornire statistiche sulla distribuzione di ordini per categoria di cliente.
"""
from collections import deque, Counter, defaultdict
import random

from dao.dao import DAO
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdini: #IL MODELLO
    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = [] #non mi importa dell'ordinamento
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list) #gli passiamo come factory una lista, chiavi: categorie, valori: ordini
        #defaultdict per evitare il controllo sull'esistenza della categoria, se categoria non esiste mi restit lista vuota
        #self._dao = DAO() uso i metodi del dao chiamandoli direttam dal dao
        self._allP = []
        self._allC = []
        self._fill_data()

    def _fill_data(self): #usa il dao per creare degli ordini
        # Leggo prodotti e clienti dal db, e poi creo degli ordini randomici per testare la mia app.
        self._allP.extend(DAO.getAllProdotti()) #se ho gia qualcosa gli aggiungo
        self._allC.extend(DAO.getAllClienti())

        for i in range(10):
            indexP = random.randint(0, len(self._allP) - 1)
            indexC = random.randint(0, len(self._allC) - 1)
            ordine = Ordine([RigaOrdine(self._allP[indexP], random.randint(1, 5))],
                            self._allC[indexC]) #ordine vuole ...
            self.add_ordine(ordine)


    def add_ordine(self, ordine: Ordine):
        """Aggiunge un nuovo ordine agli elementi da gestire"""
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto nuovo ordine da parte di {ordine.cliente}")
        print(f"Ordini ancora da evadere {len(self._ordini_da_processare)}")

    #creo un metodo crea ordine che prende le sei quantita e crea un ordine
    def crea_ordine(self, nomeP, prezzoP, quantitaP, nomeC, mailC, categoriaC):
        #l'ordine è fatto da una lista di riga ordine e da un cliente
        #quando creo l'ordine creo gli oggetti prodotto e cliente
        prod = ProdottoRecord(nomeP, prezzoP)
        cliente = ClienteRecord(nomeC, mailC, categoriaC)

        self._update_DB(prod, cliente)
        return Ordine([RigaOrdine(prod, quantitaP)], cliente)

    def _update_DB(self, prod, cliente): #si chiede se ci sono già
        if not DAO.hasProdotto(prod):
            DAO.addProdotto(prod) #prova ad aggiungere al database, se ce gia non lo aggiunge

        if not DAO.hasCliente(cliente):
            DAO.addCliente(cliente)

    def processa_prossimo_ordine(self):
        """Questo metodo legge il prossimo ordine in coda e lo gestisce"""
        #aggiorna delle categorie
        #quante volte ho venduto un laptop, a chi,...

        #assicuriamoci che un ordine da processare esista
        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda")
            return False, Ordine([], ClienteRecord("","","")) #ordine vuoto che avra 2 campi composti da lista e cliente

        #se esiste gestiamo il primo in coda
        ordine = self._ordini_da_processare.popleft() #logica FIFO

        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())


        #aggiorniamo il nostro counter per ogni prodotto
        #aggiornare statistiche su prodotti venduti
        #laptop -- 10 +1
        #mouse -- 5 +3
        print("\n" + "-" * 60)
        print("\n" + "-" * 60)
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.nome] += riga.quantita

        #raggruppo gli ordini per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        #archiviamo l'ordine
        self._ordini_processati.append(ordine)
        print("Ordine correttamente processato")
        return True

    def processa_tutti_ordini(self):
        """Processa tutti gli ordini attualmente presenti in coda."""
        print("\n" + "=" * 60)
        print(f"Processando {len(self._ordini_da_processare)} ordini")
        while self._ordini_da_processare:
            self.processa_prossimo_ordine()
        print("Tutti gli ordini sono stati processati") #mette in un ciclo il metodo che gestisce un solo ordine

    #metodi che usiamo per recuperare info da una classe gli chiamiamo con get, se metodo aggiunge usiamo add
    def get_statistiche_prodotti(self, top_n: int = 5):
        """Questo metodo restituisce info sui prodotti più venduti. """ #restituisce non stampa
        valori = []
        for prodotto, quantita in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto,quantita)) #per stampare piu facilmente, lista di tuple
        return valori



    def get_distribuzione_categorie(self):
        """Questo metodo restituisce info su totale fatturato per ogni categoria presente"""
        #cicla sulle chiavi
        valori = []
        for cat in self._ordini_per_categoria.keys():
            ordini = self._ordini_per_categoria[cat]
            totale_fatturato = sum([o.totale_lordo(0.22) for o in ordini])
            valori.append((cat, totale_fatturato))
        return valori

    def stampa_riepilogo(self):
        """Stampa info di massima"""
        print("\n" + "="*60)
        print("Stato attuale del business:")
        print(f"Ordini correttamente gestiti: {len(self._ordini_processati)}")
        print(f"Ordini in coda: {len(self._ordini_da_processare)}")

        print("Prodotti più venduti:")
        for prod, quantità in self.get_statistiche_prodotti():
            print(f"{prod}: {quantità}")

        print(f"Fatturato per categoria:")
        for cat, fatturato in self.get_distribuzione_categorie():
            print(f"{cat} : {fatturato}")

    def get_riepilogo(self):
        """Restituisce una stringa con le info di massima"""
        sommario = ""
        sommario += "\n" + "="*60
        sommario += f"\n Ordini correttamente gestiti: {len(self._ordini_processati)}"
        sommario += f"\n Ordini in coda: {len(self._ordini_da_processare)}"

        sommario += "\n Prodotti più venduti:"
        for prod, quantità in self.get_statistiche_prodotti():
            sommario += f"\n {prod}: {quantità}"

        sommario += f"\n Fatturato per categoria:"
        for cat, fatturato in self.get_distribuzione_categorie():
            sommario += f"\n {cat} : {fatturato}"
        sommario += "\n" + "="*60
        return sommario

def test_modulo():
    sistema = GestoreOrdini()

    ordini = [
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
               ClienteRecord("Mario Rossi", "mario@mail.it", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 2),
                RigaOrdine(ProdottoRecord("Tablet", 500.0), 1),
                RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
               ClienteRecord("Fulvio Bianchi", "bianchi@gmail.com", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 2),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 2)],
            ClienteRecord("Giuseppe Averta", "giuseppe.averta@polito.it", "Silver")),
        Ordine([
            RigaOrdine(ProdottoRecord("Tablet", 900.0), 1),
            RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
            ClienteRecord("Carlo Masone", "carlo@mail.it", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
            ClienteRecord("Francesca Pistilli", "francesca@gmail.com", "Bronze"))
    ]

    for o in ordini:
        sistema.add_ordine(o) #si aspetta un ordine

    sistema.processa_tutti_ordini()

    sistema.stampa_riepilogo()

if __name__ == "__main__":
    test_modulo()
    #quando eseguiamo questo modulo

#mi stampa gli ordini ricevuti
#processa gli ordini 1 per volta (mario bianchi, fulvio,...)
#le statistiche del counter sono Mouse: 10
# Cuffie: 6
# Laptop: 5
# Tablet: 2
#quelle del defaultdict Gold : 6527.0
# Silver : 2952.4
# Bronze : 1500.6
