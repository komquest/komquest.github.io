## Basic

```
nmap -sV -sC -oN academy.nmap 10.10.10.215
```

## Fast Scan for open Ports (standard Ports)

```
nmap -sT -n --open 10.10.10.215
```

## Fast Scan for open Ports (no ping verify) (all ports)

```
nmap -sT -Pn -n -p- --open 10.10.10.74
```

## Scan all ports and set a scan rate:

```
nmap -p- --min-rate=1000 -sV {target_IP}
```

## Run Vulnerablity Scripts (Vuln Scan)

```
nmap --script vuln -p445 10.10.10.100
```

## Check if vulnerable to ms17-010

```
nmap -p445 --script smb-vuln-ms17-010 192.168.151.40 

```

## Run Version and Discovery Scripts

```
nmap -sV --script="version,discovery" 10.10.10.11

sudo nmap -v -Pn -sV --script="version,discovery and not(dns-brute or targets-asn)" -p135 10.10.10.11
```

## Deep Version Discovery:

```
nmap -Pn -sV --version-all 10.10.10.11

--version-all --> runs all version detection capabilities
```

## Run all http Scripts execpt "http-brute" and "http-slowloris"

```
nmap -sV --script "(http-*) and not(http-slowloris or http-brute)" 10.10.10.11
```

## Os Vervsion Detection and Skip Host Discovery

```

nmap -sV -A -Pn 10.10.10.11

```


## Enmurate LDAP

```
nmap -sT -Pn -n --open -p389 --script ldap-rootdse 10.10.10.100
```


## **Definitions**

```
--> nmap -sC (Default Scripts) -sV(Enmurate Versions)
```

## **Find nmap script cats:**
--> This can help you only execute "safe" scripts

```
locate -r '\.nse$' | xargs grep categroies

locate -r '\.nse$' | xargs grep categroies | grep 'default\|version' | grep smb

```

## Run only Safe scripts

```
nmap --script safe -p445 10.10.10.100
```

## Service Detect Only a few ports

```
nmap -sV -sC -Pn -p9255,9256 -oN chatterbox.nmap 10.10.10.74
```

## Run SMB OS discovery

```
nmap -Pn --script smb-os-discovery.nse 10.10.10.4
```

## Run Scripts fast

```
nmap -sn --script ms-sql-dump-hashes 10.11.1.111

```

## nmap udp and tcp scan

```
sudo nmap -sU -sS -Pn --script smb-os-discovery.nse -p U:137,T:139 10.10.10.4
```

## Efficent UDP Scan, common ports only with limited version scanning:

```
sudo nmap -sUV -F --version-intensity 0 10.10.10.11

-F --> scan the most common 100 udp ports
--version-intensity --> choose test based off of port number
```

## Basic UDP Scan

```

sudo nmap -sU 10.10.10.11

```

## Ping scan for id of hosts on network:

```
sudo nmap -PEPM -sn -n 10.10.10.0/24
```


## Get Script Help:

```
nmap --script-help *sql*
```

## Insert Script Args:

```
--script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER
```

##  NMAP nse scripts location:

https://nmap.org/nsedoc/index.html

## NMAP Enmuration Windows:

http://www.lifeoverpentest.com/2018/02/enumeration-cheat-sheet-for-windows.html