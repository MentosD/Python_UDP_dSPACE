import socket
import sys
import datetime
import struct
import time
import math
import numpy as np
import scipy.io as sio
BUFSIZE = 64
ip_serverport = ('192.168.140.102', 49104)
ip_portclient = ('192.168.140.20', 49500)
# ip_portclient = ('192.168.140.102', 49001)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dt = 0.020
dtt = int(dt / 0.001)     #改变步长 间隔取值
ACC = sio.loadmat('ACC_kobe.mat')
Acc = np.asarray(np.float32(ACC['ACC_kobe']))
n = int(len(Acc)/dtt)
# time.sleep(20)
print('计时开始')
time_start = time.time()
server.bind(ip_serverport)
for i in range(1, n) :
    data, client_addr = server.recvfrom(BUFSIZE)
    data_decode = struct.unpack("!d""d""d""d""d""d", data)

    time.sleep(1)
    print(data_decode)
    # a = Acc[int(i*dtt) , 1]
    a = (float(i),float(1))
    msg = struct.pack("!d""d", a[0], a[1])
    client.sendto(msg, ip_portclient)
time_end = time.time()
print('计算结束,用时',time_end-time_start,'秒','平均每步用时',(time_end-time_start) / n,'秒')
