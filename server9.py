import socket, ssl
from pprint import pprint

context = ssl.create_default_context()

cipher = 'ECDHE-ECDSA-AES128-GCM-SHA256'#'DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:ECDHE-ECDSA-AES128-GCM-SHA256'
context.set_ciphers(cipher)
print(cipher)
print('_'*80)
pprint(context.get_ciphers())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

domain = 'google.com'

sslSocket = context.wrap_socket(s, server_hostname = domain)

sslSocket.connect((domain, 443))
sslSocket.close()
print('closed')