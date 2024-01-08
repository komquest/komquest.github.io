## Links

--> Hash index

https://hashcat.net/wiki/doku.php?id=example_hashes

--> Zip file modes:

https://forum.hackthebox.eu/discussion/3783/zip-password-crack

--> Download

https://hashcat.net/hashcat/

**Note:** wsl can run the downloaded .exe!!!

--> Password Lists

https://github.com/danielmiessler/SecLists/tree/master/Passwords

--> Tutorials

- https://laconicwolf.com/2018/09/29/hashcat-tutorial-the-basics-of-cracking-passwords-with-hashcat/
- https://laconicwolf.com/2019/03/29/hashcat-tutorial-rule-writing/
- https://www.4armed.com/blog/hashcat-rule-based-attack/


---

</br>

## Notes

- Hashcat saves it's cracked hashes in a ".pot" file located in ~/.hashcat

</br>

## Codes

## Basic run with downloaded .exe from wsl: (Start in same dir as .exe!!!)

```
./hashcat.exe -m 17225 ../node.pass ../Hob0Rules/wordlists/rockyou.txt ./rules/best64.rule
```

## Crack linux passwd/shadow file hashes:\

--> SHA-512
$6$blDsHpU9$1.jyQg4uduSokEQ9Jgvo.5WkyUW52zP1XPT/PaA54y4y1ozS0WwrYcYUjfLZkBxx85gU2ROt5OpnoR5bDnbJX1
```
./hashcat.exe -O -m 1800 ../passwd.pass ../Hob0Rules/wordlists/rockyou.txt ./rules/best64.rule
```

--> MD5

```
./hashcat.exe -O -m 500 ../passwd.pass ../Hob0Rules/wordlists/rockyou.txt ./rules/best64.rule
```

--> PHP
$P$BR2C9zC2Aau72.4cNZfJPC.iV8Ppj41
./hashcat.exe -O -m 400  .\HASHES\php_bigtree.txt rockyou.txt .\rules\best64.rule



$1$ is MD5
$2a$ is Blowfish
$2y$ is Blowfish
$5$ is SHA-256
$6$ is SHA-512

## HashCat Crack Kerberos

https://www.blackhillsinfosec.com/a-toast-to-kerberoast/
$krb5tgs$23$

```
./hashcat.exe -O -m 13100 ../passwd.pass ../Hob0Rules/wordlists/rockyou.txt ./rules/best64.rule
```

## HashCat Crack NTLM

--> Hash mode #1000
```
./hashcat.exe -O -m 1000 ./HASHES/ntlm.txt ../Hob0Rules/wordlists/rockyou.txt ./rules/*
```

## Hashcat Crack linux SHA5121crypt

```
./hashcat.exe -O -m 1800 ./HASHES/sha512crypt ./rockyou.txt ./rules/*
```

## Hashcat Crack MD5 With Salt

**MD5 with Salt**

```
hashcat -m 20 -a 0 -O pass.txt rockyou.txt
```

**MD5 With Salt, Optimized for GPU**

```
hashcat -m 20 -a 0 -O pass.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

## MD5 Raw

```

hashcat -m 0 -a 0 ./md5password.txt  /usr/share/wordlists/rockyou.txt

```

## Hashcat with For ZIP files:

```
zip2john encrypted.zip > ziphash.txt
hashcat.exe -m 13600 -a 0 ./ziphash.txt ./wordlists/rockyou.txt

## NOTE: This does not work due to a john developer thing, use john the ripper for zip password cracking or fcrackzip

```

## Use hashcat to generate password list:

```
hashcat --force --stdout -r /usr/share/hashcat/rules/best64.rule password.lst
```

## Search for Hash types with hashcat

```
./hashcat --example-hashes | grep "Your hash"
```

