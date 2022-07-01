#!/bin/bash

docker build -f Dockerfile -t ibm-test .
docker run -d -p 5000:5000 -v tmp:/src/api/data ibm-test

# docker-compose up