#!/bin/bash

rsync docker-compose.yaml swarm-master:

ssh swarm-master << EOF
docker stack deploy --compose-file docker-compose.yaml project1
EOF