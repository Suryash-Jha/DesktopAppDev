# Python Program to Get IP Address
# import socket
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)

# print("Your Computer Name is:" + hostname)
# print("Your Computer IP Address is:" + IPAddr)



# to extract ipv4 id of wireless device
# ip addr show wlp2s0 | grep -Po 'inet \K[\d.]+'
import os

print(os.popen("ipconfig | awk '/IPv4 Address/' | awk 'END{print}' | awk '{print $14}").read())

# ipconfig | awk '/IPv4 Address/' | awk 'END{print}' | awk '{print $14}'
