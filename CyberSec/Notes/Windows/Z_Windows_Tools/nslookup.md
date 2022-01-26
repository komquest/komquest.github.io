--> Find if name exists on open server:
```
nslookup MEGABANK.local 10.10.10.172
```

--> Check NS records:
```
nslookup -type=ns MEGABANK.local 10.10.10.172
```

--> Soa Records:

```
nslookup -type=soa MEGABANK.local 10.10.10.172
```

--> Mx Records:

```
nslookup -type=mx MEGABANK.local 10.10.10.172
```

**--> Find all the available DNS records of a domain**

```
nslookup -type=any MEGABANK.local 10.10.10.172
```

--> Debug Mode:

```
nslookup -debug -type=any MEGABANK.local 10.10.10.172
```

