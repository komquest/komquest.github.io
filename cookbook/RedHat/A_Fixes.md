
# Check for Devices (Hard-Drives)
```
#lists all drives and partitions system sees
lsblk

#Shows all devices system sees
dmesg
```

# Fork Retry: Resource Temporarily Unavailable

If you want to fix it:

```
ulimit -a # Check your limits
ulimit -u # Check your processes
ulimit -u 2048 # increase amount to this number (or type unlimited, but this can be dangerous) 
```

Sources:
https://access.redhat.com/solutions/543503
https://unix.stackexchange.com/questions/205016/fork-retry-resource-temporarily-unavailable
https://developer.ibm.com/answers/questions/195937/how-to-resolve-error-bash-fork-retry-resource-temp/


# Troubleshoot Account Locked:
## Check user password information and last logins
```
chage -1 USER
last
lastb

lastb | head -n 100
```

# Important locations

## Barnyard Troubleshooting:
```
#logfiles
/var/log/message | grep barnyard2

#lock files
/var/lock/subsys/
/var/data/snort/
```

## Apache web server folder
```
/var/www/
```

## Crontab locations:
```
/var/spool/cron/
/etc/crontab
```
## Check to see if IP forwarding is enabled between local NICS
```
/proc/sys/net/ipv4/ip_forward
```

## Nameservers Redhat is using:
```
/etc/resolv.conf

```

## Running Processes
```
/var/run
```

## Service Folder:
```
/etc/init.d/
```
