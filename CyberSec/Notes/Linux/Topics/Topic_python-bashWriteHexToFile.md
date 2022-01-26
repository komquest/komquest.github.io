# Python Script that converts user input hex representations into actual binary hex: (python 2)

```python
#!/usr/bin/python

#This script will take in a hex characters and write to actual binary


import argparse
import sys
import struct

parser = argparse.ArgumentParser(description='Get My Hex in raw human-readable format')
parser.add_argument('strings', nargs='+', default="0")
args = parser.parse_args()

count = 0
carry = ""

for i in args.strings[0]:
        if count == 0:
                carry += i
                count += 1
        elif count == 1:
                carry += i
                convertMe = int("0x" + carry, 16)
                sys.stdout.write(struct.pack('>B', convertMe))
                count = 0
                carry = ""

```

# Bash Examples:

```bash
python -c "import struct;import sys; sys.stdout.write(struct.pack('>hh', 0x3344,0x1122))" | hexdump -C

Swap 2 byte hex values
dd if=cve20200601Test.bin of=cve20200601TestSwapped.bin conv=swab

Dump raw hex
xxd -p test.pcap
```

# Bash write to hex:

```
perl -e 'print pack "H*", "deadbeef"' > hexfile.bin
printf %b '\xde\xad\xbe\xef' > hexfile.bin
python -c "import struct;import sys; sys.stdout.write(struct.pack('hh', 0x3434,0x5454))" > hexfile.bin

```
The perl way is the easiest method since you don't have to put in any extra chars. However, the python method  you can compensate for system endianess thus writing correct hex so things are not backwards.

# Python Console Examples:

```python
Python 2.6.6 (r266:84292, Jun 11 2019, 11:01:44)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-23)] on linux2
Type "help", "copyright", "credits" or "license" for more information.

>>> import struct

>>> struct.pack('h',0x1234)
'4\x12'
>>> struct.pack('hxx',0x1234)
'4\x12\x00\x00'
>>> struct.pack('x',0x1234)
>>> struct.pack('f',0x1234)
'\x00\xa0\x91E'
>>> struct.pack('<f',0x1234)
'\x00\xa0\x91E'
>>> struct.pack('>f',0x1234)
'E\x91\xa0\x00'
>>> struct.pack('>H',0x1234)
'\x124'
>>> struct.pack('!i',0x1234)
'\x00\x00\x124'
>>> struct.pack('!i',0x123A)
'\x00\x00\x12:'                       
>>> struct.pack('!i',0x123A)
'\x00\x00\x12:'
>>> struct.pack('!i',0x123A)
'\x00\x00\x12:'
>>> struct.pack('!i',0x123A3B)
'\x00\x12:;'
>>> struct.pack('!i',0x123A12)
'\x00\x12:\x12'
>>> struct.pack('!i',0x123A12)

```

**Note**: when the hex is displayed back, known characters are auto translated to their respective ASCII representation.

# Links (Python Struct)
https://docs.python.org/2/library/struct.html

-->This is a builtin library thus no extra downloading required!

# Link (Tutorial Video)
https://www.youtube.com/watch?v=FxNS-zSS7MQ&edufilter=NULL