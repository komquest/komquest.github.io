## Send your bash history to null
syslink so that:

```
.bash_history -> /dev/null

```

## Run a command from a variable within shell (useful if you cannot copy or paste)

```
bash -ci $abc
```

## Fancy way to unzip files based off of regex search:
```
gunzip -c  $(ls | egrep '.\.06.*') | smb | grep 192.168.1.12 | grep 10.10.1.24
```

## Make multiple Files at once:
```
touch {a,b}

```

## Force Unset of Read Only environment Variables:
```
gdb -ex 'call unbind_variable("PI")' --pid=$$ --batch

gdb -ex 'info functions' --batch --pid=$$ | grep 'unbind'
```

## Concatenate, write to same file

```
echo a > f.txt; echo b >> f.txt

```

## Write Error Output to Null
```
2>/dev/null
```

