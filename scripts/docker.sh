#!/bin/bash
sudo groupadd -f docker
sudo usermod -aG docker $(whoami)
sudo chmod 666 /var/run/docker.sock
env DATABASE_URI="${DATABASE_URI}"
env MYSQL_ROOT_PASSWORD="${MYSQL_ROOT_PASSWORD}"
docker-compose build
docker-compose push 
docker stack deploy --compose-file docker-compose.yaml stacktest