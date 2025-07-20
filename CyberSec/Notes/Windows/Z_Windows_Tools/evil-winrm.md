__tags: windows winrm linux

### Install is easy:

```
gem install evil-winrm
```

### Login with password:

```
evil-winrm -i 10.10.10.172 -u mhope -p 4n0therD4y@n0th3r$
```

### Login and upload powersploit scripts
```bash
evil-winrm -i 10.10.11.61 -u mark.adams -p 'PASSWORD' -s /usr/share/windows-resources/powersploit
```