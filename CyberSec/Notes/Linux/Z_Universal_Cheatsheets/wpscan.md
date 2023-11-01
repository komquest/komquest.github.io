## Basic Scan

```
wpscan --url 10.10.10.88/webservices/wp/
```

## Basic Scan with aggressive Plugin detection

```
wpscan --url 10.10.10.88/webservices/wp/ --plugins-detection aggressive
```

## Another Type of Scan

```
 wpscan --url sandbox.local --enumerate ap,at,cb,dbe

 ap --> All plugins
 at --> All Themes
 cb --> Config Backups
 dbe --> DB exports
```

## Brute force passwords using username and password list:

```
wpscan --url http://robot.thm/wp-login.php -U Elliot -P ./realdic.txt
```
