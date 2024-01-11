from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
import psycopg2
from elasticsearch import Elasticsearch
import uvicorn
from os import environ as env

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Paramètres de connexion à la base de données PostgreSQL
db_params = {
    'host': '172.19.0.2',
    'database': 'microservices',
    'user': 'docker',
    'password': 'docker',
}

# Paramètres de connexion à Elasticsearch
es = Elasticsearch(["http://elasticsearch:9200"])

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "my_variable": env['name']})

@app.get("/second-route")
def second_route(request: Request):
    try:
        # Établir la connexion à la base de données PostgreSQL
        conn = psycopg2.connect(**db_params)

        # Créer un curseur
        cursor = conn.cursor()

        # Exécuter une requête SQL pour récupérer les données de votre table PostgreSQL
        cursor.execute('SELECT * FROM utilisateur')

        # Récupérer les résultats
        rows = cursor.fetchall()

        # Fermer le curseur et la connexion à la base de données PostgreSQL
        cursor.close()
        conn.close()

        # Rendre le modèle HTML avec les données récupérées
        return templates.TemplateResponse("annexe.html", {"request": request, "rows": rows, "my_variable": env['name']})

    except Exception as e:
        return f"Erreur lors de la connexion à la base de données PostgreSQL : {e}"

@app.get("/search")
def search(request: Request, query: str):
    try:
        # Effectuer une recherche dans Elasticsearch
        result = es.search(index="votre_index", body={"query": {"match": {"votre_champ": query}}})

        # Rendre le modèle HTML avec les résultats de la recherche
        return templates.TemplateResponse("search.html", {"request": request, "result": result})

    except Exception as e:
        return f"Erreur lors de la recherche dans Elasticsearch : {e}"
