## Look for base naming constructs

```
ldapsearch -x -h 10.10.10.175 -s base naming contexts
```

## Dump information

```
ldapsearch -x -h 10.10.10.175 -b 'DC=EGO, DC=LOCAL' -s sub
```