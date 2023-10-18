from fastapi import FastAPI, Request
from os import environ as env
from starlette.templating import Jinja2Templates
import psycopg2


app = FastAPI()

templates = Jinja2Templates(directory="templates")

async def connect():
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
        await crsr.execute('SELECT name FROM utilisateur WHERE id=1')
        db_data = crsr.fetchone()
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

# def index():
#     return { "message": f"Hello {env['MY_VARIABLE']} !"}
@app.get("/")
async def index(request: Request):
    row = await connect()  # Appel de la fonction connect pour obtenir les données)
    return templates.TemplateResponse("index.html", {"request": request, "my_variable": env['name']})


# def second_route():
#     return { "message": "Ceci est la deuxième route."}
@app.get("/second-route")
def index(request: Request):
    return templates.TemplateResponse("annexe.html", {"request": request})
