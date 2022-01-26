--> Basic Enmuration

```
smbmap -H 10.10.10.3
```
--> Check what shares you have with login creds

```
smbmap -H 10.10.10.172 -u SABatchJobs -p SABatchJobs
```

--> Recursivly Cheack through a share

```
smbmap -H 10.10.10.172 -u SABatchJobs -p SABatchJobs -R 'users$'
```

--> Search and Download individual Files

```

smbmap -R Replication -H 10.10.10.100 -A Groups.xml -q

-R --> recursive
-H --> Host
-A --> Search for and download
-q --> quiet, only report things your find

```

--> Search and Download all files from a share:

```
smbmap -R Backups -H 10.10.10.134 -q -A '.*' -u guest
```

--> Enmurate, search for "Users"

```
smbmap -d active.htb -u svc_tags -p GPPstillStandingStrong2k18 -H 10.10.10.100 -R Users
```

--> Login with a hash

```
smbmap -u L4mpje -p aad3b435b51404eeaad3b435b51404ee:26112010952d963c8dc4217daec986d9
```
