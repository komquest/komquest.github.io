## Print Last Item in a space separated Line

```
cat a.out | awk '{print $NF}'
```

## Print multiple items for comma separated list:

```
awk '{print $1"."$2"."$3"."$4}'
```

## Print 6th item in space separated values:

```
awk '{print $6}'
```

## Turn Spaces into NewLines
```
awk ā{print $1ā\nā$2}ā 
```

## Awk cool variables

```
NF = Number of feilds
NR = Current processed line
```
## Specify separator
```
awk -F "a" '{print $1}'

```
