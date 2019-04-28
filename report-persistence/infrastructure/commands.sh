#!/usr/bin/env bash

git clone -b master https://github.com/roman-rk/innoreport-persistence.git --depth=1

cd innoreport-persistence

docker build --no-cache -f report-persistence/infrastructure/Dockerfile -t innoreportpersistencereport .

#docker run -d -p 5000:5000 -e FLASK_APP=report-persistence/report_persistence.py -e LC_ALL=C.UTF-8 -e export LANG=C.UTF-8 innoreportpersistencereport:latest

docker run -d -e FLASK_APP='report-persistence/report_persistence.py' \
 -e LC_ALL='C.UTF-8' \
 -e LANG='C.UTF-8' \
 -p 5000:5000 innoreportpersistencereport:latest
