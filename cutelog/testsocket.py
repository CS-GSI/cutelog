import socket
import json

TCP_IP = '127.0.0.1'
TCP_PORT = 19996
BUFFER_SIZE = 1024


log = {"name": "MyServer.ReqHandler", "level": "warning", "created": 1528702099, 
 "msg": "User registered", "username": "bob", "id": 13525, "bla": "lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls \\n \n \r kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas \n lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas lls kdmas "}
log = json.dumps(log)
head = bytearray(len(log).to_bytes(4, 'big'))
payload = bytearray(log, 'utf-8')
arr = head + payload

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(arr)
s.close()
