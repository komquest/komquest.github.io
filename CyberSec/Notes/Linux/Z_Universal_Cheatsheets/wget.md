
--> download recursivly, ignoring robots, don't check cert, keep it in specified domain thus ignore forign redirects, only go down 10, custom header with cookie

```
wget -r -np -l 10 --domains=".htb" --no-check-certificate --header='Cookie: PHPSESSID=e1o8eoof0hc9qno7p15kghh7tb' -e robots=off http://academy.htb
```


-->download all zip files from first layer of webpage!

```
wget -r -np -l 1 -A zip http://example.com/download/


-r,  --recursive          specify recursive download.
-np, --no-pa0rent          don't ascend to the parent directory.
-l,  --level=NUMBER       maximum recursion depth (inf or 0 for infinite).
-A,  --accept=LIST        comma-separated list of accepted extensions

-e robots=off --> turn off robots.txt restrictions
```

--> Rate Limit wget
--> wait one sec and limit to max speed of 50K download!

```
wget -r --wait=1 --limit-rate=50K -np -l 10 --domains=".htb" --no-check-certificate -e robots=off https://git.laboratory.htb/help/
```


--> download ftp recursivly

```
wget -r ftp://10.10.10.152/ProgramData/Paessler/
```

--> Use https proxy

```
wget --no-check-certificate -e use_proxy=yes -e https_proxy=127.0.0.1:8080 -S --method=OPTIONS https://valentine.htb/dev/
```

## Down everything from FTP server:

```
wget -mirror  'ftp://ftp_user:password@tally.htb.local'
```
