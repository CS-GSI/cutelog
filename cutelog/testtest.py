import json
size = 4
size = 2

log = {"name": "MyServer.ReqHandler", "level": "debug", "created": 1528702099, 
 "msg": "User registered", "username": "bob", "id": 13525}

head = bytearray(len(str(log)).to_bytes(4, 'big'))
payload = bytearray(str(log), 'utf-8')
arr = head + payload

print(arr)


log = {"name": "MyServer.ReqHandler", "level": "debug", "created": 1528702099, 
 "msg": "User registered", "username": "bob", "id": 13525}
print(log)
log = "{\"name\": \"MyServer.ReqHandle\", \"level\": \"error\"}" 
print(log)

log = {"name": "MyServer.ReqHandler", "level": "debug", "created": 1528702099, 
 "msg": "User registered", "username": "bob", "id": 13525}
print(json.dumps(log))