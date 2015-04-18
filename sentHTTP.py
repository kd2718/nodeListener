# python code
# http://stackoverflow.com/questions/9746303/how-do-i-send-a-post-request-as-a-json
import requests
import json
import websocket

url = 'http://127.0.0.1:8080'

payload = {'myNum': 2718}
headers = {'content-type': 'application/json'}

ws = websocket.WebSocket()
ws.connect("ws://localhost:8080")
ws.send(json.dumps(payload))
out  = ws.recv()
print(out)

#r = requests.post(url, data=json.dumps(payload), headers=headers)
#print(r.text)