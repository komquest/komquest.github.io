## Install xrdp on RHEL 9

```bash
# Install EPEL
sudo subscription-manager repos --enable codeready-builder-for-rhel-9-$(arch)-rpms
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm

# Install Packages

sudo dnf install tigervnc-server xrdp

# Start and Enable Service

sudo systemctl start xrdp.service
sudo systemctl status xrdp.service
sudo systemctl enable xrdp.service

# Open Port In firewall

sudo firewall-cmd -–permanent –-add-port=3389/tcp
sudo firewall-cmd –-reload

# Reboot 

reboot

# It should work now, connect via mstsc/rdp client
```

## Check for Devices (Hard-Drives)
```
#lists all drives and partitions system sees
lsblk

#Shows all devices system sees
dmesg
```

## Fork Retry: Resource Temporarily Unavailable

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


## Troubleshoot Account Locked:
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
