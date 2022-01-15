## SMB PSEXEC and IPC calls

```
* If you see and access to an "IPC$" (optcode 3) on a windows based machine, SMB is being used for RPC. View the article above for picture examples.

* For a create request, it is usually followed by a "Read" or "Write", thus you can see what is being done with the file

* For normal RPC calls made with IPC$ you can actually see within wireshark, the command executed (via the ioctrl 11). This can help to see what the user is up to. For stuff like PSEXEC, all commands are encrypted so you won't actually get to see much of what is going on.

* NTLM is unencrypted and you can see the username of the authentication request via SMB (Session Setup). Kerberos works differently with its TGS (Ticket Granting Server), thus you will need to consult Kerberos logs for user information. 

**If your network is setup to use Kerberos and NTLM is happening, then something might be wrong**
```

