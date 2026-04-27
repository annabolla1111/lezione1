from dataclasses import dataclass


@dataclass
class ProdottoRecord:
    nome: str
    prezzo_unitario: float

#per prodotto abbiamo scelto come chiave primaria il nome


    def __hash__(self):
        return hash(self.nome)

    def __eq__(self, other):
        self.nome == other.nome

    def __str__(self):
        return f"{self.nome} -- {self.prezzo_unitario}"