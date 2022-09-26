#!/bin/sh

docker build . -t jenkinsNTP -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):$(which docker)  -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
docker run -p=123:123/udp jenkinsNTP -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):$(which docker)  -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
