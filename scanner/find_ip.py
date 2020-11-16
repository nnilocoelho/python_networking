#find your ip
import socket #modulo socket
from requests import get #modulo requisição

hostname = socket.gethostname() #obter hostname
local_ip = socket.gethostbyname(hostname) #obter ip local
public_ip = get('https://api.ipify.org').text #requisição api

#saidas: hostname, ip_local e ip_public
print(f'Hostname: {hostname}')
print(f'Local IP: {local_ip}')
print(f'Public IP: {public_ip}')

