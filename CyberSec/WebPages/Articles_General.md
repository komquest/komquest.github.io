# Windows us GPO to block USB devices
https://4sysops.com/archives/restrict-installation-of-usb-devices-using-group-policy/

# High level Guide on how Nats, with a mention of quic:

https://anderstrier.dk/2021/01/11/my-isp-is-killing-my-idle-ssh-sessions-yours-might-be-too/

# Linux Security Hardening and other tweaks, great for basic but effective hardening stuffs

https://vez.mrsk.me/linux-hardening.html

# Microsoft Ransomeware Defense Report,
-->Great read if you want to be better at blue team/defense best practices:

https://www.microsoft.com/security/blog/2020/04/28/ransomware-groups-continue-to-target-healthcare-critical-services-heres-how-to-reduce-risk/

Notes:


-RDP or Virtual Desktop endpoints without MFA
-itrix ADC systems affected by CVE-2019-19781
-Pulse Secure VPN systems affected by CVE-2019-11510
-Microsoft SharePoint servers affected by CVE-2019-0604
-Microsoft Exchange servers affected by CVE-2020-0688
-Zoho ManageEngine systems affected by CVE-2020-10189\

--------
Utilize host firewalls to limit lateral movement. Preventing endpoints from communicating on TCP port 445 for SMB will have limited negative impact on most networks, but **can significantly disrupt adversary activities**.

---------
Turn on attack surface reduction rules, including rules that can block ransomware activity:

-Use advanced protection against ransomware
-Block process creations originating from PsExec and WMI commands
-Block credential stealing from the Windows local security authority subsystem (lsass.exe)


# Great source on how to protect yourself from webshells.
**Also, the refs in this pdf are great**

https://media.defense.gov/2020/Apr/22/2002285959/-1/-1/0/DETECT%20AND%20PREVENT%20WEB%20SHELL%20MALWARE.PDF



# 40 Tips for hardening a Linux Server
https://www.cyberciti.biz/tips/linux-security.html

# Finally an article about the CIA hacking the Chinese
https://www.zdnet.com/article/chinese-security-firm-says-cia-hacked-chinese-targets-for-the-past-11-years/ 


# Good Stackoverflow about Python copying of abstract data types and links the difference between a shallow and deep copy.

https://stackoverflow.com/questions/5844672/delete-an-element-from-a-dictionary


# Why CloudFlare is switching to AMD based EPYC processors for their GenX servers:

https://blog.cloudflare.com/technical-details-of-why-cloudflare-chose-amd-epyc-for-gen-x-servers/



# What Hospitals can to do enhance CyberSecurity

https://www.zdnet.com/article/cybersecurity-do-these-ten-things-to-keep-your-networks-secure-from-hackers-hospitals-told/


# This is a high level explanation on what code signing is used for:
https://www.zdnet.com/article/ransomware-installs-gigabyte-driver-to-kill-antivirus-products/


# Alternative mySQL tables and querying
https://medium.com/@terjanq/blind-sql-injection-without-an-in-1e14ba1d4952


# Great Article on how API hooking works, with examples.
--> Some good tools as well

https://www.mdsec.co.uk/2019/11/rdpthief-extracting-clear-text-credentials-from-remote-desktop-clients/


# Basic Tips For Protecting a Windows based PC from ransomware. 
--> It has some good features like App white listing and disabling scripting host. 
https://www.bleepingcomputer.com/news/security/how-to-protect-and-harden-a-computer-against-ransomware/

# Medical/ICS exposure research article (with link to tools)

https://medium.com/@woj_ciech/when-%EA%93%98amerka-meets-healthcare-research-on-exposed-medical-devices-ac62f2840da4


# Simple Methods to Detect VPN traffic
https://www.comparitech.com/blog/vpn-privacy/how-easy-is-it-to-detect-a-vpn/


# Linux Enumeration CheatSheet
https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/


# SSH Hacks
--> (Setup SSH Port forwarding)
http://matt.might.net/articles/ssh-hacks/

# More Port Forwarding examples:
https://www.ssh.com/ssh/tunneling/example


# SMB Wireshark analysis howto:
https://401trg.com/an-introduction-to-smb-for-network-security-analysts/

# OptionsBleed Attack

https://blog.fuzzing-project.org/60-Optionsbleed-HTTP-OPTIONS-method-can-leak-Apaches-server-memory.html


# Al that copies voice only after 5 seconds of hearing:

https://google.github.io/tacotron/publications/speaker_adaptation/

# In depth look at finding vulnerabilities

https://www.youtube.com/watch?v=E-P9USG6kLs&edufilter=NULL 


# Find Trickbot using Wireshark, great tutorial on how to use wireshark to find malware

https://unit42.paloaltonetworks.com/wireshark-tutorial-examining-trickbot-infections/


# Abusing COM (Component Object Model) Registry Structure
https://bohops.com/2018/06/28/abusing-com-registry-structure-clsid-localserver32-inprocserver32/


# Google Auto Delete Account data after a certain amount of time
https://www.nytimes.com/2019/10/02/technology/personaltech/google-data-self-destruct-privacy.html


# Utah Power Grid DOS hit
https://www.cyberscoop.com/spower-power-grid-cyberattack-foia/


# What is mshta.exe? and how it is used.
https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/what-is-mshta-how-can-it-be-used-and-how-to-protect-against-it/

# Joker's Stash
https://www.cyberscoop.com/jokers-stash-data-breach-recorded-future/


# Electrum Wallet Redirect attack 2019
```
https://blog.malwarebytes.com/cybercrime/2019/04/electrum-bitcoin-wallets-under-siege/
```

```
https://venturebeat.com/
--> Tech News, business 
```



