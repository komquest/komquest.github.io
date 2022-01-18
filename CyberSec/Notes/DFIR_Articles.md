# Article: How one hospital thwarted a Ryuk ransomware outbreak

https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/

---
This .exe is known as **Bazar**, which has different components known by the community as BazaLoader, BazarLoader, and BazarBackdoor.
---

You can identify this process hollowing, as we did, by looking for instances of the Windows Command prompt **(cmd.exe) executing without any command-line parameters and establishing a network connection**. 

---

Specifically, we observed the adversary using **nltest.exe to make domain trust determinations.**

---

looking for instances of it executing with a command line that includes **/dclist:<domain>, /domain_trusts or /all_trusts** has proven to be a very high-fidelity analytic for us to catch both Bazar

---

**We observed explorer.exe spawning svchost.exe—this isn’t normal**, so you should look for that in your environment.

---

 you can look for **svchost.exe processes where the parent is not services.exe**

---

Next, a Cobalt Strike binary was dropped on the endpoint as a .dll file and executed by rundll32.exe. With that, the intrusion began spreading laterally via Cobalt Strike. The operators used Windows Management Instrumentation (WMI) in their lateral movement attempt. WMI spawned cmd.exe, which subsequently spawned PowerShell with an encoded command line. 

---

Cobalt Strike uses the same structure for beacon payloads, consisting of an outer layer of Base64 encoding that contains within it another Base64 string, which is gzip-compressed.

---

We often detect **Sharphound/Bloodhound activity by hunting for many SMB connections over port 445 originating from a single process. **

---

Some things to consider before you’re facing a ransomware infection include the following:

- Make sure you are maintaining updated operating systems, software, and firmware.
- Maintain backups of important information and have a plan for recovering from backups. It’s important to periodically test your ability to recover from backups. This will help validate your recovery plan and also ensure that your backup data isn’t corrupt or otherwise unrecoverable.
- Periodically review domain administrator and accounts that have access to admin shares across your environment.
- Validate email security gateway policies and consider configuring them to quarantine and review documents or archive files before releasing them.
- Educate users so that they exercise caution when opening documents and following links, especially when they come from an unexpected sender.
- Have a disaster recovery and business continuity plan in place, and use this as an opportunity to review it.
- Consider keeping an incident response partner on retainer. These firms handle ransomware response on a daily basis and can provide invaluable assistance that could limit the impact of an outbreak and vastly expedite the recovery process.
- Also consider investing in third party assessment services like penetration testing to periodically evaluate the efficacy of your security controls and tools that afford you the ability merge extensive detection and response capabilities.

# Article: High Level Apporach to asking if a Windows system is Compromised
--> This was good training to help me ask the right questions and focus my
efforts in certain places when analyzing a system. 
--> I learned that finding compromise can be very difficult, but if you 
narrow down how and what your search in respect to a few high level "catagories"
of "where to start", you can be more efficent. It certainly is better than just
jumping into an assessment or potential incident.

# Course Link:

https://www.cybertriage.com/training/


**Users, Malware, and OS Configuration** --> Three things to focus on when trying to discover
if you have been breached


## What a good EDR client allows:
Ease of collecting Artifacts
Ease of remote collection
Id the releveant data
Pivoting
Scaling to many hosts

{Security Supp Guide}

##  Ways of analysis within DFIR:
**CLI** --> this is usually a case by case thing where you have one machine in which
you are extracting artifacts.
Continious montioring --> This is more of a SIEM environment
Full Image --> More on the Forensics side of the house, when you actually take an
image and extract information, note this can also be a memory image.


**Vender Agnostic** --> Try to be this when you are teaching

## IS THE SYSTEM COMPROMISED?? --> The highest level qusetion of them all

Cyber Triage Workflow (Determine if it is an incident or not)
1. Collect Artifacts
2. Score
3. Review
4. Deep Dive (Optional)
5. Report

## Make sure you investigate intrusions (CAT1,2,3)

## In Windows, The SAM registry hive contains the list of accounts, attackers
commonly extract this.

## Three things to ask assessing users for suspisious activity
1. Are there suspicious accounts?
2. Are there suspicious login events?
3. Did the users do anything suspicious?

---
# Windows Shellbags + RunMRU can be used to see what the user has been up to
# MRU --> Most Recently Used
---

Is the System Compromised???
--> What you can ask or catagorize to determine:
1. Are there Malicious hardware-related changes?
2. Is there malicious user activity?
3. Are there malicious programs?
4. Are there malicious OS configuration changes?

## Malware Hiding Examples:

1. Modify OS data structures to make it invisible from some APIs
2. Parasite (Hijack Another Process) or Hollowing (starting a process to hijack it,
however, the process launches from a boring location)


## Malware Detection How To (if you have a sample):
- Threat Intel: Is the program's hash on a "konwn bad" list (Hash, IOC, etc)
- Static Analysis: Does the program have byte-level signatures from previous malware?
- Dynamic Analysis: Does the program have malicious behavior?
- Reverse Engineering: Does the program have instructions that are malicious?

## System Internals "AutoRuns" --> if you want an easy program to show you everything
on Windows.

---
**One of the hardest parts of IR is finding Malware that is running**
---

---
One way to find malware is to check parents --> basically do any processes have
unexpected owner or parent processes?
Further looking into this you can do a "graph" baseline to see what parents should
be producing
---

**Advanced Memory Forensics can sometimes be the only way to detect advanced malware...**
- If running, the malware will be located inside of the memory image...
- The challenge is being able to parse the memory image and identify the malicious thread
or threads...
- It requires detailed knowledge about the OS and the apps that are running...
- This is not an easy task...

Some Remnants of Malware:
- File Artifacts: Are there any files or registry keys associated with past incidents?
- Network Cache Artifacts: Are there caches that reference IPs or domains associated
with past incidents (IOCs)?
- Memory: Is there unallocated memory that contains malware signatures?

```
Malware is hard, the authors employee an endless arsonel of tractics and techniques
int order to hide and make disoverey difficult. Thus in order to detect make sure
you have good automation in place (Things that are able to scan in many places at once
like EDR, SEIM, IDS, IPS, Scripts, etc), a board toolkit for malware analysis (Sandbox, staic/dynamic
, etc), and capability to scan memory images for advanced detections (forensic professionals?)
```

** Attackers can change the OS by:**
1. Making it easier to gain Access
2. Making it harder to detect activities
3. Making it harder for response to incidents
4. Making it easier for malware execution

** Why we need baselines: **
1. Looking for configuration changes can be hard
2. Many organizations are not consistent with endpoint configuration
3. It can be hard to know if a setting is different by accident or maliciously
