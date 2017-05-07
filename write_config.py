import telnetlib
from ciscoconfparse import CiscoConfParse


ROUTERS = 2
HOST = "192.168.56.101"
COMMANDS = ["\r", "enable\r", "terminal length 0\r", "config t\r"]
PATH = "C:/Users/hades_000/vmmaestro/workspace/My Topologies/OSPF LAB/Ro"

FIRST_PORT = 2001
TELNET = telnetlib.Telnet()
CONFIG = CiscoConfParse()

for I in range(ROUTERS):
    TELNET.open(HOST, FIRST_PORT + I)



