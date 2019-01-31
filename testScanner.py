#Test scanner

import ipaddress, socket

def realdeal():
    for i in ipaddress.IPv4Network('10.73.11.0/24'):
        fqdn = socket.getfqdn(i)
        print(i + ' fqdn is ' + fqdn)

def ipcounter():
    for i in ipaddress.IPv4Network('10.73.11.0/24'):
        print(i)

def fqdntest():
    fqdn = socket.getfqdn('10.73.11.85')
    print(fqdn)

realdeal()
#ipcounter()
#fqdntest()

# Need to validate the ip address input to see if it's even a valid address
# find a way to fast fail the dns lookup so it doesnt take 5 seconds each failure
