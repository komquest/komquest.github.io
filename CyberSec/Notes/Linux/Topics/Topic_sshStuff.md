# SSH Hacks
--> (Setup SSH Port forwarding)

http://matt.might.net/articles/ssh-hacks/

# SSH Konami Codes

--> Create forwards after you connect

https://www.sans.org/blog/using-the-ssh-konami-code-ssh-control-sequences/

# SSH Setup User that only is allowed to forward
--> This user will also only use key based auth

## Links
https://askubuntu.com/questions/48129/how-to-create-a-restricted-ssh-user-for-port-forwarding

https://unix.stackexchange.com/questions/14312/how-to-restrict-an-ssh-user-to-only-allow-ssh-tunneling

https://serverfault.com/questions/285800/how-to-disable-ssh-login-with-password-for-some-users

https://www.ssh.com/ssh/keygen/

## Steps:

1) Create User

```
useradd --shell /bin/bash username
```

2) Generate ssh keypair and upload
--> Make sure to not password protect the key since this will be used in scripts

```
ssh-keygen -f ~/.ssh/forwards.key -t ecdsa -b 521

ssh-copy-id -i ~/.ssh/forwards.key user@host
```

3) Login as username with public key to make sure you have a shell and everything is working

4) Logout, Login as root and change "etc/passwd" shell for username to 
```
/bin/false
```

5) lock down user in ssh_config, add this:

```
Match User username
    PasswordAuthentication no
    PubkeyAuthentication yes
    PermitEmptyPasswords no
    GatewayPorts no
    X11Forwarding no
    AllowAgentForwarding no

    #Additional Options based off your config:
    #ForceCommand /bin/false
    #Disables "-R":
    #AllowTcpForwarding yes 
    #PermitOpen localhost:62222
    #PermitTunnel no
```

6) Restart SSH Server

7) username should now be only able to forward ports, verfiy by trying to do scp, sftp and direct commands with ssh.

## Here are my scripts I used to bridge two hosts together over different NATs. One was Windows (The server I was connecting to) and one was Linux (The Client I Wanted to connect from)

Windows:

```
start cmd /c ssh -i .\forwards user@172.16.16.66 -N -R 2201:127.0.0.1:9999
start cmd /c ssh -i .\forwards user@172.16.16.66 -N -R 2202:127.0.0.1:27000
```

Linux:

```
ssh -i ~/.ssh/forwards -N -L 2201:localhost:2201 user@172.16.16.66 &
ssh -i ~/.ssh/forwards -N -L 2202:localhost:2202 user@172.16.16.66 &
```

# Locally Expose SSH Tunnel for local forwards:

```
ssh john@192.168.1.12 -L 0.0.0.0:8500:10.10.10.23:8500 -N
```

## Note, make sure you set "Gateway Ports" to "yes" in your sshd_config!

# Port Forward and Double Hop with SSH

```
ssh -L 5555:10.10.10.8:3389 -J dog@192.168.1.12 cat@192.168.122.36

```

# Mini Tutorial SSH port forwarding:

Purpose: This will show off a simplified use of ssh port forwarding. For some reason it took me a second to figure it out and I don't want to forget so here is any easy and quick explanation:

THE BASIC IDEA:
ssh port forwarding creates a tunnel between a client and a server and you can use this encrypted tunnel to forward stuff between the two. This is a layer 4 technology thus it uses ports and IP addresses to forward.

EXAMPLE:
I can use this to create a secure tunnel between my home PC and work PC, and use my work PC as jump to a file server on my work network (this is local fowarding) (more explanation below)

source:
https://www.ssh.com/ssh/tunneling/example

Uses: Creating back doors, exfiltration, proxying, bypassing firewalls, etc. 

First off some definitions:

client = the device running the ssh client
server = the device running the ssh server
host = the destination of the tunnel (this can be the same as the server or be a completely different device depending on your setup.)
request = something that uses the tunnel created between the client and the server

**Local Forwarding**
I call this "Client Bounce" since you start at the client which will forward (Bounce) to the server and then (Bounce) to the host:

(AMAZING DIAGRAM) (SSH initiated from client)
request--> client  --> TUNNEL --> server --> host

*note: the host can be the server or something else, depending on what you setup, examples to follow:

EXAMPLES (using OpenSSH):

```
ssh -L 80:localhost:80 root@server

```
--> As per the "AMAZING DIAGRAM" this will create a listen on the client at port 80 (run netstat to verify) if ANY requests (yes from the client or ANY other device hitting port 80 on the client) hit it. After that it will send this request through the tunnel and push it out of the server in this case since we specified "localhost:80" the request will stay on the server (thus host is the same as server in this case) and hit port 80. Therefore if a web app was running on the server, hitting port 80 on the client will allow access to this app. 

```
ssh -L 127.0.0.1:80:ftp.internalServer.local:21 root@server

```

--> Here is an example when the host is different from the server (and with a special "127.0.0.1" added in). Thus, this tunnel will push requests on the client to the server WHICH WILL THEN forward this request FROM THE SERVER to "ftp.internalServer.local:21" thus hitting the ftp server or whatever is hosted on port 21. Note the connection between the server and the "ftp.internalServer.local" is unencrypted (tunnel is only between the client and server) so beware!

Also the "127.0.0.1" simply makes it so only requests from the local client can be made to the server. Otherwise, as stated in the first example ANYTHING that connects to the client can use the the tunnel!

**Remote Forwarding**

So this basically the reverse of Local forwarding. I call this "Server Bounce" since you bounce requests off the server which will forward (Bounce) to the client and then the host. However with this said everything is initiated from the client, this is what confused me the most!

(AMAZING DIAGRAM) (SSH initiated from client)
 
request --> server --> TUNNEL --> client --> host

To clarify a bit,  if my client was my work computer and my server was a personal server on the cloud, I could bypass my company's firewall thanks to STP (stateful packet inspection). On top of that everything is encrypted which makes it pretty difficult to figure out what is going on.

EXAMPLES

```
ssh -R 2222:localhost:22 root@server

```

This will connect to the server and open port 2222 on it. If this port is accessed by a request it will then be forwarded to port 22 on the client (which could be an ssh service or something else). In this case my host is also my CLIENT.

```
ssh -R 2222:d76767.nyc.example.com:22 -R 5432:postgres3.nyc.example.com:5432 aws4.mydomain.net

```

This example I stole from the internet (see source above).  This is cool because it opens two tunnels to a host that is different from the client (nyc.example.com). Basically it is the same idea though, you start on the client connect to the server and then on the server ports 2222 and 5432 or opened. Thus, when a request is sent to the server it will forward through the tunnel and go out on the client to the host (nyc.exmaple.com) through ports 22 and 5432 respectively. In this case the user on the client machine just opened ssh and sql on the internal network to the internet.


Conclusion:

As per source turn off forwarding if you do not need it, you can do this via the ssh config file (see source).  However this really only prevents using company resources (ssh servers). For personal servers on the internet, good firewall-ing is your best bet. Whilelisting as well as background screening of employees could assist too.

# SSH LOCAL FORWARDING
--> use this to bind a local port to a remote server port through ssh.
--> This can be used to bypass socket services that should only be accessed by localhost. And the best part about this is that you can do this as a normal user. However Privileged ports are restricted to root.

```
ssh -L [Bind address, or remote address:]5602:127.0.0.1:5601
```