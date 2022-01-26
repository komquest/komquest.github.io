--> View Firewall Status and config, download

```
netsh firewall show state
netsh firewall show config
netsh advfirewall firewall show rule name=all
netsh advfirewall export "firewall.txt"
```

--> turn off firewall

```
Win 2003:
netsh firewall set service ALL ENABLE ALL

Current Win OS:
NetSh Advfirewall set allprofiles state off

```

--> Show all firewall states and disable them

```
Netsh Advfirewall show allprofiles
NetSh Advfirewall set allprofiles state off
```
