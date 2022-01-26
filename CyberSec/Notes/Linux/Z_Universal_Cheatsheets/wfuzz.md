
--> Fuzz with cookie, ignoring 404 codes

```
wfuzz -c -b 'e1o8eoof0hc9qno7p15kghh7tb' --hc '404' -z file,/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt http://academy.htb/FUZZ.php
```


-->

```
wfuzz -c -v -z file,/usr/share/wordlists/rockyou.txt --hc 404 http://10.10.10.95:8080/cgi/FUZZ.bat

c --> color
v --> verbose
z --> payload
hc --> hide responses
```

-->Fuzz a range of numbers

 ```
wfuzz -c -z range,1-100 -s 1 https://git.laboratory.htb/api/v4/users/FUZZ
 ```


-->Fuzz some more interesting stuffs:

```
wfuzz -u http://logger.htb/room.php?cod=1FUZZ -w /usr/share/seclists/Fuzzing/special-chars.txt
```

 