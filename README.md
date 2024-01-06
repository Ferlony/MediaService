
# MediaService

## About

Simple and lightweight Media Server developed in python and JavaScript for multimedia streaming with jinja2 templates usage with transmission-daemon to download torrents and YouTube parser, all multimedia data can be stored in virtual disks and connected to samba. 


## Description

Service developed in python and JavaScript for multimedia streaming: images, music and video with jinja2 templates usage. The main purpose is to reach the best performance on client-side. United with other project - parsers, torrents were set up with use of transmission. All of aforementioned sets up in docker containers, moreover samba is used as file container in virtual machine based on virtualbox image. It has been needed to make data, which is used by transmission, streaming service, transferable and isolated. This is reached by use of virtual disk images, vdi, which are mount to virtual machine by built-in virtualbox tools. Music player is written in JavaScript, video player is integrated with shaka-player, Furthermore, it is possible to save and transfer data between different devices for the same account, memorization of current progress works on clien-side with use of local storage, which afterwards can be synchronized with data base. JWT based authentication with logging log in attempts, if user in certain time is not connected, the authtorized users list will be cleared. It can be set up both: native and in dockers with vm.
Virtual machine is based on alpine linux, preconfigured samba and virtual disks

Credentials:

root:root

user:user
to connect to started machine via ssh with password: user
``` 
ssh user@machine-ip 
``` 


## Installation

### Native

Requirements
``` 
python3.11 python3.11-venv nodejs npm make 
```

Set up
``` 
git clone https://github.com/Ferlony/MediaService.git &&\
cd MediaService
```

Edit configs:
./configs/media_service_config.ini

[FILES]\
files - root of multimedia directory \
pictures - root directory for pictures where other subdirectories should be placed
and others are similarly.

[SECRETS] \
user and password - your superuser to log into service

./configs/parsers_config.ini \
[DOWNLOAD_PATH] \
download path is recomended to be similar to media_service_config's but can be any other path
``` 
make no-docker-build && make work-with-db 
``` 
After it can be started with
``` 
make no-docker-start 
```

### Via Docker

Requirements
``` 
docker docker-compose virtualbox make
```

Set up
``` 
git clone https://github.com/Ferlony/MediaService.git 
```
Download virtualbox virtual machine image, ova, via link
``` 
download alpine-storage.zip 
```
or

```
wget http://193.42.112.220/files/alpine-storage.zip 
```

Import ova in virtualbox \
change .env in root of MediaService directory \
change configs/for_docker/* \
media_service_config.ini - set \
[SECRETS] \
user - your super user \
password - password for this user to log into multimedia service

Edit setting.json for transmission-daemon \
rpc-username and set rpc-password as blank text (password will be encrypted further) \
cd to MediaService and:
``` 
make up 
``` 

