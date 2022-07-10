
---
Dubbed **SessionManager**, the malicious software poses as a legitimate module for Internet Information Services (IIS), the web server installed by default on Exchange servers. Organizations often deploy IIS modules to streamline specific processes on their web infrastructure. Researchers from security firm Kaspersky have identified 34 servers belonging to 24 organizations that have been infected with SessionManager since March 2021. As of earlier this month, Kaspersky said, 20 organizations remained infected.

---
piled on with additional claims for **copyright infringement, false designation, business defamation, breach of contract, and violations of consumer protection law.**

---
SMS has a field called sender ID, which is set by the sender, requires no identity verification, and can be any arbitrary short string.

This allows anyone to send messages to any number, identifying themselves as whoever they want to impersonate.

---
I’ll say it because it needs to be said: The United States government is in urgent need of leadership on cybersecurity at the executive branch level — preferably someone who has the authority and political will to eventually disconnect any federal government agency data portals that fail to enforce strong, multi-factor authentication.

---
 KVM and Xen have a smaller attack surface and are known to have a better isolation model, but I'm sure there are still plenty of exploits given enough resources.

KVM - the low-level kernel-level hypervisor - has a tiny attack surface and has been audited exhaustively. It's unlikely to have critical bugs in it.

When people talk about "KVM vulnerabilities", they're usually talking about vulnerabilities in QEMU, which implements the actual device emulation. QEMU has all of the attack surface, deals with low-level data shuffling, and is written in C. Even worse, most stock QEMU-KVM deployments simply run qemu as root with no extra sandboxing or MAC like SELinux/sVirt. It's very likely that a bunch of 0days exist for those environments.

This is why many cloud providers use KVM-the-kernel-module, but an in-house replacement for QEMU.

Fortunately, there's a growing ecosystem of QEMU replacements written in Rust:

- https://github.com/cloud-hypervisor/cloud-hypervisor

- https://github.com/firecracker-microvm/firecracker

- https://chromium.googlesource.com/chromiumos/platform/crosvm... (the Chrome OS VM runtime which Firecracker was forked from)

Google's gVisor - the sandbox that App Engine and Cloud Run uses - uses KVM as well: https://gvisor.dev/docs/

With an emulation layer written in a language like Rust, the trust boundary is much better.

As for VirtualBox in particular - that one should not be considered a trust boundary. Nobody is seriously using it in production, and it's regularly featured in CTF competitions as a fun exploitation target. 

---
The domain must not contain certain strings; ```the check for these strings is implemented via hashes```, so at this time the domain names that are block-listed are unknown

---
These are websites that use top-level domains (TLDs) managed by Emercoin, a blockchain company. ```Records for these domains are stored inside a blockchain and cannot be transferred to anyone else without the domain owner's cryptographic signature.```

"Notably, JokerStash was one of the original proponents of moving dark web services to Blockchain technology."

---
```This is why PAAS rocks```

Your apps run inside smart containers in a fully managed runtime environment, ```we handle everything critical for production — configuration, orchestration, load balancing, failovers, logging, security, and more.```

https://www.heroku.com/

---
Perhaps the most effective means of preventing ransomware outbreaks is to ```implement application controls, which ensure only approved binaries are allowed to execute in the environment.```


---
 you can create a ```“crypto canary”``` on your file servers to notify you when Ryuk or other families encrypt file shares. 

--> Windows File Shares Only

---
We immediately notified the customer and our mutual incident response partner, Kroll. ```Acting swiftly, Kroll began executing response processes including isolating endpoints and banning malicious binaries, as our CIRT continued to publish detections for the escalating lateral movement and credential theft.```

---
Bypass all possible ```Windows Security Defenses```:

- SMEP
- Kernel DEP
- KASLR
- Integrity Level (escape from Low)
- Null Dereference Protection
- UAC

---
As the CEO of the OLED Association, he also argues that OLED displays provide the same responsiveness as CRT monitors because they also involve electron-to-photon conversion, only with organic chemicals (the "O" in OLED is for organic) receiving the voltage instead of phosphor dots.

```"There's really no difference between OLEDs and CRTs," Young said.```


---
But judging from the proliferation of help-wanted ads for offensive pentesters in the cybercrime underground, ```today’s attackers have exactly zero trouble gaining that initial intrusion```

That’s because it usually ```takes time and a good deal of effort for intruders to get from a single infected PC to seizing control over enough resources within the victim organization where it makes sense to launch the ransomware.```

At that point, control over the victim machine may be transferred or sold multiple times between different cybercriminals who specialize in exploiting such access. ```These folks are very often contractors who work with established ransomware groups, and who are paid a set percentage of any eventual ransom payments made by a victim company.```

“But because of the rapidly growing market for compromised accesses and the fact that these could be sold to anyone, ```organizations need to focus more on efforts to understand, detect and quickly respond to network compromises,”```

which variously claims to be based in the ```offshore company havens of Belize and the Seychelles```

---
# Splunk Education:

