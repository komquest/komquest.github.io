__tags: python tech


### Quick and Dirty Web Post with JSON data:
#### websocket is not part of standard lib
```python
#pip insatll websocket-client
import json
import websocket

ws = websocket.WebSocket()
ws.connect("ws://bagel.htb:5000/")
json_value= {"WriteOrder": "HereIsTest"}
data = str(json.dumps(json_value))
ws.send(data)
print(ws.recv())
ws.close()
```

