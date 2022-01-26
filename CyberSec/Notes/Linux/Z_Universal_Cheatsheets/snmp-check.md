--> Scan for open snmp:

```
snmp-check 10.10.10.20 -c public
```


--> Get all strings from public snmp

```
snmpwalk -v2c -c public 10.10.10.20
```

--> Download MIBs, and use them to get named OIDs, thus making it much more readable:

```
1. https://github.com/trevoro/snmp-mibs
2. Modify /etc/snmp/snmp.conf to enable mibs
3. snmpwalk -Os -c public -v 1 -M -./mibs/ 10.10.10.20

ref: https://standalone-sysadmin.com/ubuntu-and-snmp-b8d1244eea42
```