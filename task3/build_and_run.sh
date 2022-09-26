#!/bin/sh

docker build . -t jenkinsNTP
docker run -p=123:123/udp jenkinsNTP
