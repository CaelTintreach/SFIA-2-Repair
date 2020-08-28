#!/bin/bash
env DATABASE_URI="${DATABASE_URI}"
docker-compose build
docker-compose push 
docker stack deploy -c docker-compose.yaml 