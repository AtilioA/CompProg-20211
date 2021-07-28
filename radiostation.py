n, m = list(map(int, input().split()))
servers = dict()
config = dict()

for line in range(n):
    serverName, ip = input().split()
    servers[ip] = serverName

for line in range(m):
    command = input()
    serverName, ip = command.split()
    print(command, '#{}'.format(servers[ip[:-1]]))
