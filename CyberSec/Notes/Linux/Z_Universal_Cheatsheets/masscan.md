## Scan Stuff:

```
sudo masscan -p80 10.0.0.0/8
```

```
sudo masscan -p80 10.11.1.0/24 --rate=1000 -e tap0 --router-ip 10.11.0.1
```

## Scan stuffs with ping

```
masscan 192.168.0.0/16 -p80 --banners --ping --adapter-ip 192.168.119.162 --rate 1000
```

## Scan stuffs and make sure your adaptors work correctly!!!

```
masscan 10.11.1.5 -p 445 -e tun0
```