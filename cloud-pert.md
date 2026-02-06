```mermaid
flowchart LR

  %% Legend:
  %% T# = Task #

  subgraph Deliveries
    T1["1: Receive 3x 100GbE NICs"]
    T2["2: Receive 2x 8TB NVMes"]
    T3["3: Receive 3x 100GbE cables"]
    T4["4: Receive 100GbE Switch"]
    T5["5: Receive 2x Rackmount UPSes"]
    T6["6: Receive 25RU Rack"]
    T7["7: Receive 25' 12/2 Power Cord"]
    T8["8: Milestone: All hardware received"]
    T1 --> T8
    T2 --> T8
    T3 --> T8
    T4 --> T8
    T5 --> T8
    T6 --> T8
    T7 --> T8
  end

  subgraph Rack_and_Power
    T9["9: Assemble Rack"]
    T10["10: Run extension from circuit 29"]
    T11["11: Place Rack"]
    T12["12: Mount 2x Rackmount UPSes (19/29)"]
    T8 --> T9
    T6 --> T9
    T7 --> T10
    T9 --> T11
    T10 --> T11
    T5 --> T12
    T11 --> T12
  end

  subgraph Node_Powerdown_and_Disconnect
    T13["13: Power off Nodes"]
    T14["14: Disconnect power + network cables"]
    T12 --> T13
    T13 --> T14
  end

  subgraph Node_Internal_Work
    T15["15: bluep02: Install 100GbE NIC"]
    T16["16: bluep03: Install 100GbE NIC"]
    T17["17: bluep: Reinstall GPU"]
    T18["18: bluep: Install 100GbE NIC"]
    T19["19: bluep: Install 2x 8TB NVMes"]
    T20["20: bluep: Remove 1x 10TB HDD"]
    T14 --> T15
    T1 --> T15

    T14 --> T16
    T1 --> T16

    T14 --> T17
    T1 --> T17
    T2 --> T17

    T17 --> T18
    T17 --> T19
    T18 --> T20
    T19 --> T20
  end

  subgraph Rack_Mount_Servers_and_Switch
    T21["21: bluep: Mount 6RU (UPS1)"]
    T22["22: bluep02: Mount 4RU (UPS2)"]
    T23["23: bluep03: Mount 4RU (UPS2)"]
    T24["24: Mount 100GbE Switch (UPS1+2)"]

    T20 --> T21
    T14 --> T21

    T15 --> T22
    T14 --> T22

    T16 --> T23
    T14 --> T23

    T4 --> T24
    T21 --> T24
    T22 --> T24
    T23 --> T24
  end

  subgraph Network_Up
    T25["25: Connect servers to 100GbE Switch"]
    T26["26: Power on Nodes, verify clean boots"]
    T27["27: Validate link lights + basic iperf3"]

    T3 --> T25
    T24 --> T25
    T25 --> T26
    T26 --> T27
  end

  subgraph RAID_and_Filesystem_on_bluep
    T28["28: mdadm create /dev/md0 (RAID1)"]
    T29["29: Partition RAID (/dev/md0)"]
    T30["30: mkfs.ext4 /dev/md0p1"]
    T31["31: mkdir /mnt/bucket"]
    T32["32: Add fstab entry"]
    T33["33: mount -a"]
    T34["34: Validate mount + RAID health"]

    T27 --> T28
    T28 --> T29
    T29 --> T30
    T30 --> T31
    T31 --> T32
    T32 --> T33
    T33 --> T34
  end

  subgraph Cluster_Form
    T35["35: Form Cluster/DataCenter"]
    T34 --> T35
  end
  ```