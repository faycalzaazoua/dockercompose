# Résumé
C'est une Application web Python qui utilise FastAPI et Jinja2 pour créer une interface utilisateur permettant de visualiser et d'ajouter des utilisateurs à une base de données PostgreSQL. L'application est conteneurisée à l'aide de Docker, et l'infrastructure est orchestrée à l'aide de Docker Compose pour simplifier le déploiement. Deux conteneurs Docker (PostgreSQL et Adminer) sont obtenus à partir du Docker Hub, tandis que le conteneur Webapp est configuré localement. Les choix techniques incluent FastAPI pour sa rapidité, Jinja2 pour le rendu des modèles, Docker pour la portabilité, PostgreSQL (relationnel) pour la persistance des données, et Docker Compose pour la gestion des conteneurs. Pour le déploiement, AWS ou Azure sont des choix judicieux en raison de leur robustesse, de leur scalabilité et de leurs services de conteneurs, comme AWS ECS ou Azure Kubernetes Service, pour une gestion simplifiée de l'infrastructure.

# Architecture
<img src="templates/img/architecture.jpg">
<img src="templates/img/architecture2.jpg">

# Détail projet
* Front (2 routes : Accueil, Annexe)
<img src="templates/img/route.png">

* Backend avec BDD dans un conteneur spécifique :
  J'ai chois PostgreSQL, une base de données relationnelle qui offre une structure de données organisée et garantit la fiabilité grâce à la prise en charge des transactions ACID.
  Table : Utilisateur
<img src="templates/img/bdd.png">


* Le projet contient docker-compose & dockerfile.

* Image du projet sur DockerHub :
https://hub.docker.com/repository/docker/harcus78/microservice/general

* Build sans erreur : 
<img src="templates/img/build.png">

* Fichier de test bash : 
test/test_container.sh

* J'ai automatisé un test simple dans mon docker-compose.yml qui utilise l'image curl pour effectuer une requête HTTP vers le service "web". Le test vérifie que le service "web" est opérationnel en retournant un code d'état HTTP valide.

# Dashboard Kibana
 <img src="templates/img/kibana-dashboard.png">


# Lancement du projet
* Lancer le projet en lancant la commande : 
    docker-compose up --build <br>
    ou <br>
    docker-compose up --build -d pour lancer le projet en arrière blanc 


