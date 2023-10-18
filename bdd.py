import psycopg2

# Connexion a la bdd existante
conn = psycopg2.connect(
    database="microservices",
    user="docker",
    password="docker",
    host="0.0.0.0"
)

# ouverture du curseur pour faciliter les opérations vers la bdd
cur = conn.cursor()

# Requête à la bdd
cur.execute("SELECT * FROM utilisateur")
rows = cur.fetchall()
if not len(rows):
    print("Empty")
else:
    for row in rows:
        print(row)


# fermer la connexion a la bdd
cur.close()
conn.close()