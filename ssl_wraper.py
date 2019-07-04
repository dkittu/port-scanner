#SSL WRAPPER FOR HTTP GRABBER
import socket
import ssl

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

