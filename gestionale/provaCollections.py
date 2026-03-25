#creiamo una lista
import copy
from collections import Counter, deque

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700.0)]

print("Prodotti nel carrello: ")

for i, p in enumerate(carrello): #enumerate prende come argormento la lista e restituisce una lista di tuple dove il primo argomento è l'indice e il secondo è l'elemento
    print(f"{i}) {p.nome} - {p.prezzo_unitario}")

#aggiungere alla lista
carrello.append(ProdottoRecord("Monitor", 150.0))
carrello.sort(key=lambda x: x.prezzo_unitario, reverse=True) #per avere prezzo ecrescente

#stampo dopo aver ordinato

print("Prodotti nel carrello: ")

for i, p in enumerate(carrello):
    print(f"{i}) {p.nome} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale prodotti nel carrello: {tot}")

#aggiungere
carrello.append(ProdottoRecord("Monitor", 150.0)) #con append un solo elemento
carrello.extend([ProdottoRecord("aaa", 150.0), ProdottoRecord("bbb", 150.0)]) #con extend una lista
carrello.insert(0, ProdottoRecord("ccc", 250.0)) #prende due argomenti, il primo è l'indice dove andra inserito il prodotto nella lista il secondo è l'elemento

#rimuovere
carrello.pop() #rimuove l'ultimo argomento
carrello.pop(2) #rimuove l'elemetno in posto 2
carrello.remove(p1) #se non so l'indice ma l'elemnto uso remove, se ce ne piu di uno toglie solo il primo
#carrello.clear() #svuota la lista

#sorting
#carrello.sort() #ordina seguendo ordinamento naturale -- questo non funziona senza __lt__
#carrello.sort(reverse=True) #ordina al contrario
#carrello.sort(key=lambda x: x.prezzo_unitario)

#per creare una nuova lista ordinata
#carrello_ordinato = sorted(carrello)

carrello.reverse() #inverte l'ordine
carrello_copia = carrello.copy() #shallow copy, ovvero contengono gli stessi oggetti, se modifico carrello allora si modifica carrello copia. lista nome diverso ma oggetti sono gli stessi
carrello_copia2 = copy.deepcopy(carrello) #mi crea la copia e anche la copia di quello che ce dentro, oggetti distinti. copio anche il contenuto

#tuple, si creano con le tonde
sede_principale = (45,8) #latitudine e longitudine sede torino. NOn cambiamno
sede_milano = (45,9)

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

AliquoteIVA = (("Standard",0.22),
               ("Ridotta", 0.10)) #tupla di tuple

for descr, valore in AliquoteIVA:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    #restituisce prezzo totale, medio massimo e minimo
    prezzi = [p.prezzo_unitario for p in carrello]
    return(sum(prezzi), sum(prezzi) / len(prezzi), max(prezzi), min(prezzi))

tot, media, max, min = calcola_statistiche_carrello(carrello)  #unpacking

#tot, *altri_campi = calcola_statistiche_carrello(carrello)

print(tot)

#set
categorie = {"Gold", "Silver", "Bronze", "Gold"} #se passo due volte gold e stampo tiene solo le istanze distinte
print(categorie)
print(len(categorie))
#unisco piu set
categorie_2 = {"Platinum", "Elite", "Gold"}
#categorie_all = categorie.union(categorie_2)
#posso anche usare la barra per unire le categorie
categorie_all = categorie | categorie_2
print(categorie_all)

categorie_comuni = categorie & categorie_2 #solo elementi comuni
print(categorie_comuni)

categorie_esclusive = categorie - categorie_2 #quelle in categorie che non sono in categorie2
print(categorie_esclusive)

categorie_esclusive_simmetrico = categorie ^ categorie_2  #differenza simmetrica, gli elementi del primo set che non ci sono nel secondo e vicev
print(categorie_esclusive_simmetrico)


