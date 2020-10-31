# port scanner

import socket
import threading
from queue import Queue

target = "10.0.0.1"
queue = Queue()
open_ports = []
closed_port = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f'"Port {port} is open')
            open_ports.append(port)
        else:
            print(f"Port {port} is closed")

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print(f'Open ports are:  {open_ports}')

