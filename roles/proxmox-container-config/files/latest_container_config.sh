#!/bin/bash
apt update
apt install -y openssh-server
systemctl enable --now ssh
[ -f /etc/sudoers.d/99-sudo-nopasswd ] || echo '%sudo ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/99-sudo-nopasswd
chmod 440 /etc/sudoers.d/99-sudo-nopasswd
adduser --disabled-password --gecos "" ubuntu
usermod -aG adm,sudo ubuntu
install -d /home/ubuntu/.ssh
if [ -f /root/.ssh/authorized_keys ] && [ ! -f /home/ubuntu/.ssh/authorized_keys ]; then
  mv /root/.ssh/authorized_keys /home/ubuntu/.ssh/authorized_keys
fi
chown -R ubuntu:ubuntu /home/ubuntu/.ssh
chmod 700 /home/ubuntu/.ssh
chmod 600 /home/ubuntu/.ssh/authorized_keys