```If you are interested in other workshops - you can find future dates & topics here -``` 
https://www.carahsoft.com/doyouknowsplunk#virtual-workshops

```Splunk .conf```

https://conf.splunk.com

---
The company said it discovered these attacks after ```two computers were flagged by the company's Firmware Scanner``` module as suspicious.

---
Microsoft has released on Friday a new tool that will allow system ```administrators to update the Defender security package inside Windows installation images``` (WIM or VHD supported). 

https://www.zdnet.com/article/microsoft-releases-tool-to-update-defender-inside-windows-install-images/

---
Another possibly use is to ```create a baseline of tools writing to the clipboard``` and create some detection logic on anomalies.

Sysmon event 24

---
Performing ```frequency analysis``` on the IIS logs could indicate the location of a malicious virtual directory.

---
commonly used staging directories ```(recycle bin, temp folders, etc.)```

---
The tooling STRONTIUM is using routes its authentication attempts through a pool of approximately 1,100 IPs, the ```majority associated with the Tor anonymizing service.```

---
Analysts from ```Microsoft Threat Intelligence Center (MSTIC)``` and ```Microsoft Identity Security``` have been tracking this new activity since April 2020.

---
The ComputeNetlogonCredential function, ```however, defines that this IV is fixed and should always consist of 16 zero bytes```. This violates the requirements for using AES-CFB8 securely: its security properties only hold when IVs are random

---
```Netlogon``` is a Windows Server process that authenticates users and other services within a domain. Since it is a service and not an application, Netlogon continuously runs in the background, unless it is stopped manually or by a runtime error. Netlogon can be stopped or restarted from the command-line terminal.

```If Netlogon is stopped```, many Windows Server functions are affected as users can no longer log in to their accounts and the domain controller cannot automatically register Domain Name System records, which contain user login information.

---
In my experience - best phrasing is:
1) based on evidence it is reasonable to conclude that XYZ data was stolen by attacker
2) in my professional opinion - XYZ data was stolen by attacker 

```Both aren’t stating a fact - but a logical or/or informed conclusion from the evidence```

---
Exactly because it takes moxie to hack into something and straight fucking own em... ```Easier $$ being the cyber arms dealer``` ... one stop shop cop n roll

---
Buying identities was so much better for them than stolen payment card data, because card data could be used once or twice before it was no good to them anymore. ```But identities could be used over and over again for years.```”

---
```TLO’s service is accessible to law enforcement agencies and to a limited number of vetted professionals who can demonstrate they have a lawful reason to access such information.``` In 2014, TLO was acquired by Trans Union, one of the other three big U.S. consumer credit reporting bureaus.

Legal Data brokers to help law enforcement 

---
Virtual  currency  exchanges  doing  business  in  the  United  States  are regulated  under the ```Bank Secrecy Act```, codified  at 31 U.S.C. § 5311 et seq.,  and  must  collect   identifying   information   of  their  customers  and  verify  their  clients’  identities.

---
Over the subsequent months, the funds were laundered through several intermediary addresses and other virtual currency exchanges.  In many instances, the actor converted the cryptocurrency into BTC, Tether, or other forms of cryptocurrency – ```a process known as “chain hopping”``` – in order to obfuscate the transaction path.  As detailed in the pleadings, law enforcement was nonetheless able to trace the funds, despite the sophisticated laundering techniques used.

---
These actors stole millions of dollars’ worth of cryptocurrency and ultimately laundered the funds through ```Chinese over-the-counter (OTC) cryptocurrency traders.```

---
The advantage of these methods is that they ```avoid dependency on specific command lines or process names, which the attackers are always changing or obfuscating.```

---
use a ```threat graph``` to find rogue processes

---
The advantage of threat hunters with this approach is that hackers can change their techniques and obfuscate their attacks, ```but they can’t easily hide their graph patterns.```

---
```"'Bulletproof exchanger'``` is a general term used internally to refer to a high-risk exchanging service that serves as a cash-out point for criminal activity, such as ransomware," the Binance security team told ZDNet in an email last week.

---
Generic detection of VM and sandbox environments can be performed. For example, ```if physical memory is less than 2GB or if there is only a single processor core, it is likely you’re running in a VM.```

---
```the WinRM service listens on TCP port 5985 (HTTP)``` and is encrypted by default. Certificates may also be configured enabling HTTPS support over TCP port 5986.

---
DCOM has been the default protocol used by WMI since its inception. ```DCOM establishes an initial connection over TCP port 135.```

---
The greatest advantage to using the CIM cmdlets is that they work over both ```WinRM and DCOM protocols```.

---
```WebRTC is``` an open source video conferencing solution used by a variety of software including browsers, messaging clients and streaming services.

---
 Emotet started life as a banking trojan before evolving into a botnet that is leased out to deliver other malware, which in this case is the Trickbot trojan.

Trickbot is a powerful form of malware that provides attackers with a full backdoor into compromised systems, including the ability to move around networks, issue commands and steal additional data.

