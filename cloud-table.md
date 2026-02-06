| Task  |  Node  |  Task  |  Predecessor(s)  |
| ---  |  ---  |  ---  |  ---  |
| 1  |    |  Receive 3ea 100GbE NICs (Dell VC496) - 1Z63A9150390152527  |    |
| 2  |    |  Receive 2ea 8TB NVMes - no tracking ino  |    |
| 3  |    |  Receive 3ea 100GbE cables - 9361289733058880335171  |    |
| 4  |    |  Receive 100GbE Switch (Mikro Tik CRS 504-4XQ-IN)- 9434636207565287217186  |    |
| 5  |    |  Receive 2ea Rack-mount UPSes - no tracking info  |    |
| 6  |    |  Receive 25RU Rack - TBA327273620064 (Delivered)  |    |
| 7  |    |  Receive 25' 12/2 Power cord replacement with right-angle plug and Female Connector  |    |
| 8  |    |  Milestone: All hardware received  |  1,2,3,4,5,6,7  |
| 9  |    |  Assemble Rack (Comes flat-packed)  |  6,8  |
| 10  |    |  Run Extension from circuit 29 into storage room  |  7  |
| 11  |    |  Place Rack  |  9,10  |
| 12  |    |  Mount 2ea Rackmount UPSes - (UPS1 --> Circuit 19, UPS2 --> Circuit 29)  |  5,11  |
| 13  |  All  |  Poweroff Nodes  |  12  |
| 14  |  All  |  Disconnect power + network cables  |  13  |
| 15  |  bluep02  |  Install 100GbE NIC  |  1,14  |
| 16  |  bluep03  |  Install 100GbE NIC  |  1,14  |
| 17  |  bluep  |  Reinstall GPU  |  1,2,14  |
| 18  |  bluep  |  Install 100GbE NIC  |  17  |
| 19  |  bluep  |  Install 2ea 8TB NVMes  |  17  |
| 20  |  bluep  |  Remove 1ea 10TB HDD  |  18,19  |
| 21  |  bluep  |  Mount 6RU Server - (UPS 1)  |  14,20  |
| 22  |  bluep02  |  Mount 4RU Server - (UPS 2)  |  14,15  |
| 23  |  bluep03  |  Mount 4RU Server - (UPS 2)  |  14,16  |
| 24  |    |  (rear) Mount 100GbE Switch -  (UPS 1 + 2)  |  4,21,22,23  |
| 25  |  All  |  Connect servers to 100GbE Switch  |  3,24  |
| 26  |  All  |  Power on Nodes, verify clean boots  |  25  |
| 27  |    |  Validate link lights + basic iperf3 test  |  26  |
| 28  |  bluep  |  mdadm --create /dev/md0 --level=1 --raid-devices=2 --bitmap=internal /dev/sd{a,b}  |  27  |
| 29  |  bluep  |  sgdisk -n1:0:0 -t1:8300 /dev/md0  |  28  |
| 30  |  bluep  |  mkfs.ext4 /dev/md0p1  |  29  |
| 31  |  bluep  |  mkdir /mnt/bucket  |  30  |
| 32  |  bluep  |  echo "/dev/md0p1 /mnt/bucket ext4 defaults 0 2" >> /etc/fstab  |  31  |
| 33  |  bluep  |  mount -a  |  32  |
| 34  |  bluep  |  Validate mount + RAID health  |  33  |
| 35  |    |  Form Cluster/DataCenter  |  34  |
