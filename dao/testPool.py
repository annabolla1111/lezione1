import time

import mysql.connector

tic = time.time()

for i in range(100):
    cnx = mysql.connector.connect(user="root",
                                  password="rootroot",
                                  host="127.0.0.1",
                                  database="sw_gestionale")
    cursor = cnx.cursor()
    query = "select * from prodotti"
    cursor.execute(query)
    out = cursor.fetchall()
    cursor.close()
    cnx.close()
toc = time.time()

print(f"Tempo con connect:{toc-tic}")

tic = time.time()
cnxPool = mysql.connector.pooling.MySQLConnectionPool(host="127.0.0.1",
                                                      user="root",
                                                      password="rootroot",
                                                      database="sw_gestionale",
                                                      pool_size=3,
                                                      pool_name="myPool")

for i in range(100):
    cnx = cnxPool.get_connection()
    cursor = cnx.cursor()
    query = "select * from prodotti"
    cursor.execute(query)
    out1 = cursor.fetchall()
    cursor.close
    cnx.close()
toc = time.time()
print(f"Tempo di esecuzione con pooling:{toc-tic}")