After this the Ryuk ransomware is downloaded onto the network by the hackers because cyber criminals view it as the quickest and easiest way to make money from a compromised network. 

---
Fortunately, ```this bug was also discovered during a Cisco investigation with a customer```. The company is not aware of public exploits for the vulnerability.  

---
While ```security in the cloud is still relatively in its infancy```, the same can be said for the attacker behaviors – much of what we observed here and in the past were elementary attack patterns.

---
The new malware, dubbed “Doki”, hasn’t been detected by any of the 60 malware detection engines in VirusTotal since it was ```first analyzed on January 14, 2020.```

---
FBI officials said the backdoor malware was spotted in the VAT software of two Chinese tech companies -- namely ```Baiwang and Aisino.```

Value Added Tax

---
Google Cloud already encrypts data at rest and in transit. Confidential ```VMs, currently in beta, offer memory encryption to keep workloads isolated.```

Encryption keys are per hardware and are non-transferable. (AMD processors)

---
```Forescout``` (device visibility and control)

---
CWE = ```Common Weakness Enumeration```

-->mitre contains a list of these

---
```The malformed packet is almost completely RFC compliant, and so it will likely be difficult for security products such as firewalls to detect this vulnerability.```

---
```Attackers can exploit CVE-2020-1048 with a single PowerShell command:```

Add-PrinterPort -Name c:\windows\system32\ualapi.dll

On an unpatched system, this will install a persistent backdoor, that won't go away *even after you patch*.

---
```VBA stomping``` refers to destroying the VBA source code in a Microsoft Office document, leaving only a compiled version of the macro code known as p-code in the document file. Maldoc detection based only on the VBA source code fails in this scenario

---
owned by Dutch VPS provider ```Host Sailor, Hong Kong-based New World Telecoms, and Malaysia-based Shinjiru Technology``` 

---
During one intrusion observed by CTU researchers, the group used the native vssadmin tool on a domain controller to create a volume shadow copy:

vssadmin create shadow /for=c:


```The threat actors retrieved the NTDS.dit file from the volume shadow copy. NTDS.dit contains Active Directory data, including password hashes for all users on a domain.```

---
```Wmiexec to move laterally```. During one intrusion, the threat actors extensively used this tool to execute WMI commands on remote hosts in the environment 


---
```hollowed svchost.exe process```

https://attack.mitre.org/techniques/T1093/

---
The tool uses the ```Windows Management Instrumentation (WMI)``` event consumer for persistence by installing a script to the system's WMI registry.

---
But this episode reveals how, with some planning and skill, ```disinformation attacks can target vulnerable websites and then use Facebook to amplify forged content```. Once it's in public groups, it's hard to stop it

---
You should continue to enforce proven preventive solutions—```credential hygiene, minimal privileges, and host firewalls```

---
but can also dump cached credentials and passwords for service accounts and scheduled tasks that are stored in the ```LSA Secrets section of the registry.``` --> I guess Mimikatz can do this

Otherwise, check the Windows Event Log for post-compromise logons—those that occur after or during the earliest suspected breach activity—with ```event ID 4624 and logon type 2 or 10. For any other timeframe, check for logon type 4 or 5.```


---
Malicious PowerShell, Cobalt Strike, and other penetration-testing tools that can allow ```attacks to blend in as benign red team activities```


---
Apr 29
Per a Coveware report released today, ```RDP still remains the top entry point for the vast majority of ransomware attack```s they've investigated

---
In these recent campaigns, an initial downloader connects to a specific paste, reads the stream, and then uses a ```compiler to do a runtime compilation and run the malware code in memory```.

---
```Auditd is the userspace component of the Linux® Auditing System```. Auditd can provide users with insight into process creation logs. The information is valuable for identifying anomalous behavior, such as in the case of malicious web shells. Auditd is available in default repositories for many Linux® distributions and must be installed and configured to log relevant web server process data. Ideally, auditd and other Linux® logging should be mirrored to a central Security Information and Event Management (SIEM) server where it can be aggregated and queried.

---
```Microsoft® Sysmon``` is a logging tool that enhances logging performed on Windows® systems. Among other things, Sysmon logs information about how each process is created. The information is valuable for identifying anomalous behavior, such as in the case of malicious web shells. Sysmon can be obtained from Microsoft® at https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon and must be installed on a system in order to begin logging. Ideally, Sysmon and other Windows® logging should be mirrored to a central Security Information and Event Management (SIEM) server where it can be aggregated and queried

---
Packet capture (PCAP) and network flow data can help to determine if the web ```shell was being used to pivot within the network```, and to where.

---
```Host Intrusion Prevention System (HIPS)``` rules for use with McAfee® 8 ```Host Based Security System (HBSS)```

---
-site:pinterest.*

Save us from pinterest

---
```Web shells``` are one of today's most popular forms of malware. The term "web shell" refers to a malicious program or script that's installed on a hacked server.


---
Are they the only government that hacks for finical gains?

Apr 15
Yes.

