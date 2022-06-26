#!/bin/bash

docker build -f Dockerfile -t ibm-test .
docker run -d -p 6000:6000 -v tmp:/src/api/data ibm-test