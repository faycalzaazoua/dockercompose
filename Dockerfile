# Utilise l'image Python 3.8.10 comme image de base
FROM python:3.8.10

# Définit le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copie tous les fichiers du répertoire local dans le répertoire de travail du conteneur
COPY . /app

# Exécute la commande pour installer les dépendances Python à partir du fichier "requirements.txt"
RUN pip3 install -r requirements.txt