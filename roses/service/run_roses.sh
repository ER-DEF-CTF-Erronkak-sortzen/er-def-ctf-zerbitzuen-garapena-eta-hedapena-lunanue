#!/usr/bin/env bash

docker-compose -f "$SERVICES_PATH/roses/docker-compose.yml" up -d --build