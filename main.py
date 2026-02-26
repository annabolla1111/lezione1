#Scriviamo un codice python che modelli un
#semplice gestionale aziendale. dovremo prevedere la possibilita di
#definire entita che modellino i prodotti, i clienti, offrire
#interfacce per calcolare i prezzi eventualmente scontati ecc
from logging import raiseExceptions

#come avrei fatto il primo anno (non va bene)
prodotto1_nome = "Laptop"
prodotto1_prezzo = 1200.0
prodotto1_quantita = 5

prodotto2_nome = "Mouse"
prodotto2_prezzo = 12.0
prodotto2_quantita = 15

valore_magazzino = prodotto1_prezzo*prodotto1_quantita + prodotto2_prezzo*prodotto2_quantita

print(f"Valore magazzino: {valore_magazzino}")

#questo non è un bel codice perche ho variabili tutte scorrelate tra loro
#allora creo una classe

#uso pass perche non mi dia errore
class Prodotto:
    #se una cosa è ugiale per tutti i prodotti la passo prima del costruttore
    aliquota_iva = 0.22 #variabile di classe - ovvero la stessa per tutte le istanze che verrannp create
    #le var di classe esistono una sola volta ovvero quando creo la classe

    def __init__(self, nome: str, prezzo: float, quantita: int, fornitore = None): #queste quantita le passo come argomento al costruttore
       #fornitore = ... è il default se non viene passato nulla
        self.nome = nome
        self._prezzo = None
        self.prezzo = prezzo
        self.quantita = quantita
        self.fornitore = fornitore
       #variabili di istanza, essitono solo nell'istanza

        #i parametri dipendono dalle proprieta che voglio dare al mio prodotto
       #self cioe l'istanza che creo della classe prodotto avra queste 4 proprieta
    #quando creo una proprietà la devo assegnare
    #non devo dire cosa è un intero e cosa è una stringa
    #posso pero suggerire il tipo nel costruttore

    def valore_netto(self):
        return self._prezzo*self.quantita

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto*(1+self.aliquota_iva)
        return lordo

    #posso creare anche metodi di classe ovvero che sono validi per tutte, uso un decoratore
    #i decoratori si indicano con @
    #metodo che creo una v sola ad esempio la classe che parla con il database la faccio
    #solo una volta
    #per creare classi che implementano un pattern che si chiama singleton(?)
    @classmethod
    def costruttore_con_quantita_uno(cls, nome:str, prezzo:float, fornitore:str): #i costr di classe prendono come input il cls invece del self
        cls(nome, prezzo, 1, fornitore)

    #metodi statici non sono associati alla singola istanza ma sono di suporto
    # ad esempio per i calcoli
    @staticmethod
    def applica_sconto(prezzo,percentuale): #non devo passare ne cls ne self
        return prezzo*(1-percentuale)

    @property #metodo che si comporta come getter e setter di java
    def price(self): #getter
        return self._prezzo
    @price.setter # posso farlo solo se ho definito il getter
    def price(self, valore):
        if valore < 0: #faccio il controllo prima di assegnare il valore
            raise ValueError("Attenzione il prezzo non puo essere negativo")
        self._prezzo = valore






mioprodotto1 = Prodotto("Laptop", 1200.0, 12, "ABC")
    #tra parentesi tutti gli argomenti che ho passato al costruttore tranne il self
    #mioprodotto1 è un istanza della classe/oggetto Prodotto che ha 4 parametri
    #se non mettiamo il paramentro: ... dobbizmo ricordarci l'ordine

print(f"nome prodotto: {mioprodotto1.nome} - prezzo: {mioprodotto1.prezzo}")

print(f"Il totale lordo di mioprodotto1 è {mioprodotto1.valore_lordo()}") #uso un metodo di istanza
p3 = Prodotto.costruttore_con_quantita_uno("Auricolari", 200, "ABC") #uso per chiamare metodo di classe
print(f"Prezzo scontato di mioprodotto1 {Prodotto.applica_sconto(mioprodotto1.prezzo, percentuale= 0.15)}")

mioprodotto2 = Prodotto("Mouse", 10.0, 25, "CDE")


print(f"nome prodotto: {mioprodotto2.nome} - prezzo: {mioprodotto2.prezzo}")

print(f"valore lordo di myproduct1: {mioprodotto1.valore_lordo()}") #prima dell'aggiornamento iva

Prodotto.aliquota_iva = 0.24 #se cambio il valore dell'iva tutte le istanze di prodotto avranno l'iva aggiornata
#ho modificato il paramentro della classe


print(f"valore lordo di myproduct1: {mioprodotto1.valore_lordo()}") #dopo l'aggiornamento

#funziona perche non devo ripere codice
#rispetto principio incapsulamento

#scrivo classe cliente che abbia i campi nome, email, categoria (gold, silver, bronze)
#vorremmo che questa classe avesse un metodo che chiamiamo descrizione che deve restituire una stringa
# formattata in un certo modo
#"Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

#si modifichi la classe cliente in maniera tale che la propr categoria sia
#protetta e accetti solo (Gold, Silver, Bronze)

class Cliente:
    def __init__(self, nome, email, categoria):
        self.nome = nome
        self.email = email
        self._categoria = None
        self.categoria = categoria

    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, categoria):
        categorie_valide = {"Gold", "Silver", "Bronze"}
        if categoria not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida scegliere tra Gold, Silver, Bronze")
        self._categoria = categoria



    def descrizione(self): #to_string in java
        return f"Cliente {self.nome} ({self.categoria}) - {self.email}"

c1 = Cliente("Mario Bianchi", "mario@google.com", "Gold")
c2 = Cliente("Fulvio Bianchi", "fulvio@google.com", "Gold")
#c3 = Cliente("Carlo Bianchi", "carlo@google.com", "Platinum") #mi da value error
#se faccio print(c1) mi da una cosa strana. perche sto stampando un oggetto
#mi restituisce l'indirizzo di memoria dove si trova l'oggetto
print(c1.descrizione())

#strumento fondamentale è il debug, metto brak point quando arriva li il programma si ferma
#debbaggo e esegue tutto fino al break point (la riga dove ce il bp non la esegue )
