#creiamo una lista
import copy

from gestionale.core.prodotti import ProdottoRecord

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

tot, *altri_campi = calcola_statistiche_carrello(carrello)

print(tot)

#set



