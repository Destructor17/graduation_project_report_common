FROM ubuntu

RUN apt-get update
RUN apt-get install -y librsvg2-bin
RUN apt-get install -y make python3
