#Scriviamo un codice python che modelli un
#semplice gestionale aziendale. dovremo prevedere la possibilita di
#definire entita che modellino i prodotti, i clienti, offrire
#interfacce per calcolare i prezzi eventualmente scontati ecc
from logging import raiseExceptions

#come avrei fatto il primo anno (non va bene)
#prodotto1_nome = "Laptop"
#prodotto1_prezzo = 1200.0
#prodotto1_quantita = 5

#prodotto2_nome = "Mouse"
#prodotto2_prezzo = 12.0
#prodotto2_quantita = 15

#valore_magazzino = prodotto1_prezzo*prodotto1_quantita + prodotto2_prezzo*prodotto2_quantita

#print(f"Valore magazzino: {valore_magazzino}")

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
    def prezzo(self): #getter
        return self._prezzo
    @prezzo.setter # posso farlo solo se ho definito il getter
    def prezzo(self, valore):
        if valore < 0: #faccio il controllo prima di assegnare il valore
            raise ValueError("Attenzione il prezzo non puo essere negativo")
        self._prezzo = valore


    def __str__(self):
        return f"{self.nome} - disponibili: {self.quantita} pezzi a {self.prezzo}"
    def __repr__(self):
        return f"Prodotto (nome={self.nome}, prezzo={self.prezzo}, quantita={self.quantita}, fornitore={self.fornitore})"
    def __eq__(self, other):
        if not isinstance(other, Prodotto):
            return NotImplemented #se non sono elemneti della stessa classe
        return self.nome == other.nome and self.prezzo == other.prezzo and self.quantita == other.quantita and self.fornitore == other.fornitore
    def __lt__(self, other: "Prodotto") -> bool:
        return self.prezzo < other.prezzo

    def prezzo_finale(self) -> float:
        return self.prezzo*(1+self.aliquota_iva)

class ProdottoScontato(Prodotto): #questa classe avra gia un repr un lt uno str
    def __init__(self, nome: str, prezzo: float, quantita: int, fornitore: str, sconto_percento: float):
        #Prodotto.__init__()
        super().__init__(nome, prezzo, quantita, fornitore) #se non mi ricordo da dove eredito
        self.sconto_percento = sconto_percento

    def prezzo_finale(self) -> float:
        return self.valore_lordo()*(1-self.sconto_percento/100)

class Servizio(Prodotto):
    def __init__(self, nome: str, tariffa_oraria: float, ore: int):
        super().__init__(nome=nome, prezzo=tariffa_oraria,quantita=1,fornitore=None)
        self.ore = ore

    def prezzo_finale(self) -> float:
        return self.prezzo*self.ore





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

print(mioprodotto1)

p_a = Prodotto("Laptop", 1200.0, 12, "ABC")
p_b = Prodotto("Mouse", 10.0, 14, "CDE")

print("mioprodotto1 == p_a?", mioprodotto1 == p_a) #va a chaimare __eq__
print("p_a == p_b?", p_a == p_b) #false

mylist = [p_a,p_b, mioprodotto1]
mylist.sort(reverse=True)

print("lista di prodotti ordinata")
for p in mylist:
    print(f"- {p}") #chiama metodo __lt__ e poi fa reverse =true

mioprodotto_scontato = ProdottoScontato("Auricolari", 1200.0, 12, "ABC", sconto_percento=10)
mio_servizio = Servizio("Consulenza", tariffa_oraria=100, ore=3)

mylist.append(mioprodotto_scontato)
mylist.append(mio_servizio)

mylist.sort(reverse=True)

for elem in mylist:
    print(elem.nome,"->", elem.prezzo_finale()) #l'importante è che offrano metodo prezzo finale (ducktyping)

print("-------------------------------------------")

#definire una classe abbonamento che abbia come attributi: nome, prezzo mensile, mesi
#abbonamento dovra avere un metodo per calcolare il prezzo finale (prezzo_mensile*mesi)

class Abbonamento:
    def __init__(self, nome: str, prezzo_mensile: float, mesi: int):
        self.nome = nome
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.mesi*self.prezzo_mensile

abb = Abbonamento(nome="Software Gestionale", prezzo_mensile=30.0, mesi=24)

mylist.append(abb)
for elem in mylist:
    print(elem.nome,"->", elem.prezzo_finale())

def calcola_totale(elementi):
    totale = 0

    for e in elementi:
        totale += e.prezzo_finale()
    return totale
print(f"il totale è {calcola_totale(mylist)}")

#il protocollo serve a specificare i metodi che ci aspettiamo nelle classi
#protocol classe astratta

from typing import Protocol
class HaPrezzoFinale(Protocol):
    def prezzo_finale(self) -> float:
        ...

def calcola_totale(elementi: list[HaPrezzoFinale]) -> float:
        return sum(e.prezzo_finale() for e in elementi)

print(f"il totale è {calcola_totale(mylist)}")

print("--------------------------------------")
print("Uso di dataclass")

from dataclasses import dataclass
@dataclass
class ProdottoRecord:
    nome: str
    prezzo_unitario: float

@dataclass
class ClienteRecord:
    nome: str
    email: str
    categoria:str

@dataclass
class RigaOrdine:
    prodotto: ProdottoRecord
    quantita: int

    def totale_riga(self):
        return self.prodotto.prezzo_unitario*self.quantita

@dataclass
class Ordine:
    righe: list[RigaOrdine]
    cliente: ClienteRecord

    def totale_netto(self):
        return sum(r.totale_riga() for r in self.righe)

    def totale_lordo(self, aliquota_iva):
        return self.totale_netto()*(1+aliquota_iva)

    def num_righe(self):
        return len(self.righe)

@dataclass
class OrdineconSconto(Ordine):
    sconto_percento: float

    def totale_scontato(self):
        self.totale_lordo()*(1-self.sconto_percento)

    def totale_netto(self):
        netto_base = super().totale_netto() #lo prendiamo dalla classe ordine
        return netto_base*(1-self.sconto_percento)
cliente1 = ClienteRecord("Mario Rossi", "mariorossi@xample.com", "Gold")
p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20)

ordine = Ordine([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1)
ordine_scontato = OrdineconSconto([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1, 0.1)

print(ordine)
print("Numero di righe nell'ordine ", ordine.num_righe())
print("Totale netto: ", ordine.totale_netto())
print("Totale lordo (iva 22%)", ordine.totale_lordo(0.22))

print(ordine_scontato)
print("Totale netto sconto: ", ordine_scontato.totale_netto())
print("Totale lordo scontato: ", ordine_scontato.totale_lordo(0.22))

print("------------------------------")

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
