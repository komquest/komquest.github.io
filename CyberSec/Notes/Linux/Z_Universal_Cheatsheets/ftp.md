## Anonymous access:

```
ftp 10.10.10.98
Login: anonymous
Password: <press enter>
```

## Get Filename with Spaces

```
get "File Name"
```

## Set Binary Mode, if you are downloading stuff other than txt files

```
binary
```

## Set ASCII Mode


```
ascii
```

## Note on FTP and firewalls:

---
That typically happens as nowadays most client machines are behind a firewall or NAT or both, what prevents the FTP active mode from working. **To make the active mode working you need to open your firewall (not recommended) and/or configure NAT routing rules.** 


## Download patterns(recursive):

```
# Set prompt to off
prompt

mget *
```

## Connect with passive mode

```
pftp 10.11.1.8
```