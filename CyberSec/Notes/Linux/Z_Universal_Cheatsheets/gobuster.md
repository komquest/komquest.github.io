
## Common query

```
gobuster dir -u http://academy.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

## Common Query 2

```
gobuster dir -u http://10.10.10.95:8080 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

## Exclude Length

```
gobuster dir -u http://academy.htb/home.php/ -c 'PHPSESSID=e1o8eoof0hc9qno7p15kghh7tb' -f --random-agent --exclude-length 54914 -r -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

## Exclude Length, only return stuff that is above zero

```
gobuster dir --exclude-length 0 -u http://10.10.10.152 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

## Use Blacklists

```
gobuster dir -u http://academy.htb/ -c 'PHPSESSID=e1o8eoof0hc9qno7p15kghh7tb' -b '404,500' --random-agent -r -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

## Ignore ssl

```
gobuster dir -k -u https://git.laboratory.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

## Look for files with extensions:

```
gobuster dir -u http://10.10.10.93/uploadedfiles/  -x .asp,.aspx,.jpg,.txt,.html -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

## Verbose Output, see what urls you are accessing:

```
gobuster -v dir -e -k -u http://192.168.174.128:88  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

## Search for subdomains with a root domain
- Note: if you find sub domains, make sure to add it to your hosts file or "real" dns will be queried!
- "append-domain": this makes it so that you can use a list of words that will be appended to host
```
gobuster vhost -u vulnnet.thm -w ./a.txt -v --append-domain
```


