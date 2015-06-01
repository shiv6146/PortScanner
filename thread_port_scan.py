import threading
import socket
import sys
from queue import Queue

print_lock=threading.Lock()

target=sys.argv[1]
num_threads=int(sys.argv[2])
strt_port=int(sys.argv[3])
end_port=int(sys.argv[4])

def port_scan(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        con=s.connect((target,port))
        with print_lock:
            print("Port",port,"is open")
        con.close()
    except:
        pass

def threader():
    while True:
        worker=q.get()
        port_scan(worker)
        q.task_done()

q=Queue()

for x in range(num_threads):
    t=threading.Thread(target=threader)
    t.daemon=True
    t.start()

for worker in range(strt_port,end_port):
    q.put(worker)

q.join()
