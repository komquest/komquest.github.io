--> Use the man page to find all of the rpc commands

--> Login as null user:

```
rpcclient -U "" -N 10.10.10.172
```

--> Login as null user and enumerate system users:

```
rpcclient -U "" -N 10.10.10.172 -c enumdomusers`
```