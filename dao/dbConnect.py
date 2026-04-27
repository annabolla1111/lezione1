import pathlib

import mysql.connector

class DBConnect:
    _mypool = None #variabile di classe cls

    def __init__(self):
        #per implementare il pattern singletone ed impedire al chiamante di creare istanza di classe.
        raise RuntimeError("Attenzione! non devi creare un'istanza di questa classe. Usa i metodi di classe.")

    #classmethod non ha il self perche non è il metodo dell'istanza ma della classe
    #invece di creare una connessione creo un pool di connessioni
    @classmethod
    def getConnection(cls): #questa ce la danno all'esame, insieme a un metodo del dao
        if cls._mypool is None: #per evitare di creare la connessione inutilmente se ce gia
            try: #questo codice si ripete spesso quindi lo sistemiamo
                # cnx = mysql.connector.connect(
                #     user = "root",
                #     password = "rootroot",
                #     host = "127.0.0.1",
                #     database = "sw_gestionale"
                # )
                #pool velocizza la cnnessione
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool( #il mio connettore ammette user, pss,..,
                    # user = "root",
                    # password = "rootroot",
                    # host = "127.0.0.1",
                    # database="sw_gestionale",
                    pool_size = 3, #quante connessioni posso creare
                    pool_name = "myPool",
                    option_files = f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"  #modulo che mi da il percorso locale del file
                )
                return cls._myPool.get_connection()

            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None
        else:
            #allora il pool già esiste, e quindi restituisco direttamente la connessione
            return cls._myPool.get_connection()



