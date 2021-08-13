#!/bin/bash

scp $WORKSPACE/docker-compose.yaml jenkins@swarm-master


ssh -i ~/.ssh/ansible_id_rsa jenkins@swarm-master "export DATABASE_URI=$DATABASE_URI && docker stack deploy --compose-file docker-compose.yaml project1"
