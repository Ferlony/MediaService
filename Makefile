#TODO
#-------------
build:
	docker-compose -f docker-compose.yml build
up:
	#mount_files_path=$(awk -F "=" '/files/ {print $2}' ./src/main/python/config.ini)
	docker-compose -f docker-compose.yml up -d
	#docker run -v $mount_files_path:/

start:
	mount_files_path=$(awk -F "=" '/files/ {print $2}' ./src/main/python/config.ini)
	echo $mount_files_path
	docker-compose -f docker-compose.yml start
#==============


# Run a container using the `alpine` image, mount the `/tmp`
# directory from your host into the `/container/directory`
# directory in your container, and run the `ls` command to
# show the contents of that directory.
#docker run \
#    -v /tmp:/container/directory \
#    alpine \
#    ls /container/directory
#
# docker run -v /host/directory:/container/directory -other -options image_name command_to_run

#	cp configs/hypercorn_config.toml src/main/python/multi_parser/src/hypercorn_config.toml &&\ 
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

	#mkdir local &&\

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

	# rm config.ini &&\


remove-front:
	rm -rf src/main/resources/mediaservice/src/templates/js/node_modules/* &&\
	echo "front removed"
#	rm src/main/resources/mediaservice/src/templates/js/node_modules/*.json &&\
#	rm src/main/resources/mediaservice/src/templates/js/*.json &&\


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

