FROM alpine

RUN apk add --update
RUN apk add openrc --no-cache
RUN apk add git
RUN apk add transmission-daemon
RUN apk add python3
RUN apk add py3-pip
RUN rm -rf /var/cache/apk/*

# debian
#RUN apt update
#RUN apt install git
#RUN apt install transmission-daemon --install-suggests -y

#RUN systemctl stop transmission-daemon.service

#RUN rc-service transmission-daemon stop

RUN git clone -b dev https://github.com/Ferlony/MediaService &&\
    cd MediaService/ &&\
    cd src/main/python/ &&\
    git clone https://github.com/Ferlony/ParsersScripts.git &&\
    cd ../../.. &&\
    cp configs/media_service_config.ini src/main/python/config.ini &&\
    cp configs/parsers_config.ini src/main/python/ParsersScripts/src/python/config.ini &&\
#    cp configs/setting.json /etc/transmission-daemon/ &&\
    cd src/main/python/ &&\
    python3 -m venv venv &&\
    source venv/bin/activate &&\
    pip install -r requirements.txt &&\
    pip install -r ParsersScripts/src/python/requirements.txt

RUN echo hi
RUN rc-service transmission-daemon start
#RUN systemctl start transmission-daemon.service

VOLUME ["/MediaService/src/main/python/"]

EXPOSE 8000:8000
EXPOSE 8001:8001
EXPOSE 51413/tcp 51413/udp

CMD ["python3", "/MediaService/src/main/python/main_MediaService.py"]
