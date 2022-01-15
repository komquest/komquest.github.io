# Basic IF/Then

```

index=* earliest=0 host=fed OR host=cap OR host=dis 
|  stats sum(Debit) as B, sum(eval(if(Amount>0,Amount,0))) as A by host

```
