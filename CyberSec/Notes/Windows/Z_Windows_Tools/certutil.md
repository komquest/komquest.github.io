--> Download file from web server

```
certutil.exe -urlcache -split -f https://myserver/filename outputfilename
```

--> Base64 Encode/Decode:

```
certutil.exe -encode inputFileName encodedOutputFileName
certutil.exe -decode encodedInputFileName decodedOutputFileName
```