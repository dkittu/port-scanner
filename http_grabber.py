import socket
import re
import database_check
import codecs
import ssl_wraper


def httpgrabber(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.settimeout(3)
    http_get = "GET / HTTP/1.0\r\n\r\n"

    req = bytes(http_get, 'utf-8')
    data = ''
    flag = 0
    try:
        s.sendall(req)
        data = s.recvfrom(1024)
        data = data[0]
        if len(data)==0:                                 #IF SSL IS ENABLED CALLING SSL WRAPPER
            data=ssl_wraper.ssl_grabber(host,port)


        xx = codecs.decode(data, 'raw_unicode_escape')   #TO CONVERT BYTES TO STR WITH ESCAPE SEQUENCES
        #print(data)
        da = data.decode()

        headers = da.splitlines()
        for da in headers:

            if re.search('Server: ', da, re.IGNORECASE):
                #print(da)
                ans=da
                flag = 1
                break
            else:

                pass
        if flag == 0:
            ans = database_check.db_check(xx)

        else:
            pass

        return ans


    except:

        pass

    finally:
        s.close()

