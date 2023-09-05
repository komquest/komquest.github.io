# Recursive search find within files for text (case insensitive):

```
grep -ir "hello"
```

# Recursive search (used to find multiple files)

```
grep -r /path/*.txt
```

# You can search for blank lines with the following examples:

```
grep '^$' filename
```

# egrep 'and' and 'or' operators:

```
grep -E 'pattern1.*pattern2|pattern2.*pattern1' filename
```

# Negate egrep lookups:

```
grep "${PATT}" file | grep -v "${NOTPATT}"
```

# Display lines before and after match
```
cat myFile.txt | grep -A1 -B1 text
```

# Load Patterns from file and Compare
```
cat file1 | grep -f file2
```

# Match only IP Addresses
note: this does not take into account out stepping IPv4 bounds!

```
grep -E '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'


```

# Enable Colors
```
grep --color=always -z 'hello'

```

# Search for everything that is contained in a file
```
fgrep -f $Filename
```

# Return all with pattern's found highlighted
```
cat file.txt | grep --color=auto -izE 'google|microsoft|godaddy|digital ocean|cloudflare|amazon'

```

# Return Invert Search

```
grep -v "pattern"

```
