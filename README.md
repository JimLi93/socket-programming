# Introduction to Computer Networks <br> <small>Assignment 1</small>



## Part 1 : UDP Pinger

Write UDPPingerClient.py using provided file UDPPingerServer.py.

### Server Specifications :

* In an infinite loop for listening for incoming UDP packets.

### Client Specifications : 

* Set timeout of 1 second for server reply.

* Send 10 ping to the server using UDP.

* If no reply received within 1 second, print "Request timed out."

* If received reply, print round-trip-time.

### Run the Program

`python3 UDPPingerServer.py`

`python3 UDPPingerClient.py`

## Part 2 ICMP Messages

Create ICMP socket and parse the received ICMP packets.

### Client Specifications : 

* Create additional thread and an ICMP socket.

* Set timeout of 1 second for server reply.

* Send 10 ping to the server using UDP, and wait for ICMP reply.

* Once received ICMP packet, parse and print it.

### Run the Program

`python3 UDPClient.py`

## Part 3 UDP Traceroute

Implement traceroute application using UDP request and ICMP reply messages.

### Code Specifications

* Set timeout of 1 second on the ICMP socket.

* Realize traceroute with destination IP: 140.114.89.43

* Print the router name, IP address, and RTT.

### Run the Program

`python3 traceroute.py`