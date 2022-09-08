#!/bin/bash
import socket


if __name__ == '__main__':

    # TCP server basato su IPv4 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_number = 8081

    # Associa l'indirizzo IP e il numero di porta
    s.bind((socket.gethostname(),port_number))          

    # il numero di porta può essere compreso tra 0-65535 (di solito le porte non privilegiate sono > 1023)

    s.listen(port_number)
    print(f'lisening portnumber {port_number} ...')
    while True:
        clt, adr = s.accept()

        cmd = input(':> ')

        s.send(bytes( cmd ,"utf-8"))
        print(f'sending command: {cmd}')

        data = s.recv(2048)
        if data:
            print('data recived:\n\t {data}')
