# Pull out an IP

--> This shows you can rewrite fields on the fly

```
#String:
./client_logs/192.168.210.5.log

#Command:
index="a_iplogs2" earliest=0 | eval sourcetype=(sourcetype + date_zone) 
| rex field=source "(?<source>\d+[.]\d+[.]\d+[.]\d+)" 
|  rename source as "IP_ADDRESS"


#Out:
192.168.210.5

```

# Rex

-->Remember: Rex makes new fields, Regex pulls data based off of field.

```
#String:
Aug 10 20:01:56 vagrant sudo:  vagrant : TTY=pts/0 ; PWD=/home/vagrant ; USER=root ; COMMAND=/bin/ss -tulp

#Command:
sourcetype=syslog sudo | rex field=_raw "sudo:.*COMMAND\=(?<X_KOMAND>.*)"

#Out:
/bin/ss -tulp
```
