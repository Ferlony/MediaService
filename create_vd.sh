#!/bin/bash

while getopts "s:n:" var
do
   case "$var" in
       s) size=${OPTARG};;
       n) name=${OPTARG};;
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


create_disk $name.img
part_disk $name.img
yes | mkfs.ext4 $name.img