prodotti_ordine_A = {ProdottoRecord("Laptop", 1200),
                     ProdottoRecord("Mouse", 20),
                     ProdottoRecord("Tablet", 700)} #oggetti che non sono hashable facciamo funzione di hash in prodotti

prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200),
                     ProdottoRecord("Mouse2", 20),
                     ProdottoRecord("Tablet", 700)}

#metodi utili per i set
s = set()
s1 = set()
#aggiungere
s.add(ProdottoRecord("aaa", 20.0)) #aggiunge un elemento
s.update([ProdottoRecord("aaa", 250.0), ProdottoRecord("bbb", 700.0)])#per aggiungere piu elem

#togliere
#s.remove(elem)#rimuove un elemento. raise keyerror se non esiste
#s.discard(elem) # rimuove un elemtno senza dare errore se non esiste
s.pop() #rimuove e restituisce un elem. non sappiamo quale perche set non è ordinato
s.clear()

#operazioni inisemistiche
s.union(s1) #s | s1, genera un set che unisce i due set
s.intersection(s1) # s & s1 elem comuni
s.difference(s1) #s-s1, elem di s che non sono in s1
s.symmetric_difference(s1)# elem di s non contenuti in s1 e vicev

s1.issubset(s) #se gli elem di s1 sono contenuti in s
s1.issuperset(s) # se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) # se gli elementi di s e quelli di s1 sono diversi, sono disgiunti

#dizionari
#possiamo salvare info a coppie, chiave-valore
catalogo = {
    "LAP001": ProdottoRecord("Laptop", 1200),
    "LAP002": ProdottoRecord("Laptop Pro", 2300.0),
    "MAU001": ProdottoRecord("Mouse", 20.0),
    "AUR001": ProdottoRecord("Auricolari", 250.0)
}

cod = "LAP002"
prod = catalogo[cod] #uso codice per prendere l'oggetto associato
#utile perche evitiamo di ciclare su una lista
#complessita o grande di 1
print(f"Il prodotto con codice {cod} è {prod}") #definisco __str in prodotto regord per avere print piu carina

#occhio quando proviamo a leggere ogg che non ci sono. o uso una if se no metodo get
#print(f"Cerco un altro oggetto: {catalogo["NonEsiste"]}") #keyerror

prod1 = catalogo.get("NonEsiste")
if prod1 is None:
    print("Prodotto non trovato")


prod2 = catalogo.get("NonEsiste2", ProdottoRecord("Sconosciuto", 0))
print(prod2)

#ciclare su un dizionario
keys = list(catalogo.keys()) # per stamparli uso una lista
values = list(catalogo.values())
for k in keys:
    print(k)
for v in values:
    print(v)

#per recuperare tutti e due con items, restitusce coppie chiave valore
for key, val in catalogo.items():
    print(f"Codice {key} è associata a: {val}")

#per eliminare da dizionario usiamo pop
rimosso = catalogo.pop("LAP002")
print(rimosso)

#dict comprehension
prezzi = {codice: prod.prezzo_unitario for codice, prod in catalogo.items()} #per creare un dizionario e specificare come deve costruito direttamente come argomenti delle graffe

#da ricordare per dict
# v = d[key] # per leggere, restituisce key error se non esiste
# d[key] = v # scrivo sul diz
# v = d.get(key, default=None) # legge senza rischiare key error
# d.pop() # restituisce un valore e lo cancella dal diz
# d.clear() #elimina tutto
# d.keys()#mi restituisce tutte le chiavi del diz
# d.values()#mi restituisce tutti i valori del diz
# d.items()#restituisce le coppie
# if key in d #se key è presente nel diz
#per commentare cosi uso ctrl /

#esercizio
"""Esercizio live
Per ciascuno dei seguenti casi, decidere quale struttura usare:"""

