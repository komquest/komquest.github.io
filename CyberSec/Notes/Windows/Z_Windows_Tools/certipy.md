__tags: windows AD certs ADCS

### Reference: https://app.hackthebox.com/machines/EscapeTwo

#### Look for problems with AD Certificate Services using a user and password
```bash
certipy find -u 'ca_svc@sequel.htb' -p 'Password123!!' -dc-ip 10.10.11.51 -stdout
```


