docker-compose -d

mount_files_path=$(awk -F "=" '/files/ {print $2}' ./src/main/python/config.ini)


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

