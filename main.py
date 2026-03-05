#Scriviamo un codice python che modelli un
#semplice gestionale aziendale. dovremo prevedere la possibilita di
#definire entita che modellino i prodotti, i clienti, offrire
#interfacce per calcolare i prezzi eventualmente scontati ecc

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
print("=============================")
#PER UTILIZZARE le classi di prodotto dentro al main faccio...

from gestionale.vendite.ordini import Ordine, RigaOrdine, OrdineconSconto
from gestionale.core.prodotti import Prodotto, creo_prodotto_standard, ProdottoRecord
from gestionale.core.clienti import Cliente, ClienteRecord
import networkx as nx

p1 = Prodotto("Ebook", 120.0, 1, "AAA")
p2 = creo_prodotto_standard("Tablet", 750.0)

print(p1)
print(p2)

#MODI PER IMPORTARE
#1)
from gestionale.core.prodotti import ProdottoScontato
p21 = ProdottoScontato("Auricolari",120,1,"ABC",10)
#2)
from gestionale.core.prodotti import ProdottoScontato as ps
p3 = ps("Auricolari",120,1,"ABC",10)
#3)
from gestionale.core import prodotti
from gestionale.core import prodotti as p

p4 = prodotti.ProdottoScontato("Auricolari", 120, 1, "ABC", 10)
#4)
p5 = p.ProdottoScontato("Auricolari",120,1,"ABC",10)
print("=============================")

c1 = Cliente("Mario Rossi", "mail@mail.com","Gold")

print("=============================")



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

#nel package gestionale scriviamo un modulo fatture.py che contenga:
#- una classe fattura, che contiene un ordine, un numero fattura e una data
#- un metodo genera_fattura che restituisce una stringa formattata con tutte le info della fattura
#