Although some members of Iranian and Chinese APTs are also involved in financially motivated hacks, those hacks are for personal gain, rather than for their respective central governments.
·
Apr 15
```Basically, stealing money is a day job for the Norks, but only a personal project for the other foreign APTs.```

---
The botnets also implement ```hashbusting```, which ensures the malware's file hash is different on each infected system. 2/4

---
Cloudflare marks themselves as green and safe on their site. But yet I can still access their website on ```cloudflare from an RPKI invalid IP address block```. Or should I say:


---
The underlying problem is that consumer-grade devices are not that secure and don’t stand up to the sort of adversaries that have the ```capability of buying zero-days and going after devices en masse```

---
"Detection at this level allows organizations to respond to advanced threats quickly and successfully, interrupting the ```attack chain``` before it's able to do more damage," 

---
To guarantee even stronger isolation (e.g., with protection against a compromised operating system), cloud providers can also run ```software inside secure (SGX) enclaves.``` 

---
#MDS: Microarchitectural Data Sampling


```RIDL (Rogue In-Flight Data Load)```
whether using shared cloud computing resources, or using JavaScript on a malicious website or advertisement - can steal data from other programs running on the same machine, across any security boundary: other applications, the operating system kernel, other VMs (e.g., in the cloud), or even secure (SGX) enclaves. 

```Fallout``` demonstrates that attackers can leak data from Store Buffers, which are used every time a CPU pipeline needs to store any data. Making things worse, an unprivileged attacker can then later pick which data they leak from the CPU's Store Buffer. 

The reason our attacks are impervious to all the ```existing defenses against speculative execution attacks``` is that they can leak ```in-flight data```. Unlike other recent attacks such as Spectre, Meltdown, and Foreshadow which are based on vulnerabilities leaking data from the CPU caches, RIDL and Fallout collect data from ```internal CPU buffers (Line Fill Buffers, Load Ports, Store Buffers)```.

---
Docker servers targeted by new Kinsing malware campaign

- Attacks started last year
- Hacker group targets Docker hosts with API ports left exposed on the internet
- On exposed systems, hackers spin up an Ubuntu system and install the ```Kinsing cryptominer```

---
This is an ad for the Makop ransomware-as-a-service (RaaS).

A few people have asked or reached out for help with this recently. Appears to be in the wild now... and going through a distribution surge? cc: @demonslay335

This is a ```crypto locker```

---
I am not jumping on the bandwagon but as an IT security professional you ```(a) should launch investigations in your infra to check for breaches (b) make public those results to get back trust (c) IMMEDIATELY ROLL OUT stronger authentication, (2FA, Risk detection)```

---
demonstrated that the firmware of many USB dongles can be reprogrammed so that, when inserted in a computer, it reports that it's actually a keyboard and starts sending commands that could be used to deploy malware.

https://www.csoonline.com/article/3534693/cybercriminal-group-mails-malicious-usb-dongles-to-targeted-companies.html

---
Using the same PassiveTotal, Denley found that the same servers were also ```hosting more than 450 other websites```, all with shady-looking domains, containing terms like Gmail, coronavirus, and the brands of other cryptocurrency-related entities.

---
For example, using ```ADS allows stream data to remain invisible in File Explorer```, and in this case Astaroth reads and decrypts several plugins from ADS streams in desktop.ini that allow Astaroth to steal email and browser passwords as well as find and disable installed security software. 

```The plugins are the NirSoft MailPassView tool for recovering email client passwords and the NirSoft WebBrowserPassView tool for recovering passwords from browsers. ```

---
Furthermore, the botnet should be managed via a web-based administration panel hosted on a ```*command and control (C&C) server, placed behind a network of VPN and proxy servers, in order to hide its real location.```*

---
The time from initial compromise to the actual ransomware attack -- known as a "```dwell time```" -- is, on average, three days, according to FireEye.

---
"I think this is why they employ as it returns back the legit Cloudflare proxy IP which acts as a reverse proxy passing the traffic to the C2. It makes blocking the IP traffic impossible given it is ```*Cloudflare (unless the whole Cloudflare worker space is banned) infrastructure while hiding the actual C2```*."

---
As ```WSL2 uses a true Linux kernel```, Linux apps will now have full access to their normal system calls, which will bring increased compatibility with existing Linux apps and greater performance.

---
According to one of Bloomberg's sources, this tweet was in response to a ```disinformation campaign``` being conducted by the attackers in conjunction with the attempt to take down the HHS.gov site.

---
Brave's decision comes as online advertisers and ```analytics firms are moving away from tracking users via cookies to using fingerprints.```

---
Monitoring for various processes such as PowerShell.exe, net.exe, net1.exe, cmd.exe, ping.exe, nslookup,exe, certutil.exe, etc., ```where the parent process is w3wp.exe can be an effective mechanism to detect exploitation.```

---
```Canary Token```

---
```"We know that 60% of users reuse passwords. It's super common,"``` said Lee Walker, Identity and Security Architect at Microsoft. 

