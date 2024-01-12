#!/bin/bash

# Définissez le nom du conteneur
container_name="database-1"

# Commande à exécuter à l'intérieur du conteneur pour vérifier la connectivité (par exemple, ping ou une commande de base de données)
test_command="ping -c 4 google.com"  # Remplacez par la commande que vous souhaitez exécuter

# Exécutez la commande à l'intérieur du conteneur
docker exec "$container_name" $test_command

# Vérifiez le code de retour de la commande
if [ $? -eq 0 ]; then
    echo "le conteneur $container_name est fonctionnel."
else
    echo "un des conteneur $container_name n'est pas fonctionnel."
fi

container_name="elasticsearch"

docker exec "$container_name" $test_command

# Vérifiez le code de retour de la commande
if [ $? -eq 0 ]; then
    echo "le conteneur $container_name est fonctionnel."
else
    echo "un des conteneur $container_name n'est pas fonctionnel."
fi


container_name="kibana"

docker exec "$container_name" $test_command

# Vérifiez le code de retour de la commande
if [ $? -eq 0 ]; then
    echo "le conteneur $container_name est fonctionnel."
else
    echo "un des conteneur $container_name n'est pas fonctionnel."
fi
