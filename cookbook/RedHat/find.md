# Find Files you can write too

```
find / -type d \( -perm -g+w -or -perm -o+w \) -exec ls -adl {} \;
```

# Find all files in current dir and display there word count and sort

```
find . -type f -exec wc -l {} \; | sort -nr

```

# Find files based off of modification time and display in ls format:
```
find -mtime 80 -ls

```

# Find files in Past 100 days and display their properties:

```
find . -mtime 100 | ls -lh
```

# Find files based off of times: (in days)
```
-atime == access time
-ctime == file's status last changed
-mtime = file's data was last modififed

```

# Find and List Results in current dir
```
find . -ls
find . -ls -type f
```

# Find files while suppressing permission denied errors:
```
find -name "*ptrace*" -type f 2>&1 | grep -v "denied"
```

# Find files in past x hours:
```
find -type f -name *snort* -mmin -$((60*24))
```



