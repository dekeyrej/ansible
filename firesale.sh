#!/usr/bin/env bash
qm list | grep -v VMID | awk '{print $1}' > proxmoxkvm.list

for vmid in `cat proxmoxkvm.list`; do
     qm set $vmid --protection false
     qm stop $vmid
     qm destroy $vmid --purge
done

pct list | grep -v VMID | awk '{print $1}' > proxmoxlxc.list
for vmid in `cat proxmoxlxc.list`; do
     pct set $vmid --protection false
     pct stop $vmid
     pct destroy $vmid --purge
done
