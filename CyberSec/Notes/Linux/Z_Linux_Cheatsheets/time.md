--> Display Current time in nice format:

```
date --utc +"%d-%m-%y %T"
```

## Change Time/TimeZones

```
timedatactl list-timezones

sudo timedatectl set-timezone UTC

sudo timedatectl set-time 15:58:30
sudo timedatectl set-time 20151120
sudo timedatectl set-time '2015-11-20 16:14:50'
```


## The Other way to change time:

```
date -s "2 OCT 2006 18:00:00"

#Then Sync with Hardware Clock:

hwclock --systohc


# ---

date -s "2 OCT 2006 18:00:00"; sudo hwclock --systohc

```

--> set timezone

```
sudo rm /etc/localtime
sudo ln -s /usr/share/zoneinfo/Etc/UTC  /etc/localtime

```


https://www.cyberciti.biz/faq/howto-set-date-time-from-linux-command-prompt/