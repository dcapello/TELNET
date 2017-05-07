import getpass
import sys
import telnetlib

ROUTERS = 2
HOST = "192.168.56.101"
COMMANDS = ["\r", "enable\r", "terminal length 0\r", "show running-config\r"]
PATH = "C:/Users/hades_000/vmmaestro/workspace/My Topologies/OSPF LAB/Ro"

FIRST_PORT = 2001
TELNET = telnetlib.Telnet()

for I in range(ROUTERS):
    TELNET.open(HOST, FIRST_PORT + I)
    TELNET.write(COMMANDS[0].encode('ascii'))
    TELNET.write(COMMANDS[1].encode('ascii'))
    TELNET.write(COMMANDS[2].encode('ascii'))
    TELNET.write(COMMANDS[3].encode('ascii'))
    TELNET.read_until("service password-encryption".encode('ascii'), 5)
    FILE = open(PATH + str(I + 1) + ".txt", 'w')
    FILE.write((TELNET.read_until("!\r\nend".encode('ascii'), 5)).decode())
    FILE.close()
    TELNET.close()

exit(0)
