#nel package gestionale scriviamo un modulo fatture.py che contenga:
#- una classe fattura, che contiene un ordine, un numero fattura e una data
#- un metodo genera_fattura che restituisce una stringa formattata con tutte le info della fattura
#

from dataclasses import dataclass
from datetime import date

from gestionale.core.clienti import Cliente
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


@dataclass
class Fattura:
    ordine: "Ordine"
    num_fattura: str
    data: date


    def genera_fattura(self):
        linee = [
            f"="*60,
            #intestazione della fattura ovvero data e num fattura
            f"Fattura no. {self.num_fattura} del {self.data}", #RICORDARSI LA VIRGOLA
            f"=" * 60,
            f"Cliente: {self.ordine.cliente.nome}",
            f"Categoria: {self.ordine.cliente.categoria}",
            f"Mail: {self.ordine.cliente.email}",
            f"-" * 60,
            #dettagli
            f"DETTAGLIO ORDINE"

        ]
        for i, riga in enumerate(self.ordine.righe):
            linee.append(f"{i+1}. "
            f"{riga.prodotto.nome} "
            f"{riga.quantita} x {riga.prodotto.prezzo_unitario} = "
            f"{riga.totale_riga()}")
        linee.extend([f"-" * 60,
            f"Totale Netto: {self.ordine.totale_netto()}",
            f"iva: {self.ordine.totale_netto()*0.22}",
            f"Totale lordo: {self.ordine.totale_lordo(0.22)}",
            f"="*60]

        )
        return "\n".join(linee)

def _test_modulo():
    p1 = ProdottoRecord("Laptop", 1200.0)
    p2 = ProdottoRecord("Mouse", 20.0)
    p3 = ProdottoRecord("Tablet", 600.0)
    cliente = Cliente("Mario Bianchi", "mario@gmail.com", "Gold")
    ordine = Ordine(righe = [RigaOrdine(p1,1), RigaOrdine(p2,5), RigaOrdine(p3,2)], cliente=cliente)
    fattura = Fattura(ordine, "2026/01", date.today())
    print(fattura.genera_fattura())

if __name__ == "__main__":
    _test_modulo()