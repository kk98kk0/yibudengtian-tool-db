#!/usr/bin/env python3

import socket

def connect_try(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        s.settimeout(1.1);  #经测试，默认的超时时间大概二十一二秒，等待时间太长了，一般连接成功也就1秒以内，改为1.1秒基本可判定是否能成功连接
        s.connect( (ip, port) );
        print("[*] " + ip + " %d/tcp open" % port);
        with open("results.txt", "a") as f:
            f.write(ip + ":" + str(port) + "\n");
    except:
        print("[*] " + ip + " %d/tcp closed" % port);

def main():
    port = 80;
    for i in range(0, 256):
        ip = '192.168.1.' + str(i);
        connect_try(ip, port);

if __name__ == "__main__":
    main();
