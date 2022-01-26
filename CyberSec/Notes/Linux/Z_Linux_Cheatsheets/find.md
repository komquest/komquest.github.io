## Find suid bins:

```
find / -perm 4000 -ls 

find / -perm -u=s -type f 2>/dev/null
```

## Find all files owned by user

```
find / -user Bob 2>/dev/null
```

## See all files in current dir

```
find .
```

## Find Writeable dirs

```
 find / -writable -type d 2>/dev/null
```