# Basic One Liner Loop

```
while ($true) { sleep 5; wget http://209.240.132.16/ }
```

# Get AD groups based off of name
```
Get-ADGroup -Filter 'Name -like "Admin"'
```

# Get AD User based off of name:
```
Get-ADUser -Filter "Name -eq 'User Name'" -Properties *
```

# Get AD info on computers based on IP address:
-->Note: I could not get this working in scripts (conversion issue)

```
Get-ADComputer -Filter 'IPv4Address -eq "128.80.136.189"' -Properties *
```

# Get Signature of file to verify if it has been altered or not
```
Get-AuthenticodeSignature .\xcopy.exe | Format-List

```

# Display Pretty console Colors
```
Write-Host -ForegroundColor Green "This is a test!"
```

# Loop Through text file line by line:
```
ForEach ($line in Get-Content .\a.txt)
```

# Links:

```
# WMI Querying examples
https://www.andersrodland.com/use-powershell-discover-create-sccm-collection-queries/

#Check to see what SUG is applied to in SCCM:

https://arisaastamoinencom.blogspot.com/2017/06/kickin-those-sugs.html
```
