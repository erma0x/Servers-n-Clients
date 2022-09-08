#!/usr/bin/env python

# librerie built-in
import sys
import os
import socket
from datetime import datetime
import socket, ssl
from pprint import pprint
from server import Port

PATH_MESSAGGI ='messaggi.txt'
PORTA_SERVER = 8081
IP_SERVER = socket.gethostname()
CLIENT_ID = socket.gethostname()
PORTA_CLIENT = 8081


def server():
    
    while True:

        context = ssl.create_default_context()
        cipher = 'ECDHE-ECDSA-AES128-GCM-SHA256'#'DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:ECDHE-ECDSA-AES128-GCM-SHA256'
        context.set_ciphers(cipher)

        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('dasduygsaidu')
        #sslSocket = context.wrap_socket(s, server_hostname = CLIENT_ID,port_number=PORTA_CLIENT)
        #sslSocket.bind((IP_SERVER,PORTA_SERVER))

        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain('cert.pem', 'cert.pem')
        
        with socket.create_connection((CLIENT_ID, PORTA_CLIENT)) as sock:
            with context.wrap_socket(sock, server_hostname=CLIENT_ID) as ssock:
                ssock.bind((CLIENT_ID, PORTA_CLIENT))
                ssock.listen(30)
                conn, addr = ssock.accept()
                        
                

if __name__ == '__main__':
    server()