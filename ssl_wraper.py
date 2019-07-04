import socket
import ssl,pprint

#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ssl_sock = ssl.wrap_socket(s,
#                            ca_certs="/etc/ssl/certs/ca-certificates.crt",
#                            cert_reqs=ssl.CERT_REQUIRED)
# ssl_sock.connect(('www.verisign.com', 443))
# pprint.pprint(ssl_sock.getpeercert())
# ssl_sock.close()
# ssl_sock=ssl.wrap_socket(s,ca_certs="/etc/ssl/certs/ca-certificates.crt",cert_reqs=ssl.CERT_REQUIRED)
# ssl_sock.connect(('www.verisign.com', 443))
# #pprint.pprint(ssl_sock.getpeercert())




# http_get = "GET / HTTP/1.0\r\n\r\n"
# req = bytes(http_get, 'utf-8')
# context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
# #context.verify_mode = ssl.CERT_REQUIRED
# context.load_verify_locations("/etc/ssl/certs/ca-certificates.crt")
# conn = context.wrap_socket(socket.socket(socket.AF_INET,socket.SOCK_STREAM))
# conn.connect(("136.243.69.14", 995))
# conn.sendall(req)
# pprint.pprint(conn.recv(1024))

def ssl_grabber(host, port):
    http_get = "GET / HTTP/1.0\r\n\r\n"
    req = bytes(http_get, 'utf-8')
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    #context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations("/etc/ssl/certs/ca-certificates.crt")
    conn = context.wrap_socket(socket.socket(socket.AF_INET,socket.SOCK_STREAM))
    conn.connect((host, port))
    conn.sendall(req)
    data=conn.recv(1024)
    conn.close()
    return data

# xx=ssl_grabber("136.243.69.14", 995)
# #xx=xx[1]
# print(xx.decode())