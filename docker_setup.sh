#!/bin/bash

set -e

# Make sure only root can run our script
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# backup old file
mkdir /root/backup/
mv /etc/network/interfaces /root/backup/

# set br0 bridge
echo "auto br0" > /etc/network/interfaces
echo "  iface br0 inet static" >> /etc/network/interfaces
echo "  address 10.1.1.3" >> /etc/network/interfaces
echo "  network 10.1.1.0" >> /etc/network/interfaces
echo "  netmask 255.255.255.0" >> /etc/network/interfaces
echo "  broadcast 10.1.1.255" >> /etc/network/interfaces
echo "  gateway 10.1.1.2" >> /etc/network/interfaces
echo "  bridge_ports enp11s0" >> /etc/network/interfaces
echo "  bridge_stp off" >> /etc/network/interfaces
echo "  bridge_fd 0" >> /etc/network/interfaces
echo "  bridge_maxwait 0" >> /etc/network/interfaces

# set dns servers
mv /etc/resolvconf/resolv.conf.d/base /root/backup/
echo "nameserver 8.8.8.8" > /etc/resolvconf/resolv.conf.d/base
ehco "nameserver 8.8.4.4" >> /etc/resolvconf/resolv.conf.d/base

# docker
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
apt-get update
apt-get install -y docker.io

# sleep for 10 seconds
sleep 10s

#reboot
reboot
