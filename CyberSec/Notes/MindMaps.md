##
> KVM and Xen have a smaller attack surface and are known to have a better isolation model, but I'm sure there are still plenty of exploits given enough resources.

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

##
The domain must not contain certain strings; ```the check for these strings is implemented via hashes```, so at this time the domain names that are block-listed are unknown

##
These are websites that use top-level domains (TLDs) managed by Emercoin, a blockchain company. ```Records for these domains are stored inside a blockchain and cannot be transferred to anyone else without the domain owner's cryptographic signature.```

"Notably, JokerStash was one of the original proponents of moving dark web services to Blockchain technology."

##
```This is why PAAS rocks```

Your apps run inside smart containers in a fully managed runtime environment, ```we handle everything critical for production — configuration, orchestration, load balancing, failovers, logging, security, and more.```

https://www.heroku.com/

##
Perhaps the most effective means of preventing ransomware outbreaks is to ```implement application controls, which ensure only approved binaries are allowed to execute in the environment.```


##
 you can create a **“crypto canary”** on your file servers to notify you when Ryuk or other families encrypt file shares. 

--> Windows File Shares Only

##
We immediately notified the customer and our mutual incident response partner, Kroll. **Acting swiftly, Kroll began executing response processes including isolating endpoints and banning malicious binaries, as our CIRT continued to publish detections for the escalating lateral movement and credential theft.**

##
Bypass all possible **Windows Security Defenses**:

- SMEP
- Kernel DEP
- KASLR
- Integrity Level (escape from Low)
- Null Dereference Protection
- UAC

##
As the CEO of the OLED Association, he also argues that OLED displays provide the same responsiveness as CRT monitors because they also involve electron-to-photon conversion, only with organic chemicals (the "O" in OLED is for organic) receiving the voltage instead of phosphor dots.

**"There's really no difference between OLEDs and CRTs," Young said.**


##
But judging from the proliferation of help-wanted ads for offensive pentesters in the cybercrime underground, **today’s attackers have exactly zero trouble gaining that initial intrusion**

That’s because it usually **takes time and a good deal of effort for intruders to get from a single infected PC to seizing control over enough resources within the victim organization where it makes sense to launch the ransomware.**

At that point, control over the victim machine may be transferred or sold multiple times between different cybercriminals who specialize in exploiting such access. **These folks are very often contractors who work with established ransomware groups, and who are paid a set percentage of any eventual ransom payments made by a victim company.**

“But because of the rapidly growing market for compromised accesses and the fact that these could be sold to anyone, **organizations need to focus more on efforts to understand, detect and quickly respond to network compromises,”**

which variously claims to be based in the **offshore company havens of Belize and the Seychelles**

##
# Splunk Education:

**If you are interested in other workshops - you can find future dates & topics here -** 
https://www.carahsoft.com/doyouknowsplunk#virtual-workshops

**Splunk .conf**

https://conf.splunk.com

##
The company said it discovered these attacks after **two computers were flagged by the company's Firmware Scanner** module as suspicious.

##
Microsoft has released on Friday a new tool that will allow system **administrators to update the Defender security package inside Windows installation images** (WIM or VHD supported). 

https://www.zdnet.com/article/microsoft-releases-tool-to-update-defender-inside-windows-install-images/

##
Another possibly use is to **create a baseline of tools writing to the clipboard** and create some detection logic on anomalies.

Sysmon event 24

##
Performing **frequency analysis** on the IIS logs could indicate the location of a malicious virtual directory.

##
commonly used staging directories **(recycle bin, temp folders, etc.)**

##
The tooling STRONTIUM is using routes its authentication attempts through a pool of approximately 1,100 IPs, the **majority associated with the Tor anonymizing service.**

##
Analysts from **Microsoft Threat Intelligence Center (MSTIC)** and **Microsoft Identity Security** have been tracking this new activity since April 2020.

##
The ComputeNetlogonCredential function, **however, defines that this IV is fixed and should always consist of 16 zero bytes**. This violates the requirements for using AES-CFB8 securely: its security properties only hold when IVs are random

##
**Netlogon** is a Windows Server process that authenticates users and other services within a domain. Since it is a service and not an application, Netlogon continuously runs in the background, unless it is stopped manually or by a runtime error. Netlogon can be stopped or restarted from the command-line terminal.

**If Netlogon is stopped**, many Windows Server functions are affected as users can no longer log in to their accounts and the domain controller cannot automatically register Domain Name System records, which contain user login information.

##
In my experience - best phrasing is:
1) based on evidence it is reasonable to conclude that XYZ data was stolen by attacker
2) in my professional opinion - XYZ data was stolen by attacker 

**Both aren’t stating a fact - but a logical or/or informed conclusion from the evidence**

##
Exactly because it takes moxie to hack into something and straight fucking own em... **Easier $$ being the cyber arms dealer** ... one stop shop cop n roll

