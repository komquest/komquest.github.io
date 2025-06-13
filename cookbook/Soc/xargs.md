# Gunzip Search

```
fgrep 'IP' * | fgrep 'dns' | cut -f2 | xargs -i gunzip -c {} | smb | grep IP
```
