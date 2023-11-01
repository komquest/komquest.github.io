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
awk '{print $1”\n”$2}'
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

## Specify Separator and use regex to find lines in file, then display with formatting from columns:

```
awk -F : '/root/ { print $4 " " $1 }' /etc/passwd

0 root
1 bin
2 daemon
4 adm
7 lp
```
