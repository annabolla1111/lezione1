from dataclasses import dataclass

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

#definire una classe abbonamento che abbia come attributi: nome, prezzo mensile, mesi
#abbonamento dovra avere un metodo per calcolare il prezzo finale (prezzo_mensile*mesi)

class Abbonamento:
    def __init__(self, nome: str, prezzo_mensile: float, mesi: int):
        self.nome = nome
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.mesi*self.prezzo_mensile

@dataclass
class ProdottoRecord:
    nome: str
    prezzo_unitario: float

    def __hash__(self):
        return hash((self.nome, self.prezzo_unitario)) #passiamo una tupla con gli elem che ci servonos

    def __str__(self):
        return f"{self.nome} -- {self.prezzo_unitario}"

MAX_QUANTITA = 1000

def creo_prodotto_standard(nome:str,prezzo:float):
    return Prodotto(nome, prezzo, 1, None)


#per non eseguire il codice sottostante quando importo il modulo prodotti
# sfrutto il fatto che py riconosce quando eseguo il file in standalone e quando è importato

def _test_modulo(): #faccio un metodo per testare
    print("Sto testando il modulo")
    #per testare comodamente i moduli, da fare SEMPRE
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

if __name__=="__main__":
    _test_modulo()