from socket import *
import time

DESTINATION = '140.114.89.43'
PORT = 554
MAX = 30

hop = 1

while 1:
    start_time = time.time()
    timeArray=list()
    addr = 0
    name = 0
    
    for i in range(3):
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.setsockopt(SOL_IP, IP_TTL, hop)
        clientSocket.sendto(''.encode(), (DESTINATION, PORT))
        iSocket = socket(AF_INET, SOCK_RAW,IPPROTO_ICMP)
        start_time = time.time()
        iSocket.settimeout(1)
        try:
            data, addr = iSocket.recvfrom(1024)
            timeArray.append(time.time()-start_time)
            addr = addr[0]
            try:
                name = gethostbyaddr(addr)[0]
            except:
                name = addr
        except :
            timeArray.append(0)
            pass
            iSocket.close()
            clientSocket.close()
    

    timeArray[0] = str(round(timeArray[0]*1000, 3))
    timeArray[1] = str(round(timeArray[1]*1000, 3))
    timeArray[2] = str(round(timeArray[2]*1000, 3))
        
    if timeArray[0] == '0' and timeArray[1] == '0' and timeArray[2] == '0':
        print(str(hop) + "  " + "* * * Request timed out")
    elif timeArray[0] != '0' and timeArray[1] == '0' and timeArray[2] == '0':
        print(str(hop) + "  " + str(name) + " (" + str(addr) + ") " + timeArray[0] + " ms " +  " * * ")
    elif timeArray[0] == '0' and timeArray[1] != '0' and timeArray[2] == '0':
        print(str(hop) + "  " + str(name) + " (" +  str(addr) + ") " + " * " + timeArray[1] + " ms " +  " * ")
    elif timeArray[0] == '0' and timeArray[1] == '0' and timeArray[2] != '0':
        print(str(hop) + "  " + str(name) + " (" +  str(addr) + ") " + " * * " + timeArray[2] + " ms ")
    elif timeArray[0] != '0' and timeArray[1] != '0' and timeArray[2] == '0':
        print(str(hop) + "  " + str(name) + " (" +  str(addr) + ") " + timeArray[0] + " ms " + timeArray[1] + " ms " +  " * ")
    elif timeArray[0] == '0' and timeArray[1] != '0' and timeArray[2] != '0':
        print(str(hop) + "  " + str(name) + " (" +  str(addr) + ") " + " * " + timeArray[1] + " ms " + timeArray[2] + " ms ")
    elif timeArray[0] != '0' and timeArray[1] == '0' and timeArray[2] != '0':
        print(str(hop) + "  " + str(name) + " (" +  str(addr) + ") " + timeArray[0] + " ms " + " * " + timeArray[2] + " ms ")
    else:
        print(str(hop) + "  " + str(name) + " (" +  str(addr) + ") " + timeArray[0] + " ms " + timeArray[1] + " ms " + timeArray[2] + " ms ")

    hop += 1
    if addr == DESTINATION or hop > MAX:
        break

