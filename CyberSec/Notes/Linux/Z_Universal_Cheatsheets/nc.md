## The Classic listen for your reverse shell!

```
nc -lvnp 4444
```

## Send recive file via tar

```
#Receiving End

nc -l -p 1234 | tar xvfp -

#Sending End

tar cfp - /some/dir | nc -w 3 [destination] 1234
```

## Just send a file

#Recieving End
```
nc -l -p 1234 > out.file
```

#Sending End
```
nc -w 3 [destination] 1234 < out.file
```

## Enmurate Rsync or grab headers

```bash

  nc -vn 10.129.228.37 873

```
