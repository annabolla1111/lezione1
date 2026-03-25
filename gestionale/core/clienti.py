#scrivo classe cliente che abbia i campi nome, email, categoria (gold, silver, bronze)
#vorremmo che questa classe avesse un metodo che chiamiamo descrizione che deve restituire una stringa
# formattata in un certo modo
#"Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

#si modifichi la classe cliente in maniera tale che la propr categoria sia
#protetta e accetti solo (Gold, Silver, Bronze)

from dataclasses import dataclass
categorie_valide = {"Gold", "Silver", "Bronze"}

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

        if categoria not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida scegliere tra Gold, Silver, Bronze")
        self._categoria = categoria



    def descrizione(self): #to_string in java
        return f"Cliente {self.nome} ({self.categoria}) - {self.email}"

@dataclass
class ClienteRecord:
    nome: str
    email: str
    categoria:str

    def __str__(self):
        return f"{self.nome} -- {self.email} ({self.categoria})"

def _test_modulo():
    print("Sto testando il modulo")
    c1 = Cliente("Mario Bianchi", "mario@google.com", "Gold")
    c2 = Cliente("Fulvio Bianchi", "fulvio@google.com", "Gold")
    #c3 = Cliente("Carlo Bianchi", "carlo@google.com", "Platinum") #mi da value error
    #se faccio print(c1) mi da una cosa strana. perche sto stampando un oggetto
    #mi restituisce l'indirizzo di memoria dove si trova l'oggetto
    print(c1.descrizione())

#strumento fondamentale è il debug, metto brak point quando arriva li il programma si ferma
#debbaggo e esegue tutto fino al break point (la riga dove ce il bp non la esegue )

if __name__ == "__main__":
    _test_modulo()