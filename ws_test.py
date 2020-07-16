import websocket
import time

# Connect to WebSocket server
ws = websocket.WebSocket()
ws.connect("ws://192.168.1.17")
print("Connected to WebSocket server")

# Wait for server to respond and print it
while (1) :
   fh = open("/var/www/html/index.html", "a")
   result = ws.recv()
   now = time.localtime()
   current_time = time.strftime("%H:%M:%S", now)
   print("Received HR: " + result + " at " + current_time)
   fh.write("<p>Received HR: " + result + " at " + current_time + "</p>")
   ws.send(result)
   fh.close()

# Gracefully close WebSocket connection
ws.close()
