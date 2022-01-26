## login with password

```
mysql -u root -pGkEWXn4h4g8qx9fZ1 -h academy
```

## login to specific port

```
mysql -h 10.10.10.215 -P 33060
```

## Navigate through tables:

```
show tables;
show tables from {DB};
SELECT * FROM users;

# Select Database:
use DATABASE
```

## Show Databases:

```
show databases;
```

## Show Table Columns
```
describe {table}
```

## mySQL Basic survival kit:

```
#login:
mysql -u user -p

show tables from mysql;

select current_user(); 
select schema();

select * from mysql.user;
select user, password, host from mysql.user;

show events;

```