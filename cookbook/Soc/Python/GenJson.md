# GenJson.py

```python
#!/usr/bin/python3

#This will generate sample Json files for used in processing by my test script

import argparse
import random



#Argument Parser
parser = argparse.ArgumentParser(description='Print Out a sample Json File!!!!')
parser.add_argument('number', type=int, nargs=1, help='Number of iterations')

args = parser.parse_args()

keyArray=  ['ts', 'uri', 'headers', 'dest_ip', 'source_ip']
valueArray= ['times', 'www.awesome.com/', 'header:', '192.168.1.', '10.10.10.']

passes=args.number[0]

maxKeys= (random.randrange(len(keyArray)) + 1)
jsonLine="{"

#Build Json Line
for i in range(passes):
    for j in range(maxKeys):
        jsonLine += "\"" + keyArray[j] + "\"" + ":" + "\"" + valueArray[j] + str(random.randrange(10)) + "\"" + ","
    jsonLine = jsonLine[:-1]
    jsonLine += "}"
    print(jsonLine)
    jsonLine="{"


    





```