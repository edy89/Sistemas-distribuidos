import socket
import SocketServer
import ntplib
import time
from datetime import datetime


form = "%H:%M:%S"

def updateTimeWeb():
    hour_web_req = ntplib.NTPClient()
    time_response = hour_web_req.request('pool.ntp.org')
    hours   = time.localtime(time_response.tx_time).tm_hour
    minutes = time.localtime(time_response.tx_time).tm_min
    seconds = time.localtime(time_response.tx_time).tm_sec

    hh_mm_ss = [hours,minutes,seconds]

    return hh_mm_ss



class miHandler(SocketServer.BaseRequestHandler):

   def handle(self):

    exit = False

    while not exit:

        time_client    = str(self.request.recv(1024))
        time_client    = datetime.strptime(time_client, form)
        hours_client   = time_client.hour
        minutes_client = time_client.minute
        seconds_client = time_client.second

        time_web    = updateTimeWeb()
        hour_web    = time_web[0]
        minutes_web = time_web[1]
        seconds_web = time_web[2]
        print seconds_web
        
        h = abs(int(hours_client)   - int(hour_web))
        m = abs(int(minutes_client) - int(minutes_web))

        if h > 1:
            hours_client = hour_web
            if m > 1:
                minutes_client = minutes_web
                seconds_temp = abs(int(seconds_client) - int(seconds_web))
                if seconds_temp >= 10: #Diferencia de 10 segundos para actualizar
                    seconds_client = seconds_web
            else:
                seconds_temp = abs(int(seconds_client) - int(seconds_web))
                if seconds_temp >= 10: #Diferencia de 10 segundos para actualizar
                    seconds_client = seconds_web
        else:
            hours_client   = hour_web
            minutes_client = minutes_web
            seconds_client = seconds_web

        response = str(hours_client)+':'+str(minutes_client)+':'+str(seconds_client)
        #response = hours_client+':'+minutes_client+':'+seconds_client
        self.request.send(response)
        print "Request time has been send!"            
    

def main():
   print 'Taller Cristian'
   host='localhost'
   puerto = 8557
   socket_client = SocketServer.TCPServer((host,puerto),miHandler)

   if socket_client:
    print "Server ON"
    socket_client.serve_forever()

main()