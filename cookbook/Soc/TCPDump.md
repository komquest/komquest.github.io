# "Universal" command to process VLAN and non-VLAN traffic:

```
tcpdump -Anr file.tcpdump '(not vlan and host 192.168.11.1) or (vlan and (udp or icmp or tcp) and host 192.168.11.1)'

or ?

tcpdump -Anr file.tcpdump '(host 192.168.11.1) or (vlan and (udp or icmp or tcp) and host 192.168.11.1)'
```

# Find if traffic you are collecting is on a VLAN or not:

```
timeout 1 tcpdump -i INT vlan
timeout 1 tcpdump -i INT not vlan 
```

# Use for vlans and networks without them:
(Note: this is still being tested since it appears that different data is being returned!)
(Note2: This doesn't return adequate results, see above for a better command)  

```
tcpdump -Anr file.tcpdump '(icmp && not vlan) || (vlan && icmp)'
tcpdump -Anr file.tcpdump '(icmp && not vlan) || (vlan && icmp)'
```

# Monitor a live interface and write to file
```
tcpdump -i en1 -n -w test.pcap tcp port 3306 and host 192.168.1.12
```

# Monitor a live interface for certain ssh traffic

```
tcpdump -i en1 tcp port 22 and not host 192.168.1.20
```

# Pull Host and port from multiple files then write binary:
```

for i in $(find -maxdepth 1 -type f | tail -n 10); do tcpdump port 445 and host 192.19.1.32 and host 192.137.18.179 -r $i -w ~/ben${i:2}.pcap; done
```

# editcap, split pcap files:

```
editcap.exe -c 1000000 .\tcpdump.pcap out.pcap
```

# Super loops, pull ports or IPs

```
for i in $(find -maxdepth 1 -type f | tail -n 10); do echo -e "-->$i"; cat $i | tcpdump -qns 0 -A  host 192.0.0.1 -r -; done
for i in $(find -maxdepth 1 -type f | sort | tail -n 50); do echo -e "-->$i"; cat $i | tcpdump -qns 0 -A  net 10.0.0.0/8 -r -; done | tee ~/out.txt
```

```
FILEPATH="~/dnsdump.txt";for i in $(find -maxdepth 1 -type f | tail -n 1); do echo $i | tee -a $FILEPATH; cat $i | tcpdump -qns 0 -A  port 53 -r - | egrep -i -A10 -B10 'microsoft.com' | tee -a $FILEPATH; echo -e "\n\n\n" | tee -a $FILEPATH ;done


FILEPATH="~/dnsdump.txt";for i in $(find -maxdepth 1 -type f | tail -n 1); do echo $i | tee -i $FILEPATH; cat $i | tcpdump -qns 0 -A  port 53 -r - | egrep -i -A10 -B10 'microsoft.com' | tee -ia $FILEPATH; echo -e "\n\n\n" | tee -ia $FILEPATH ;done
```

```
#Search though DNS for microsoft.com
for i in $(find -maxdepth 1 -type f | tail -n 1); do echo -e "-->$i"; cat $i | tcpdump -qns 0 -A  port 53 -r - | egrep --color --group-separator=$'\n\n' -i -A5 -B5 'microsoft.com'; done
```

**Note**
When tcpdump converts timestamps, you can no longer write it out as a pcap since the format has now changed, working on a way to convert it back.

# tcpdump flag explanation and cookbook commands:
https://danielmiessler.com/study/tcpdump/

# tcpdump filters explained:
https://docs.netgate.com/pfsense/en/latest/book/packetcapture/using-tcpdump-from-the-command-line.html

# Basic
```
tcpdump -qns 0 -A -r serverfault_request.pcap
tcpdump -qns 0 -X -r serverfault_request.pcap
```
