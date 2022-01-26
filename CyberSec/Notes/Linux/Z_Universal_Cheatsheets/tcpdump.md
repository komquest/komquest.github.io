## Use these commands to capture packets and output in pcap format!!!

```
sudo tcpdump -i en1 -n -w test.pcap tcp port 3306 and host 192.168.1.12
```

```
sudo tcpdump -i tun0 -n -w test.pcap tcp port 139
```