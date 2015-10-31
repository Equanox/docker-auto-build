#run cmds
#RUP sudo docker run -d -p 127.0.0.1:8080:9001 --restart=always --name=%name% %name%
#RUD sudo docker run -i -t -p 127.0.0.1:8080:9001 --restart=always --name=%name% %name% /bin/bash
FROM ubuntu:14.04

RUN apt-get -y upgrade -y && apt-get -y update

RUN apt-get -y install python3-pip
RUN pip3 install tornado

ADD dab dab 
EXPOSE 9001 9001

ENTRYPOINT python3 dab/examples/server.py



