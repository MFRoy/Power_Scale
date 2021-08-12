#!/bin/bash
docker login -u $(DOCKERHUUB_CREDENTIALS_USR) -p $(DOCKERHUUB_CREDENTIALS_PSW)
docker-compose build --parallel && \
docker-compose push