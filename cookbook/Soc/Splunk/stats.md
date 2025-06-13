# Using the "where" clause to remove null valued fields:

```

index=a_finance host="fed" earliest="07/01/2020:00:00:00" latest="07/31/2020:23:59:00"
| eval day=case(isnull(Amount), Debit, isnull(Debit) AND Amount>0,Amount) 
| stats sum(day) as TOTAL by date_mday 
| sort date_mday 
| where NOT isnull(TOTAL)

```

# Create a Count for SparkLine

```

index=a_finance earliest=0 
|  stats sparkline count by host

```

# List distinct Values

--> So "list" displays everything while "values" only lists distinct values.

```

index="a_iplogs2" earliest=0 
|  stats count(activity) as Activity_Reports, dc(activity) as Total_Uniq, values(activity) as Types by IP

```

# List and Display Actions based off of Other
--> "list" can be used to display in a stat command

```
index="tutorial_data" sourcetype=access_* | fields + other,action | stats count(action), list(action) by other
```

# Random

```

stats latest(startTime) AS startTime, latest(status) AS status, latest(histID) AS currentHistId, earliest(histID) AS lastPassHistId BY testCaseId

```

# Search Transfer Rate by Host

```

sourcetype=access* | stats avg(kbps) BY host

```

# Remove duplicates in the result set and return the total count for the unique results

```

... | stats dc(host)

```

# Stats Doc Notes

**Syntax**

Simple: stats (stats-function(field) [AS field])... [BY field-list] 


Statistical and charting functions that you can use with the stats command. Each time you invoke the stats command, you can use one or more functions. However, you can only use **one BY clause**.

**Some functions are inherently more expensive, from a memory standpoint, than other functions**. For example, the distinct_count function requires far more memory than the count function. The values and list functions also can consume a lot of memory. 

```
**Aggregate functions** 	
avg()
count()
distinct_count()
estdc()
estdc_error()
exactperc<num>()
max()
median()
min()
mode()
perc<num>()
range()
stdev()
stdevp()
sum()
sumsq()
upperperc<num>()
var()
varp()
**Event order functions** 	
first()
last()
**Multivalue stats and chart functions**
 list()
values()
**Time functions** 
earliest()
earliest_time()
latest()
latest_time()
rate()

```



