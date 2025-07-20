__tags: bloodhound windows AD bloodyAD

#### Use python bloodhound to scan with user and password
```bash
bloodhound-python -u ryan -p 'WqSZAF6CysDQbGb3' -d sequel.htb -ns 10.10.11.51 -c
all --zip
```

#### use bloodyad to find all writable stuffs for user
```bash
bloodyAD --host DC01.haze.htb -d haze.htb -u mark.adams -p 'Password' get writable --detail
```