# Examples
```bash
#Build Partition
parted -l
parted /dev/sdb
mkpart

#Format and make label
mkfs.ext4 /dev/sdb1
e4label /dev/sdb1 disk2-part1
```
