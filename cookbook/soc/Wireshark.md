# look up specific frame numbers:

```
frame.number == 107113 or frame.number == 105645 or frame.number == 107258 or smb2
```

# Find Windows EXE
```
frame contains "MZ" and frame contains "program"
```

# SMB2 Optcode search (used to find usernames and files)
```
smb2.cmd == {optcode (decimal)}

```
https://wiki.wireshark.org/SMB2

```
* 0x00 SMB2/NegotiateProtocol

* 0x01 SMB2/SessionSetup

* 0x02 SMB2/SessionLogoff

* 0x03 SMB2/TreeConnect

* 0x04 SMB2/TreeDisconnect

* 0x05 SMB2/Create

* 0x06 SMB2/Close

* 0x07 SMB2/Flush

* 0x08 SMB2/Read

* 0x09 SMB2/Write

* 0x0a SMB2/Lock

* 0x0b SMB2/Ioctl

*  0x0c SMB2/Cancel

* 0x0d SMB2/KeepAlive

* 0x0e SMB2/Find

* 0x0f SMB2/Notify

* 0x10 SMB2/GetInfo

* 0x11 SMB2/SetInfo

* 0x12 SMB2/Break
```

# Another way to search for hex in a frame
```
frame contains "\x28\x29\x20\x7b\x20"
```

# Search for hex value in frame
```
frame contains 52:61:72:21:1a:07:00
```

# Search for file extension in smb2 
```
smb2.filename contains ".exe"


```

