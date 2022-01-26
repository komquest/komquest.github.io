--> Check for open shares if anonymous login is enabled

```
smbclient -L 10.10.10.172
```

--> Login with user and view accessable shares:

```
smbclient -L \\\\10.10.10.172\\ -U SABatchJobs
```

--> Login to Share

```
smbclient -U 'SABatchJobs%SABatchJobs' \\\\10.10.10.172\\azure_uploads
```

--> Null Login to Check a Share

```
smbclient -U '%' \\\\10.10.10.100\\Replication
```

--> Mount an open samba share to your machine:

```
sudo mount -t cifs -o rw,guest,vers=1.0 //10.10.10.3/tmp /mnt/sm
b/
```

--> Download files Recursively

```
smbclient '\\server\share'
recurse ON
prompt OFF
cd 'path\to\remote\dir'
lcd '~/path/to/download/to/'
mget *
```

--> View local file system

```
!ls
```

## login to older SMB:

```
smbclient -N //10.10.10.3/tmp --option='client min protocol=NT1'

-N --> No password prompt
```