---
```password spraying```, a technique during which an attacker picks a common and easy-to-guess password, and goes through a long list of usernames until they get a hit and can access an account using said password.

---
Microsoft has been monitoring another malware group it calls ```Parinacota``` (Microsoft is using volcanoes to name digital crime actors) for 18 months. They've historically hacked machines to install cryptocurrency miners and send spam, but recently started deploying ```Wadhrama ransomware on corporate networks in "smash and grab" attacks``` with ransom demands made within an hour of infiltration. If given the opportunity, the group also conducts reconnaissance and moves within the network, too. 

---
"```Ransomware groups at this point have it down to a science,```" Goldberg added. "Find a simple reliable exploit like this, attack opportunistic victims, find those with money to pay, and profit."

---
Edwards allegedly ```hired software developers in India``` for the purpose of altering the stolen software and preparing a modified version.

---
Originally published for Windows, the “Heaven’s Gate” technique allowed malicious software to evade endpoint security products by invoking 64-bit code in 32-bit processes, effectively bypassing user-mode hooks. This technique has since been mitigated in Windows 10+ through ```Control Flow Guard (CFG).```

---
SUSE, she believes, has found a functioning business model to ```marry open-source software and profit```: it is ```support and services``` that the company sells, to the enterprises using the open-source technologies developed by SUSE developers. 

---
The results were telling, and indicated that ```modern technology is often a stumbling block```, and confidence is only marginal at best. 

---
raising money through cyber-thefts, such as the use of ransomware and ```hacks of banks, ATM networks, gambling sites, online casinos, and cryptocurrency exchanges.```

---
We looked very seriously at ARM-based CPUs and continue to keep our software up to date for the ARM architecture so that we can use ```ARM-based CPUs when the requests per watt is interesting to us.```

