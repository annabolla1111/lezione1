from dataclasses import dataclass

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord


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