import ipapi

ip = input("Informe o IP que deseja informações: ")

print(ipapi.location(ip))

import io
with io.open('ipapi.log', "a", encoding="utf-8") as file:
    file.write(str(ipapi.location(ip)) + "\n" "\r\n")
