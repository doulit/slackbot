FROM ubuntu:18.04
# FROM alpine:3.9

RUN apt-get update && \
    apt-get install -y libssl-dev && \
    apt-get install -y python3-pip python3-dev && \
    apt-get clean

WORKDIR /code
# ADD requirements.txt /code/
RUN pip3 install websocket-client && pip3 install slackbot && pip3 install slackclient && pip3 install slacker && pip3 install nltk && pip3 install numpy
ADD . /code/

EXPOSE 8000

CMD ["python3", "/code/starterbot2.py"]