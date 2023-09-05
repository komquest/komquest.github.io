# Cut a file to a certain size and remove last line

```
head -c 500K file.sh | head -n - 1 > out.txt
```


# View multiple files with separators:

```
tail -n + 1 *.txt

```
