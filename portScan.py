import socket
from IPy import IP
import concurrent
import concurrent.futures

class PortScan():

    banners = []
    open_ports = []

    def __init__(self, target, port_number):
        self.target = target
        self.port_number = port_number

    def scan(self):                           #scan when only one ip is given
        for port in range(1, (self.port_number+1)):
            self.scan_port(port)

    def check_IP(self):
        try:
            IP(self.target)
            return self.target
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan_port(self, port):
        try:
            converted_IP = self.check_IP()
            sock = socket.socket()              #this is socket descriptor(sock).
            sock.settimeout(0.5)                #this sets a time out interval for any one port
            sock.connect((converted_IP, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append(' ')

            sock.close()

        except: 
            pass