build:
	docker-compose -f docker-compose.yml build

up:
	docker-compose -f docker-compose.yml up -d

start:
	docker-compose -f docker-compose.yml start -d

logs:
	docker-compose -f docker-compose.yml logs

build-back:
	cd src/main/python/ &&\
	if [ -d "multi_parser" ]; then \
    cd multi_parser && git pull origin main && cd .. ; \
	else \
		git clone https://github.com/Ferlony/multi_parser.git ;\
  fi &&\
	cd ../../.. &&\
	cp configs/media_service_config.ini src/main/python/config/config.ini &&\
	cp configs/parsers_config.ini src/main/python/multi_parser/src/config.ini &&\
	cd src/main/python/ &&\
	python3.11 -m venv venv &&\
	. venv/bin/activate &&\
	pip install -r requirements.txt &&\
	pip install -r multi_parser/requirements.txt &&\
	echo "back finished building"

build-front:
	echo "$PWD" &&\
	cd src/main/resources/mediaservice/src/templates/js/ &&\
	if [! -d "node_modules"]; then \
		mkdir node_modules;\
	fi &&\
	cd node_modules &&\
	npm i shaka-player &&\
	echo "front finished building"

remove-back:
	cd src/main/python/ &&\
	rm -rf venv/ &&\
	rm -rf multi_parser/ &&\
	echo "back removed"

remove-front:
	rm -rf src/main/resources/mediaservice/src/templates/js/node_modules/* &&\
	echo "front removed"


no-docker-build: build-back build-front

no-docker-remove: remove-back remove-front

no-docker-start:
	cd src/main/python/ &&\
	. venv/bin/activate &&\
	cd ../../.. &&\
	nohup python -m src.main.python.main_MediaService &

no-docker-logs:
	tail -f src/main/python/nohup.out


work-with-db:
	cd src/main/python/ &&\
	. venv/bin/activate &&\
	cd ../../.. &&\
	python -m src.main.python.db.user_worker_db

