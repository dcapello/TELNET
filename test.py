FIRST_PORT = 17000
PORTS = []
for P in range(2):
    PORTS.append(FIRST_PORT + 2*P)
    print(PORTS[P])
exit(0)
