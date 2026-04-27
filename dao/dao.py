import mysql.connector

from dao.dbConnect import DBConnect
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord

#dao modulo che contiene una sola classe
#si occupa dell'interazione con il database
#dto sono oggetti che contengono dati, collettori di dati


class DAO:

    @staticmethod #non hanno il self, tutto quello che sa il metodo è dentro la funzione
    def getAllProdotti():
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #     host = "127.0.0.1",
        #     database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True) #serve per scorrere i risultati delle queery
        cursor.execute("Select * from prodotti") #esegue una queery
        row = cursor.fetchall() #leggere i dati dal cursore

        #creaiamo oggetti di tipo prodotto e gli restituiamo

        res = []
        for p in row:
            res.append(ProdottoRecord(p["nome"], p["prezzo"]))

        cursor.close()
        cnx.close() #impo
        return res

    @staticmethod
    def getAllClienti():
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #     host = "127.0.0.1",
        #     database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("Select * from clienti")
        row = cursor.fetchall()

        res = []
        for p in row:
            res.append(ClienteRecord(p["nome"], p["mail"], p["categoria"])) #devono essere gli stessi che ho su dbeaver

        cursor.close()
        cnx.close()
        return res

#di solito non modifichiamo i database
    @staticmethod
    def addProdotto(prodotto):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #     host = "127.0.0.1",
        #     database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        query = """insert into prodotti 
                    (nome, prezzo) values (%s, %s)"""
        #aggiungere riga nel database

        cursor.execute(query, (prodotto.name, prodotto.prezzo_unitario))

        cnx.commit() #questo modifica il database
        cursor.close()
        cnx.close()
        return

    @staticmethod
    def addCliente(cliente):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #     host = "127.0.0.1",
        #     database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        query = """insert into clienti
                    (nome, mail, categoria)
                     values (%s, %s, %s)"""

        cursor.execute(query, (cliente.nome, cliente.mail, cliente.categoria))

        cnx.commit()
        cursor.close()
        cnx.close()
        return

    @staticmethod
    def hasCliente( cliente):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #     host = "127.0.0.1",
        #     database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection() #la importo da dbConnect

        cursor = cnx.cursor(dictionary=True)
        query = "Select * from clienti where mail = %s"
        cursor.execute(query, (cliente.mail,))
        row = cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0

    @staticmethod
    def hasProdotto(prod):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #     host = "127.0.0.1",
        #     database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = "Select * from prodotti where nome = %s"
        cursor.execute(query, (prod.name,))
        row = cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0


if __name__ == "__main__":
    mydao = DAO()
    mydao.getAllProdotti()