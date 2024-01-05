up:
	VBoxManage startvm alpine-storage --type headless &&\
	sleep 60 &&\
	docker-compose up -d

start:
	VBoxManage startvm alpine-storage --type headless &&\
	sleep 60 &&\
	docker-compose start

build-back:
	cd src/main/python/ &&\
	if [ -d "multi_parser" ]; then \
        cd multi_parser && git pull origin main && cd .. ; \
	else \
		git clone https://github.com/Ferlony/multi_parser.git ;\
    fi &&\
    if [ ! -d "tmp" ]; then \
        mkdir tmp ; \
    fi &&\
	cd ../../.. &&\
	cp configs/media_service_config.ini src/main/python/config/config.ini &&\
	cp configs/parsers_config.ini src/main/python/multi_parser/src/config.ini &&\
	cd src/main/python/ &&\
	if [ ! -d "venv" ]; then \
		python3 -m venv venv ;\
	fi &&\
	. venv/bin/activate &&\
	pip install -r requirements.txt &&\
	pip install -r multi_parser/requirements.txt &&\
	echo "back finished building"

build-front:
	cd src/main/resources/mediaservice/src/templates/js/ &&\
	mkdir -p node_modules/ &&\
	cd node_modules/ &&\
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
	if [ -f "nohup.out" ]; then \
		cat /dev/null > nohup.out ; \
	fi &&\
	nohup python -m src.main.python.main_MediaService &

no-docker-logs:
	tail -f src/main/python/nohup.out


work-with-db:
	cd src/main/python/ &&\
	. venv/bin/activate &&\
	if [ ! -d "local" ]; then \
		mkdir local && cd local && touch db.sqlite3 && cd .. ;\
	else \
		cd local &&\
		if [ ! -f "db.sqlite3" ]; then \
			touch db.sqlite3 ; \
		fi &&\
		cd .. ;\
	fi &&\
	cd ../../.. &&\
	python3 -m src.main.python.db.user_worker_db --option 1

