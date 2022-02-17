import ipapi

ip = input("Informe o IP que deseja informações: ")

print(ipapi.location(ip))

import sys

sys.stdout = open('IPAPI.log', 'a')
