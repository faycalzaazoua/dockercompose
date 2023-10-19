from fastapi import FastAPI, Request
from os import environ as env
from starlette.templating import Jinja2Templates
import psycopg2


app = FastAPI()

templates = Jinja2Templates(directory="templates")

def connect():
    connection = None
    db_data = None
    try:
        # Connexion a la bdd existante
        connection = psycopg2.connect(
            database="microservices",
            user="docker",
            password="docker",
            host="0.0.0.0"
        )

        # creation du curseur pour faciliter les opérations vers la bdd
        crsr = connection.cursor()
        # Requête à la bdd
        crsr.execute('SELECT name FROM utilisateur')
        db_data = crsr.fetchall()
        crsr.close()

        if db_data is None:
            print("Aucune donnée trouvée dans la base de données.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erreur de connexion à la base de données :", error)
    finally:
        if connection is not None:
            # fermer la connexion a la bdd
            connection.close()
            print('Connexion à la base de données terminée.')

    return db_data
print(connect())
# Création de la première route qui sera l'Acceuil
# def index():
#     return { "message": f"Hello {env['MY_VARIABLE']} !"}
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "my_variable": env['name']})


# Création de la deuxième route qui sera la page annexe
# def second_route():
#     return { "message": "Ceci est la deuxième route."}
@app.get("/second-route")
def index(request: Request):
    rows = connect()  # Appel de la fonction connect pour obtenir les données)
    return templates.TemplateResponse("annexe.html", {"request": request, "datas": rows })
