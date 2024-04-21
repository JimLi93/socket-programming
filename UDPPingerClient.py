from socket import *
import time

clientSocket = socket(AF_INET, SOCK_DGRAM)
loss = 0
average_time = 0

for i in range(1,11):
    clientSocket.sendto(''.encode(), ('140.114.89.43', 55555))
    clientSocket.settimeout(1)
    start_time = time.time()
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        ans = (time.time() - start_time)*1000
        average_time += ans
        print("PING " + str(i) + " " + str(round(ans, 3)))
    except:
        print('Request times out.')
        loss+=1
if loss != 10:
    average_time = average_time / (10 - loss)   
else:
    average_time = 0  
print("Result:")
print("Average RTT " + str(round(average_time, 3)))
print("Packet loss rate " + str(loss/10))