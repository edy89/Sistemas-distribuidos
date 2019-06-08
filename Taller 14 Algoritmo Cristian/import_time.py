import time
import os
 
try:
    import ntplib
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    print (time.localtime(response.tx_time))
    
 
    # Si deseamos actualizar la fecha en Linux...
    #os.system('date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
except:
    print('No ha sido posible descargar la fecha')