# python3

#ipRange = input('Please include the network address and either the subnet mask or CIDR notation for a full ping sweep: ')
# need to decide how to to create the logic of IP addressing (remember it's just base 10 math)

bits = int(input('How many bits in your network CIDR notation:  '))

# below is a good start but i need to work in some regex into the mix to determine if there is cidr notation or they are using the subnet mask

def convertIpRange():
    for i in bits:
        hosts = i % 8
        numHosts = 2 ** hosts 
        print(numHosts)

convertIpRange()


#for i in ipRange():
    #find a way to ping the ip address
        #if ping == success
        #   nslookup
        #else
        #    break (soft break, want to continue the loop)


# Add this in your own way, test the os.system command on nslookup and see what happens for POC
# https://stackoverflow.com/questions/26468640/python-function-to-test-ping
