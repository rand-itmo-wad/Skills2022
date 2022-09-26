#!/bin/sh

docker build . -t jenkinsNTP -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):$(which docker)
docker run -p=123:123/udp jenkinsNTP -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):$(which docker)
