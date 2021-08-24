import time

def log_it(id,message):
    
    with open('/home/pi/Desktop/mailLogs.txt', 'a') as f:
        f.write(f"{time.ctime()} - {id} {message}\n".format())
        f.close()
        
# log_it(23123,"one")
# log_it(23123,"two")
# log_it(23123,"three")