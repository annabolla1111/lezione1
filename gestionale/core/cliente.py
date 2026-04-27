#file per scrivere solo la def associata alla tabella
from dataclasses import dataclass

#se ho tabella clienti devo creare classe cliente!!

@dataclass
class ClienteRecord:
    nome: str
    email: str
    categoria:str

#deve avere metodo dunder hash

    def __hash__(self):
        #mi permette di associare una funzione di hash all'istanza di questa classe
        #due istanze sono lo stesso oggetto se la chiave primaria del database è la stessa
        #associa all'oggetto un indirizzo univoco
        #la usiamo per identificare la chiave primaria
        return hash(self.email)

    def __eq__(self, other):
        self.email == other.email


    def __str__(self):
        return f"{self.nome} -- {self.email} ({self.categoria})"

    #corredo minimo per un dto
    #per ogni tabella costruiamo una claase fatta cosi