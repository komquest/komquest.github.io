# Snort execute on NIC:
```
snort  -i en1 -u user -g usergroup -m0x11 -d -c ./etc/snort.conf
```

# Snort Read PCAPS
```
Run snort -h

   --pcap-single <tf>              Same as -r.
   --pcap-file <file>              file that contains a list of pcaps to read - read mode is implied.
   --pcap-list "<list>"            a space separated list of pcaps to read - read mode is implied.
   --pcap-dir <dir>                a directory to recurse to look for pcaps - read mode is implied.

```

# Parse through multiple files trick:

```
--pcap-list=$(/dir | tail -n 25 | tr '\n' ' ')

ls -d /dir/* | tail -n 25 | tr '\n' ' '
```

