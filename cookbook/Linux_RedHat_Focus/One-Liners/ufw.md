# Limit SSH, so that brute force attacks will fail:

```
ufw limit ssh/tcp
```

#Allow Rules examples:

```
ufw allow from 192.168.1.106 proto tcp to any port 22

ufw allow from 192.168.1.106

ufw allow 6660:6670/tcp

ufw allow 22/tcp
```

#Deny Examples

```
ufw deny http

sudo ufw deny in on tun0 to any port 5900:6000 proto tcp
sudo ufw deny in on tun0 to any port 22 proto tcp

```

# Set all IPV6 to deny

```
#Config file /etc/ufw/ufw.confg

# Set to yes to apply rules to support IPv6 (no means only IPv6 on loopback
# accepted). You will need to 'disable' and then 'enable' the firewall for
# the changes to take affect.
IPV6=yes

#Disable/Enable ufw
```

# Display numbered rules then delete

```
ufw status numbered
ufw delete 10
```