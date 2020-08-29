#!/bin/bash
sudo groupadd -f docker
sudo usermod -aG docker $(whoami)
#env DATABASE_URI="${DATABASE_URI}"
#env MYSQL_ROOT_PASSWORD="${MYSQL_ROOT_PASSWORD}"
docker-compose build
docker-compose push 
docker stack deploy -c docker-compose.yaml 