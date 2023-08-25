FROM python:3.11


RUN cd src/main/python/ &&\
    git clone https://github.com/Ferlony/ParsersScripts.git &&\
    cp configs/media_service_config.ini src/main/python/config.ini &&\
    cp configs/parsers_config.ini src/main/python/ParsersScripts/src/python/config.ini &&\
    python -m venv venv &&\
    source venv/bin/activate &&\
    pip install -r requirements.txt &&\
    pip install -r ParsersScripts/src/python/requirements.txt


WORKDIR /src/main/python/

CMD["python", "main_MediaService.py"]