"""1) Memorizzare una elenco di ordini che dovranno poi essere processati in ordine di arrivo""" #lista, perche posso ordinare, puo contenere oggetti duplicati
ordini_da_processare = []
o1 = Ordine([], ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"))
o2 = Ordine([], ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"))
o3 = Ordine([], ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"))
o4 = Ordine([], ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"))

ordini_da_processare.append((o1, 0)) #arrivato al tempo 0, per ordinare usando il secondo elem della tupla
ordini_da_processare.append((o2, 10))
ordini_da_processare.append((o3, 3))
ordini_da_processare.append((o4, 45))

"""2) Memorizzare i CF dei clienti (univoco)""" #set, cosi mi aggiunge una sola volta i codici fiscali
codici_fiscali = {"adjdjfhdjh", "dknfkjrfrd", "dfherkuhf", "dknfkjrfrd"} #il secondo e il quarto sono uguali, mi aggiunge solo il secondo
print(codici_fiscali)

"""3) Creare un database di prodotti che posso cercare con un codice univoco""" #diz, per cercare in maniera efficiente e in poco tempo
listino_prodotti = {"LAP0001" : ProdottoRecord("Laptop", 1200.0),
                    "KEY001" : ProdottoRecord("Keyboard", 20.0)}

"""4) Memorizzare le coordinate gps della nuova sede di Roma""" #tupla, coord non cambiano
magazzino_roma = (45, 6)

"""5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale""" #set, perche le categorie sono distinte
categorie_periodo = set()
categorie_periodo.add("Gold")
categorie_periodo.add("Bronze")

print("___________________________________")

#strutture piu avanzate
#counter, quante volte ce stato un certo valore, piu comune, meno comune...

lista_clienti = [
    ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"),
    ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "mario@polito.it", "Gold"),
    ClienteRecord("Giuseppe Averta", "bianchi@polito.it", "Silver"),
    ClienteRecord("Francesca Pistilli", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Fulvio Corno", "carlo@polito.it", "Silver")
]

categorie = [c.categoria for c in lista_clienti] # list comprehension
categorie_counter = Counter(categorie) #da importare

print("Distribuzione categorie")
print(categorie_counter)

print("Le 2 categorie piu frequenti")
print(categorie_counter.most_common(2)) #quanti elementi prendere

#posso calcolare i totali
print("Totale: ")
print(categorie_counter.total())

vendite_gennaio = Counter(
    {"Laptop": 13, "Tablet": 15}
)

vendite_febbraio = Counter(
    {"Laptop": 3, "Stampante": 1}
)

vendite_bimestre = vendite_gennaio+vendite_febbraio

#Aggregare informazione
print(f"Vendite Gennaio: {vendite_gennaio}")
print(f"Vendite Febbraio: {vendite_febbraio}")
print(f"Vendite bimestre: {vendite_bimestre}") #mi aggrega le vendite che hanno la stessa chiave

# Fare la differenza
print(f"Differenza di vendite: {vendite_gennaio-vendite_febbraio}") #dove ho underperformato


#modificare i valore in the fly

vendite_gennaio["Laptop"] += 4
print(f"Vendite Gennaio: {vendite_gennaio}")

# metodi da ricordare
#c.most_common(n) #restituisce gli n elementi più frequenti
#c.total() # somma dei conteggi

#Defaultdicts

#deque
print("=============================================================")
print("Deque")

coda_ordini = deque()
for i in range(1, 10):
    cliente = ClienteRecord(f"Cliente {i}", f"cliente{i}@polito.it", "Gold")
    prodotto = ProdottoRecord(f"Prodotto{i}", 100.0 * i)
    ordine = Ordine([RigaOrdine(prodotto, 1)], cliente)

    coda_ordini.append(ordine)

print(f"Ordini in coda {len(coda_ordini)}")

#cicla finchè è pieno
while coda_ordini:
    ordine_corrente = coda_ordini.popleft()
    print(f"Sto gestendo l'ordine del cliente: {ordine_corrente.cliente}") #uso metodo tostring del cliente

print("Ho processato tutti gli ordini")
