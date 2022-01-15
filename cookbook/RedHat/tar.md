# List files in archive only:

```
tar --gzip --list --verbose --file=archive.tar
```

# Extract:

```
tar -xzvf archive.tar.gz -C /tmp
```

# Exclude Stuff

```
tar -czvf archive.tar.gz /home/ubuntu --exclude=/home/ubuntu/Downloads --exclude=/home/ubuntu/.cache --exclude=*.mp4
```

# Tar and compress dir:

```
tar -czvf name-of-archive.tar.gz /path/to/directory-or-file
```
