import socket
import time
import ssl

PORTA_SERVER = 8081
PORTA_CLIENT = 8081
IP_SERVER = 'localhost' #socket.gethostname()
CLIENT_ID = 'localhost' #socket.gethostname()


while True:
    # context = ssl.create_default_context()
    # cipher = 'ECDHE-ECDSA-AES128-GCM-SHA256'#'DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:ECDHE-ECDSA-AES128-GCM-SHA256'
    # context.set_ciphers(cipher)
    # context.load_cert_chain( certfile='cert.pem', keyfile='key.pem')

    context = ssl.create_default_context()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        with context.wrap_socket(sock, server_hostname=IP_SERVER) as ssock:
            ssock.connect((IP_SERVER, 8081))
            ssock.send(bytes('hello'.encode()))
            time.sleep(1)
