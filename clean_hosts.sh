#1/usr/bin/env bash
for i in {0..4} 
do 
   ssh-keygen -f '/home/ubuntu/.ssh/known_hosts' -R host$i 
done
