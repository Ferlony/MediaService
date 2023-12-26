#!/bin/bash

while getopts "s:" var
do
   case "$var" in
       s) size=${OPTARG};;
   esac
done


create_disk() {
  dd if=/dev/zero of=$1 bs=1M count=$size
}


part_disk() {
  (
    echo g
    echo n
    echo p
    echo 1
    echo
    echo
    echo w
  ) | fdisk $1
}

create_disk multimedia_vdisk.img
create_disk transmission_vdisk.img

part_disk multimedia_vdisk.img
part_disk transmission_vdisk.img

yes | mkfs.ext4 multimedia_vdisk.img
yes | mkfs.ext4 transmission_vdisk.img