##
Buying identities was so much better for them than stolen payment card data, because card data could be used once or twice before it was no good to them anymore. **But identities could be used over and over again for years.**”

##
**TLO’s service is accessible to law enforcement agencies and to a limited number of vetted professionals who can demonstrate they have a lawful reason to access such information.** In 2014, TLO was acquired by Trans Union, one of the other three big U.S. consumer credit reporting bureaus.

Legal Data brokers to help law enforcement 

##
Virtual  currency  exchanges  doing  business  in  the  United  States  are regulated  under the **Bank Secrecy Act**, codified  at 31 U.S.C. § 5311 et seq.,  and  must  collect   identifying   information   of  their  customers  and  verify  their  clients’  identities.

##
Over the subsequent months, the funds were laundered through several intermediary addresses and other virtual currency exchanges.  In many instances, the actor converted the cryptocurrency into BTC, Tether, or other forms of cryptocurrency – **a process known as “chain hopping”** – in order to obfuscate the transaction path.  As detailed in the pleadings, law enforcement was nonetheless able to trace the funds, despite the sophisticated laundering techniques used.

##
These actors stole millions of dollars’ worth of cryptocurrency and ultimately laundered the funds through **Chinese over-the-counter (OTC) cryptocurrency traders.**

##
The advantage of these methods is that they **avoid dependency on specific command lines or process names, which the attackers are always changing or obfuscating.**

##
use a **threat graph** to find rogue processes

##
The advantage of threat hunters with this approach is that hackers can change their techniques and obfuscate their attacks, **but they can’t easily hide their graph patterns.**

##
**"'Bulletproof exchanger'** is a general term used internally to refer to a high-risk exchanging service that serves as a cash-out point for criminal activity, such as ransomware," the Binance security team told ZDNet in an email last week.

##
Generic detection of VM and sandbox environments can be performed. For example, **if physical memory is less than 2GB or if there is only a single processor core, it is likely you’re running in a VM.**

##
**the WinRM service listens on TCP port 5985 (HTTP)** and is encrypted by default. Certificates may also be configured enabling HTTPS support over TCP port 5986.

##
DCOM has been the default protocol used by WMI since its inception. **DCOM establishes an initial connection over TCP port 135.**

##
The greatest advantage to using the CIM cmdlets is that they work over both **WinRM and DCOM protocols**.

##
**WebRTC is** an open source video conferencing solution used by a variety of software including browsers, messaging clients and streaming services.

##
 Emotet started life as a banking trojan before evolving into a botnet that is leased out to deliver other malware, which in this case is the Trickbot trojan.

Trickbot is a powerful form of malware that provides attackers with a full backdoor into compromised systems, including the ability to move around networks, issue commands and steal additional data.

After this the Ryuk ransomware is downloaded onto the network by the hackers because cyber criminals view it as the quickest and easiest way to make money from a compromised network. 

##
Fortunately, **this bug was also discovered during a Cisco investigation with a customer**. The company is not aware of public exploits for the vulnerability.  

##
While **security in the cloud is still relatively in its infancy**, the same can be said for the attacker behaviors – much of what we observed here and in the past were elementary attack patterns.

##
The new malware, dubbed “Doki”, hasn’t been detected by any of the 60 malware detection engines in VirusTotal since it was **first analyzed on January 14, 2020.**

##
FBI officials said the backdoor malware was spotted in the VAT software of two Chinese tech companies -- namely **Baiwang and Aisino.**

Value Added Tax

##
Google Cloud already encrypts data at rest and in transit. Confidential **VMs, currently in beta, offer memory encryption to keep workloads isolated.**

Encryption keys are per hardware and are non-transferable. (AMD processors)

##
**Forescout** (device visibility and control)

##
CWE = **Common Weakness Enumeration**

-->mitre contains a list of these

##
**The malformed packet is almost completely RFC compliant, and so it will likely be difficult for security products such as firewalls to detect this vulnerability.**

##
**Attackers can exploit CVE-2020-1048 with a single PowerShell command:**

Add-PrinterPort -Name c:\windows\system32\ualapi.dll

On an unpatched system, this will install a persistent backdoor, that won't go away *even after you patch*.

##
**VBA stomping** refers to destroying the VBA source code in a Microsoft Office document, leaving only a compiled version of the macro code known as p-code in the document file. Maldoc detection based only on the VBA source code fails in this scenario

##
owned by Dutch VPS provider **Host Sailor, Hong Kong-based New World Telecoms, and Malaysia-based Shinjiru Technology** 

##
During one intrusion observed by CTU researchers, the group used the native vssadmin tool on a domain controller to create a volume shadow copy:

vssadmin create shadow /for=c:


**The threat actors retrieved the NTDS.dit file from the volume shadow copy. NTDS.dit contains Active Directory data, including password hashes for all users on a domain.**

##
**Wmiexec to move laterally**. During one intrusion, the threat actors extensively used this tool to execute WMI commands on remote hosts in the environment 

