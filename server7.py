import socket
import ssl

PORTA_SERVER = 8081
PORTA_CLIENT = 8081
IP_SERVER =  'localhost'#socket.gethostname()
CLIENT_ID = 'localhost'#socket.gethostname()
print(IP_SERVER,PORTA_SERVER)

while True:
    # context = ssl.create_default_context()
    # cipher = 'DHE-RSA-AES128-SHA'#'ECDHE-ECDSA-AES128-GCM-SHA256'#'DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:ECDHE-ECDSA-AES128-GCM-SHA256'
    # context.set_ciphers(cipher)
    # context.load_cert_chain( certfile='cert.pem', keyfile='key.pem')

    context = ssl.create_default_context()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((IP_SERVER, PORTA_SERVER))
        sock.listen(1)
        
        with context.wrap_socket(sock, server_hostname=IP_SERVER) as ssock:
            conn, addr = ssock.accept()
            buf = conn.recv(64)
            if len(buf) > 0:
                print(buf) 
   
