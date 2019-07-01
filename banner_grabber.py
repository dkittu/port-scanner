import socket
import http_grabber
import database_check


def non_http(ip, port):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1096)
        #print(banner)
        return banner.decode()
    except:
        return False
    finally:
        s.close()


def all_grabber(ip, port):

    banner1 = non_http(ip, port)
    if banner1 :
        if len(banner1) < 80:  # DURING HTTP BANNER IS NONETYPE
            return (banner1)
        else:
           ans= database_check.db_check(banner1)
           return (ans)# use file handling
    else:
        x = http_grabber.httpgrabber(ip, port)
        return (x)



