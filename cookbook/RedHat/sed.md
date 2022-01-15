# Pull out IPs without port numbrs form tcpdump headers:

**Note the "sed -r" so you don't have to do any backspacing**

```
sed -r 's/([0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3})[.][0-9:]+/\1/g'
```

# Sed Spagetti

```
sed 's/[0-9.]*389//g' | sed 's/[: ]//g' | sed 's/[0-9]*[.][0-9]*$//g'
```

# Replace whole line in file with something

```
sed -i 's/.*THREE.*/\#/g' test.txt
```

# sed replace:

```
sed 's/\./ /g'
```