---
A great step indeed for websites that use static IP for a single resource. Websites that uses ```Server Name Indication TLS (SNI)``` extension for shared hosting force clients to send the hostname in plain-text during TLS handshake which could be sniffed. (Reliance Jio in India is already doing it https://cis-india.org/internet-governance/blog/reliance-jio-...).

The Same thing OCSP Stapling (Online Certificate Status Protocol) extension which also sends the hostname.

Cloudflare crafted a solution for this by storing the public key of the target website along with the DNS record. So during DoH when the user asks for IP of a given host, it can also get the public key of the host. User then establishes the TCP, ```encrypt the SNI (ESNI)``` extension & OCSP with the public key and starts the TLS handshake.

Though ESNI doesn't seem to provide perfect forward secrecy it is a leap forward. 

---
To reduce costs for 5G operators, ```5G allows for smaller transmitters that consume lower power```, but that cover much smaller service areas than typical 4G towers. 

---
The rollout of 5G may mean that enterprises ```ultimately mandate that employees use 5G over public Wi-Fi. ```

---
the group used ```reseller hosting services```, which allowed them to disguise their traffic

---
```Instead of registering domains``` to spread malware, the Equifax hackers directly connected malicious code, known as a web shell, to a server in a way that enabled them to remotely collect data from the Equifax network, according to the indictment.

---
Dashlane stated that they "```fell afoul of an automated bot```, but we’re back up after we were able to speak to a human at Google."

---
The majority of organizations may also be struggling with managing which keys and certificates -- including those that have been self-signed -- are in play, ```with 74 percent of survey respondents suggesting that their businesses do not know which are in use, where to find them, or when they expire. ```

---
According to multiple experts, both BEC and ransomware attacks are expected to continue to rise in 2020, as ```there's little to deter cyber-crime groups from launching new operations.```

---
"Companies need to understand that ```cyberattacks are no longer technically sophisticated. ```

---
```OpenSSH 8.2 adds support for authentication via FIDO/U2F protocols, most commonly used with hardware security keys.```


---
```business email compromise (BEC)```

---
Last year, Microsoft said that the company's customers who enabled MFA for their respective ```Microsoft accounts blocked 99.9% of account hacking attempts```, showing just how difficult is to bypass a MFA solution today.

```In a table it published in October, Microsoft ranked FIDO-based hardware security keys as the most secure MFA solution and the hardest to crack.```

---
Almost a quarter of interviewed CISOs said boards didn't accept or understand that "```breaches are inevitable```" and said they'd hold them personally accountable for any security incidents.

---
"Even when they are not at work many CISOs feel unable to switch off," Nominet said. "```As a result, CISOs reported missing family birthdays, holiday, weddings and even funerals```.

---
Gigabyte's fault resides in its ```unprofessional manner in which it dealt with the vulnerability report``` for the affected driver. Instead of acknowledging the issue and releasing a patch, Gigabyte claimed its products were not affected.

---
```Contractors are required to report any such event within 72 hours of discovery``` and submit the malware to the DOD Cyber Crime Center (DC3), according to federal acquisition regulations.

---
The company's ```Pegasus suite```, for example, is mobile malware able to intercept communication from Android and iOS devices, extract data, havest live video and audio feeds as well as compromise messaging systems including WhatsApp, Twitter, and Skype.

---
to access the ```printed circuit board (PCB)```

---
```International Traffic in Arms Regulations (ITAR)```, meaning Sun and Raytheon were supposed to get approval from the US government in order to transfer the files abroad.

---
#Redteam operators: Which defensive settings have you encountered that made it *super* painful for you to operate in a Windows AD environment?

```No client-to-client comm. ```
😈

This is why ```I love the Windows Firewall```. Supereasy to implement this and thus making lateral movement a lot harder. And again I recommend this pearl by @jepayneMSFT

https://sec.ch9.ms/sessions/ignite/New-Zealand-2016/M377.mp4


---
In a typical online retailer intrusion, ```the attackers will use vulnerabilities in content management systems, shopping cart software, or third-party hosted scripts``` to upload malicious code that snarfs customer payment details directly from the site before it can be encrypted and sent to card processors.

---
```“card not present” fraud```

---
increasingly are ```shifting their attention to compromising e-commerce merchants```, a trend seen in virtually every country that has already made the switch to chip-based cards.

---
breaches at ```supermarket``` chain Hy-Vee, ```restaurant chains``` Sonic, Buca di Beppo, Krystal, Moe’s, McAlister’s Deli, and Schlotzsky’s, ```retailers``` like Bebe Stores, and ```hospitality brands``` such as Hilton Hotels.

---
Backdoors into facial recognition platforms, specifically, are a real worry, as their ```compromise could set off a chain reaction in which AI learning could be corrupted. ```

---
```"FortiSIEM has a hardcoded SSH public key for user 'tunneluser' which is the same between all installs,"``` said Andrew Klaus, the security researcher who identified this issue.

---
But they also said that threats to the ```"information ecosphere" -- like the spread of misinformation and fake news -- could also create dangerous global instability.```

---
```The Windows 7 era coincided with the high point of the PC era```, and the end of Windows 7 marks the end of the PC era, too.

---
She suggests the need for greater ```organizational awareness on how cybersecurity leadership teams are structured.``` By empowering specialists and giving them more authority and accountability, they will be able to deliver their expertise in a way the board is expecting.

---
In response, Intel today pushed out an ```update to its chips' firmware``` that ```by default locks the voltage settings of its processors```, blocking the undervolting attack

--> Plundervolt

---
Throughout Glowing Symphony, Cyber Command frequently butted heads with the intelligence community given that Cyber Command’s task — ```disrupt or destroy ISIS infrastructure``` — ```ran contrary with the intelligence community’s mission of gathering information```, according to former Secretary of Defense Ash Carter.

---
The hackers behind the phishing campaign took great effort to mask their malicious intent from the victims; they used ```Sender Policy Framework (SPF) and Domain Keys Identified Mail (DKIM)```, according to Area 1. SPF and DKIM are email ```security tools that are used to validate an email message’s sender```.

---
That group has been linked to ```Russia’s intelligence directorate```, which is more commonly known as the ```GRU```

---
A New York Times investigation revealed this week that a host of ```dating apps```, including Grindr, have ```shared personal user information``` including location data with numerous marketing and advertising companies in ways that experts said ```may violate privacy laws```, according to a new report by the Norwegian Consumer Council (NCC).

---
As it stands, the ```face recognition use is entirely unregulated in most states``` and legal cases have already emerged accusing authorities of offering up unreliable results as evidence in court. 

---
Indeed, it was the NSA itself that discovered the vulnerability and reported it to Microsoft. This is, Neuberger confirmed, the ```first time that the NSA had publicly disclosed a vulnerability``` to a software vendor. 

CVE 2020-0601

---
```Incident Response team``` has been working closely with our ```offensive``` and ```research teams``` 

---
most widespread in ```Russia```, where the largest share of infected users (28.46%) was recorded in October – November 2019," Kaspersky Lab researcher Igor Golovin said. "Second place went to ```Brazil``` (18.70%) and third to ```India``` (14.23%)."

---
For smaller companies, the stats are clear. Commercial insurance carriers reported in 2019 that  ```cyber attacks``` cost companies of all sizes an average of ```$200,000 per incident``` in direct costs alone.

---
```Some Common Router CVEs```

In terms of exploited vulnerabilities, LiquorBot exploits some critical CVEs (CVE-2015-2051, CVE-2016-1555, CVE-2016-6277) as well as a series of command injection and remote command execution vulnerabilities found in various router models (CVE-2018-17173, CVE-2017-6884, CVE-2018-10562, CVE-2017-6077, CVE-2017-6334, CVE-2016-5679, CVE-2018-9285, CVE-2013-3568, CVE-2019-12780).


---
How botnets get around:

```Propagation through SSH brute-forcing and exploitation of unpatched vulnerabilities in select router models```

---
The key to unlocking and detonating the malware is the ```biometric recognition``` of a predefined target. This means that ```DeepLocker malware``` can be widely distributed to millions of users, but it will only ever activate against the precise target or targets.

```AI Locksmithing```

---
2020 will be the year where businesses fully embrace ```Autonomous Response``` – or AI that fights against cyber-threats automatically.

---
A cyber weapon designed to shut down the power of a military compound could ```leak from the intended system```, and inadvertently plunge parts of the country into darkness – prompting its governments to respond in kind

---
In a nutshell, ```API hooking``` is the process of intercepting a function call in a program by redirecting it to another function. This is done by ```re-writing the in-memory code``` for the target function in order to be redirected to the other function, which later-on calls the original function. 

---
To create a payload that uses ```HTML smuggling```, use the –smuggle argument with the –template argument to select a template, e.g. –smuggle –template mcafee.

---
```Ransomware 2019:```

• Emergency patients had to be redirected to other hospitals.
• Medical records were inaccessible and, in some cases, permanently lost.
• Surgical procedures were canceled, tests were postponed and admissions halted.

---
Automation is essential to keep up with an attack vector that is growing exponentially. ```But you need the right balance with human intelligence```. 

---
If the expected reply is not received, it terminates. 
```For malware like this, firewall rules can be effective```


---
The implication is that it is available for hire as
part of the burgeoning ```malware-as-a-service black market```. 


---
Windows 0-day exploit CVE-2019-1458 used in Operation ```WizardOpium```
In November 2019, Kaspersky technologies successfully detected a Google
Chrome 0-day exploit that was used in Operation WizardOpium attacks. 

--This also exploits a Window's driver bug to gain admin on Windows 7 boxes.

---
This is why Patrick suggests ```Threat Intelligence``` is going to become increasingly more critical because enterprises are going to have to constantly be analyzing acceptable/unacceptable uses patterns, base lines and anomalies.

---
```Docker images are often composed of like 25 “layers”.```

---
"It's still an area where there's ```little risk of being caught or arrested``` – and it's still a lucrative business," said Monrad.

---
The goal was to test if the country's national internet infrastructure -- ```known inside Russia as RuNet``` -- could function without access to the global DNS system and the external internet.

Called the ```"internet sovereignty" law```, it grants the Russian government the power to ```disconnect the country from the rest of the internet``` at will and with little explanation, on the grounds of "national security."

---
If, after trying to use the bridge interface, you find your network link becomes dead and refuses to work again, ```it might be that the router/switch upstream is blocking "unauthorized switches"``` in the network (for example, by detecting ```BPDU packets```)


---
```North Korea has hosted at least two cryptocurrency conferences so far```, one in late 2018, and another in the spring of 2019 -- the one which Griffith attended.

---
IM-RAT reported as having ```14,5k buyers``` in 124 countries
--> That's a very low number in respect to the number of countries

---
In some cases, ```organizations did not even realize their operations still relied on Windows XP```, until an affected machine seized somewhere, causing disruptions.

---
it wasn’t immediately clear how ```smaller and mid-sized organizations``` could combat adversaries and embrace the fight.

---
Companies hit by the Ryuk ransomware all too often are ```compromised for months or even years``` before the intruders get around to mapping out the target’s internal networks and compromising key resources and data backup systems. 

---
A ransomware outbreak has ```besieged a Wisconsin based IT company that provides cloud data hosting, security and access management to more than 100 nursing homes``` across the United States.

---
It may be difficult to tell from the angle of the photograph above, but the horizontal bar across the top of the machine (just above the “This Sale $” indicator) contains a hidden pinhole camera angled so as to record debit card users entering their PIN.

---
Yes, you read that right: houston.gov, losangeles.gov, newyorkcity.gov, and philadelphia.gov are all still available. As is the .gov for San Jose, Calif., the economic, cultural and political center of Silicon Valley. ```No doubt a great number of smaller cities also haven’t figured out they’re eligible to secure their own .gov domains```.

---
```Wire fraud``` (obtaining something of value via the Internet/telephone/fax through false pretenses)

---
Microsoft declares = ```Privacy is a human right```

---
Cyber Command to be more offensive in cyberspace, key officials have suggested there is a groundswell of support for ```multi-nation countermeasures in the digital age```

```collective countermeasures```

---
```Aleksei Burkov``` appeared in the Eastern District Court of Virginia to refute charges including computer intrusion, identity theft and other fraud-related accusations.

---
HNAP ```(Home Network Administration Protocol)```
```Simple Object Access Protocol``` (SOAP) 
```Representational State Transfer``` (REST) 

---
Since Windows stores some credentials (either Kerberos tickets or NTLM hashes) in memory for logged on users, an attacker can sometimes gain more valuable credentials by gaining local Admin on a box, ```dumping the Kerberos tickets or NTLM hashes from memory, and then impersonating that user to move to another machine that they have access to.``` 

---
```Web Stresser``` or ```Booter``` service= online DOS services.

---
When Israel declined, a Russian court sentenced ```Issachar``` to more than ```seven years``` in prison for allegedly holding a small amount of marijuana while passing through a Moscow airport.

---
In the USB Charger Scam, often called ```“juice jacking,”``` criminals load malware onto charging stations or cables they leave plugged in at the stations so they may infect the phones and other electronic devices of unsuspecting users.

---
The pair said they managed to create a similar tool even though they ```didn’t possess particularly strong technical skills```. That, of course, was their point: Virtually ```anyone``` could now create convincing AI-powered content generation tools.

---
```Google Text To Speech```

---
Four of the defendants were charged with defrauding the U.S. government by falsely asserting that ```Aventura was owned by Frances Cabasso in order to win government contracts reserved for female-owned firms```.


---
```Data localization``` = keeping a county's citizen's data local to that country.
Referred to as "Splinternet"

---
With one interaction, you’ll say “Alexa, play some music” and the assistant will ```‘randomly’ select a playlist that touches the depths of your soul```, as if it knew better than you did what you needed to hear. 

---
The malware was capable of ```stealing call logs and SMS conversations``` from a target’s phone.

---
Over 100 public-sector ```ransomware attacks``` have been reported in 2019 alone, double the amount in 2018.

---
international payment protocols such as ```WeChat, Alipay and M-Pesa```.

---
Put concisely, this project will not empower anyone. It is a pivot from a company whose advertising business is so embroiled in scandal and corruption that it has ```no choice but to try to diversify into payments and credit scoring to survive```.

---
Uighur community, a ```Muslim population``` under mass surveillance by the Chinese

---
DOE defines a “cyber event” as a disruption to electrical or communication systems caused by unauthorized access to hardware, software or communications networks. ```Utilities have to promptly report any such incidents to DOE```.

---
This case only is the latest example of ```Russian officials``` trying to prevent an accused hacker from being sent to trial in the U.S.

---
One might theorize that attackers know they have essentially one shot at using it at scale, and it ```becomes a game of chicken as to who will do it first```.

---
all the honeypots and changed them from ```kernel logging to full memory logging```. (Windows)

---
```Azure Sentinel with Microsoft Sysmon```

---
These kinds of missions, known as ```“Hunt Forward”``` operations, are relatively new for Cyber Command. Last year, along with Montenegro, 

---
FireEye has observed this methodology executed numerous times by both ethical hackers and unauthorized threat actors in addition to ```Certutil’s``` benign use as a part of legitimate business applications and operations.

---
```Antiboycott Laws:```

During the mid-1970's the United States adopted two laws that seek to counteract the participation of U.S. citizens in other nation's economic boycotts or embargoes. These "antiboycott" laws are the 1977 amendments to the Export Administration Act (EAA) and the Ribicoff Amendment to the 1976 Tax Reform Act (TRA). While these laws share a common purpose, there are distinctions in their administration.

---
```github``` which is basically carrying a big chunk of commercial IP in private repos

---
Another indicator that you should be aware of is when using ```staged DNS payloads```. As .NET <= v4 does not contain a native DNS library for performing ```TXT record lookups```,

---
we ```invest heavily in reconnaissance```. The reason for this is that understanding the target’s environment will pay dividends, particularly when it comes to payload creation.

---
mostly those involving ```malware inside point-of-sale retail checkout systems```.

---
According to Gemini, there were ```142 resellers``` and more than ```50,000 buyers``` of the card data sold through BriansClub. These buyers purchased at least 9 million of the 27.2 million cards available

---
```hard truths```. Most notably, that the world’s largest financial institutions tend to have a much better idea of which merchants and bank cards have been breached than do the thousands of smaller banks and credit unions across the United States. Also, a great deal of cybercrime seems to be perpetrated by a relatively small number of people.

---
Fancy Bear is the same group that breached the ```Democratic National Committee``` in 2016.

---
```Chinese law requires``` companies to comply with requests from Chinese intelligence departments, which Pai and intelligence officials say raises concerns about Huawei or ZTE conducting espionage on behalf of the Chinese government.

---
Federal Communications Commission Chairman Ajit Pai revealed a proposal Monday that would bar U.S. communications companies from using federal subsidies to buy Huawei and ZTE equipment and services.

---
Mobile malware is increasingly used by hacking group because ```mobile security solutions are few and far between```, so avoiding detection is much easier than efforts that target users on desktop or laptop computers, according to Cylance.

---
```Outlook Forms```
```Empire Power Shell```
```Web Beacon``` (email, turn off your images)


---
```Password Sprays```
spray.sh

---
The Threat to SoHo IoT Devices is Growing Rapidly A network of 50 honeypots deployed around the world has been catching and monitoring attacks against IoT devices. Such detected attacks have increased almost nine-fold between H1 2018 and H1 2019, from 12 million to 105 million. 

---
Raccoon Malware-as-a-Service 

---
# System Mods and rootkit finders
Tripwire or rkhunter

---
Joker's Stash

---
FakeApp

---
Unaware of a secret international arrest warrant

---
“There are a lot of highly educated, technical people and not a lot of jobs,” Chan said. “To try to make a living, many go into criminal hacking.”

---
“Such data can then be encoded onto any plastic magstripe card, allowing criminals to make in-person purchases.”

