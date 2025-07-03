import mysql.connector
import pandas as pd

# Prisijungti prie sakila duomenų bazės.
# Pabandyti consolėje atsispausdinti customer lentelės duomenis.
#
# 1. Atvaizduoti kiek kiekvienas klientas iš viso yra išleidęs filmų nuomai. atvaizduojame stulpeline diagrama
# 2. Atvaizduoti filmus pagal jų trukmes. t.y sugrupuoti pagal trukmę ir Y ašyje rodyti kiekį, X trukmę. Stulpelinė diagrama.
# 3. Atvaizduoti kiek sugeneruota pajamų pamėnesiui. Stulpeliais pajamas, kreive su taškais kiek filmų buvo išnuomuota.
# 4. Atvaizduoti filmus pagal kategorijas, piechart. Kategorijos yra category lentelėje.
# 5. Top 10 populiariausių filmų pagal išnuomavimo kiekį. Atvaizdavimas pasirinktinai

DB_CONFIG = {
    'host':'localhost',
    'port': 3306,
    'user':'root',
    'password':"",
    'database':'sakila'
}
def get_conn():
    return mysql.connector.connect(**DB_CONFIG)


headers = ['customer_id', 'store_id', 'first_name', 'last_name', 'email', 'address_id', 'active', 'create_date', 'last_update']
def load_customers():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from customer")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    # print(rows)

    customers = []
    for row in rows:
        item = {}
        for i in range(len(headers)):
            item[headers[i]] = str(row[i])
        customers.append(item)
    return customers

    df = pd.DataFrame(rows, columns=column_names)
    return df
