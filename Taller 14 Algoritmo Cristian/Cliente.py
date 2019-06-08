#cd desktop/Sistemas distribuidos/taller 14 Algoritmo Cristian
import socket
import sys
import time
import datetime
from datetime import datetime


form = "%H:%M:%S"

print 'Taller Cristian'
host = 'localhost'
puerto = 8557
socket_server = socket.socket()
socket_server.connect((host,puerto))
exit = False
time_client = "03:10:00"


def updateTime (time_x):
  hhmmss = time_x

  hhmmss = datetime.strptime(hhmmss, form)
  hours = hhmmss.hour
  minutes = hhmmss.minute
  seconds = hhmmss.second

  time.sleep(1)

  seconds = seconds + 1

  if(seconds == 60):
    seconds = 00
    minutes = minutes + 1

  if(minutes == 60):
    minutes = 00
    hours = hours + 1

  if(hours == 24):
    hours = 00

  hhmmss = str(hours)+':'+str(minutes)+':'+str(seconds)
  #time_x = hhmmss
  return hhmmss

u = 0
x = 0

while not exit:

  if u == 0:
    hour = updateTime(time_client)
    print hour
    u += 1
  else: 
    hour = updateTime(hour)
    print hour

  if u == 5:
    socket_server.send(hour)
    print "Request for update of time sent!"
    hour = socket_server.recv(1024)
    u = 1
  if x == 10:
    hour_temp = datetime.strptime(time_client, form)
    hours = hour_temp.hour
    minutes = hour_temp.minute
    seconds = hour_temp.second 
    seconds = seconds + 20
    hour_temp = str(hours)+':'+str(minutes)+':'+str(seconds)
    print hour_temp
    socket_server.send(hour_temp)
    print "Request for update of time sent!"
    hour = socket_server.recv(1024)
    x = 0

  u += 1
  x += 1