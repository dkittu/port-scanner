import banner_grabber
import socket
import csv
import threading
import queue
import time
import link_extractor

print_lock = threading.Lock()

service_list = []

c = open('protocol.csv', 'r')
csv_reader = csv.reader(c, delimiter=' ')
req = (list(csv_reader))
c.close()

server1 = input('Enter the website to be scanned : ')
min = int(input('give starting port : '))
max = int(input('give ending port: '))
print('PORT SCANNING STARTED', end='\n\n')
start = time.time()


def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        ban = banner_grabber.all_grabber(server1, port)
        service_list.append(ban)

        for l in req:
            if port == int(l[1]):

                print(f'{port}....{l[0]}....{ban}')
                break
            else:
                continue



    except:
        pass
    finally:
        s.close()


def scanner_worker():
    while True:
        worker = port_queue.get()
        portscan(worker)
        port_queue.task_done()


port_queue = queue.Queue()

for _ in range(180):
    t = threading.Thread(target=scanner_worker)
    t.daemon = True
    t.start()

for port in range(min, max + 1):
    port_queue.put(port)
port_queue.join()
end = time.time()
total = end - start
print(f'\n\nSCAN COMPLETED IN {total} sec')

service_set=set(service_list)


print('\n\nLINKS TO EXPLOITS:', end='\n\n')
aux_list = []
for l in service_set:
    if l == None or l == '?':
        pass
    else:
        reqq = l.split('\r')[0]
        final = reqq + ' vulnerability'
        aux_list.append(final)

# print(service_set)
# print(aux_list)
for query, original in zip(aux_list, service_list):
    print(original)
    for _ in range(len(original)):
        print('-', end='')
    print('\n')
    link_extractor.link_scrape(query)
    print('\n')
    time.sleep(2)
