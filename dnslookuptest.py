import socket, re

#TODO POC dns lookup of ip address
    #addr1 = socket.gethostbyname('IN0L223469')
    #info1 = socket.getaddrinfo(addr1, 22)
    #hostname = socket.gethostbyaddr(addr1)
    #def printing():
    #    print(addr1)
    #    print(info1)
    #    print(hostname)
    #printing()

#TODO Find a way to look up hostnames of IP addresses > may need to do some weird stuff with DNS lookups for this since we need an A record or CNAME

import ipaddress, socket
for ip in ipaddress.IPv4Network('10.73.11.0/24'):
    ip = i
    fqdn = socket.getfqdn(i)
    print(i + ' fqdn is ' + fqdn)

#TODO Loop through all ip addresses in a range to do a ping test
    #TODO if successful then state the IP is active, then attempt DNS lookup
    #TODO if unsuccessful then move to the next ip addressin the range


#TODO Create a counter from 0 to 255
def counter():
    for i in range(0,255):
        i = i+1
        print(i)

networkRange = input('Please input the network starting address you want to scan: ')
subnetMask = input('Please enter the subnet mask: ')

print(networkRange)
print(subnetMask)

#TODO Validate input for network and subnet with regex. Can't just search for digits need to be specific on the 0-255 range

networkRegex = re.compile(r'[\d\d\d.\d\d\d.\d\d\d.\d\d\d]')

#[\d\d\d '.' \d\d\d '.' \d\d\d '.' \d\d\d]

nr = networkRegex.search(networkRange)
print('Network range validated: ' + nr.group())

# Enhancement define logic for ip address ranges (depending on subnetting should count from the start to the end of the subnet)
