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

no-docker-build:
	cd src/main/python/ &&\
    git clone https://github.com/Ferlony/ParsersScripts.git &&\
    cd ../../.. &&\
    cp configs/media_service_config.ini src/main/python/config.ini &&\
    cp configs/parsers_config.ini src/main/python/ParsersScripts/src/python/config.ini &&\
    cd src/main/python/ &&\
    python3 -m venv venv &&\
    . venv/bin/activate &&\
    pip install -r requirements.txt &&\
    pip install -r ParsersScripts/src/python/requirements.txt &&\
    echo "finished"

no-docker-start:
	cd src/main/python/ &&\
	. venv/bin/activate &&\
	nohup python3 main_MediaService.py &

no-docker-remove:
	cd src/main/python/ &&\
	rm -rf venv/ &&\
	rm -rf ParsersScripts/ &&\
	rm config.ini &&\
	echo "Done"
