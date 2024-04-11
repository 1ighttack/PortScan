import time
import socket
import threading
import sys

class myThread (threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
    def run(self):
        threadLock.acquire()
        tcp_scan(self.ip, self.port)
        threadLock.release()

def tcp_scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        if s.connect_ex((ip, port)) == 0:
            print("%s:%s open" % (ip, port))
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        else:
            pass
    except Exception as e:
            pass
    finally:
        s.close()


if __name__ == "__main__":
    try:
        ip = sys.argv[1]
        porte = sys.argv[2]
        ports = porte.split("-")
        po1 = ports[0]
        po2 = ports[1]
        threadLock = threading.Lock()
        threads = []
        s_time = time.time()
        for port in range(int(po1), int(po2) + 1):
            thread1 = myThread(ip, port)
            thread1.start()
            threads.append(thread1)
            thread1.join()
        e_time = time.time()
        print("扫描用时", float(round(e_time - s_time, 2)),"秒")
    except Exception as e:
        print("python3 portscan.py 127.0.0.1 1-65532   基于tcp仅限端口扫描，速度取决于网速:)")