# Use a Case statment with a default case

```
index=a_finance earliest=0 
| eval day=case(isnotnull(Amount), Amount, isnotnull(Debit),Debit, 1=1, 0)
| table Description day
```

# strftime to create your own custom time fields

```
eval times=strftime(_time,"%m-%Y")
```

--> with this you can use the _time field for each row and format it to what you want
--> Useful if you would like to create your own time fields for sorting purposes

# String Concatenation with Eval

```

index="a_iplogs2" earliest=0 | eval sourcetype=(sourcetype + date_zone)

```

# Write Over fields with Eval
--> This will reset all the values of "activity" to 1

```
index="a_iplogs2" | eval activity=1

```
