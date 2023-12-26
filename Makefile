build:
	docker-compose -f docker-compose.yml build

up:
	docker-compose -f docker-compose.yml up -d

start:
	docker-compose -f docker-compose.yml start -d

logs:
	docker-compose -f docker-compose.yml logs

create-vd:
	./create_vd.sh -s 1024 &&\
	
	if [ ! -d "storage" ]; then \
  		mkdir storage; \
	fi &&\
	mv multimedia_vdisk.img storage/ &&\
	mv transmission_vdisk.img storage/


build-back:
	cd src/main/python/ &&\
	git clone https://github.com/Ferlony/multi_parser.git &&\
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
	cd src/main/resources/mediaservice/src/templates/js/node_modules/ &&\
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

