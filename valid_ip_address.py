"""
Create a function to verify if a string given as dotted-quad decimal is valid IPv4 address

With Python STL
socket.inet_aton(ip_string)
Convert an IPv4 address from dotted-quad string format (for example, ‘123.45.67.89’) 
to 32-bit packed binary format, as a bytes object four characters in length
"""

import socket
import ipaddress

def valid_ip_1(ip_addr):
    try:
        socket.inet_aton(ip_addr)
        print("Valid IP")
    except socket.error:
        print("Invalid IP")


def valid_ip_2(ip_addr):
    try:
        return ipaddress.IPv4Address(ip_addr)
    except Exception as e:
        return e    

# driver code
inp = "192.168.1.1"
print(valid_ip_1(inp))
print(valid_ip_2(inp))