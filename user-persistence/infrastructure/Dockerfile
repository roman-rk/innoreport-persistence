FROM ubuntu:latest

MAINTAINER Roman

RUN apt-get update -y

RUN apt-get install -y python3 python3-dev python3-pip
RUN pip3 install flask
RUN pip3 install neo4j-driver py2neo

COPY . /innoreport-persistence
WORKDIR /innoreport-persistence

EXPOSE 5001

#ENTRYPOINT ["python"]

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]