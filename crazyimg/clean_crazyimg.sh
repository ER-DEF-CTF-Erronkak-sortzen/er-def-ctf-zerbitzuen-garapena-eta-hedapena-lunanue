#!/usr/bin/env bash

docker stop crazyimg_db_1 
docker stop crazyimg_ssh_1

docker rm crazyimg_db_1 
docker rm crazyimg_ssh_1 