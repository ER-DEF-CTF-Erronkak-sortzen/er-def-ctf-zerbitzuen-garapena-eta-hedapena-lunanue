#!/usr/bin/env bash

docker stop roses_ssh_1 
docker stop roses_www_1
docker stop roses_web_1
docker rm roses_ssh_1
docker rm roses_www_1
docekr rm roses_web_1