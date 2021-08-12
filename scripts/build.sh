#!/bin/bash
docker login
docker-compose build --parallel && \
docker-compose push