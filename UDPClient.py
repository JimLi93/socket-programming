from socket import *
import threading
import time
loss = 0
average_time = 0
message=''
def job():
    while True:
        global stop_threads
        if stop_threads: 
            break
        try:
            data, addr = isocket.recvfrom(1024)
            isocket.settimeout(1)
            type = int.from_bytes(data[20:21], byteorder='big')
            code = int.from_bytes(data[21:22], byteorder='big')
            if type==0 and code==0:
                print("ICMP Info: type=0, code=0, message: echo reply")
            elif type==3:
                if code==0:
                    print("ICMP Info: type=3, code=0, message: destination network unreachable")
                elif code==1:
                    print("ICMP Info: type=3, code=1, message: destination host unreachable")
                elif code==2:
                    print("ICMP Info: type=3, code=2, message: destination protocol unreachable")
                elif code==3:
                    print("ICMP Info: type=3, code=3, message: destination port unreachable")
                else:
                    print("ICMP Info: type=3, code=" + str(code) + ", message: destination unreachable")
            else:
                print("ICMP Info: type=" + str(type) + ", code=" + str(code) + ", message: other messages")
        except timeout:
            pass

    

clientSocket = socket(AF_INET, SOCK_DGRAM)
isocket = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)

stop_threads = False
t = threading.Thread(target=job)
t.start()

for i in range(1,11):
    clientSocket.sendto(message.encode(), ('140.114.89.43', 55556))
    clientSocket.settimeout(1)
    start_time = time.time()
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        end_time = time.time()
    except timeout:
        pass
       
stop_threads = True
t.join()
