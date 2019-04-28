#!/usr/bin/env bash

git clone -b master https://github.com/roman-rk/innoreport-persistence.git --depth=1

cd innoreport-persistence

docker build --no-cache -f user-persistence/infrastructure/Dockerfile -t innoreportpersistenceuser .

docker run -d -e FLASK_APP='user-persistence/user_persistence.py' \
 -e LC_ALL='C.UTF-8' \
 -e LANG='C.UTF-8' \
 -p 5001:5001 innoreportpersistenceuser:latest