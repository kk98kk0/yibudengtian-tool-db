#!/usr/bin/env python3

import socket

address = 'xxx.xxx.xxx.xxx';
f = open(address + ".txt", "w");
f.close();

def connect_try(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        s.settimeout(1.1);  #经测试，默认的超时时间大概二十一二秒，等待时间太长了，一般连接成功也就1秒以内，改为1.1秒基本可判定是否能成功连接
        s.connect( (ip, port) );
        print("[*] " + ip + " %d/tcp open" % port);
        with open(address + ".txt", "a") as f:
            f.write(ip + ":" + str(port) + "\n");
    except:
        print("[*] " + ip + " %d/tcp closed" % port);

def main():
    for i in range(1, 65536):
        ip = address;
        port = i;
        connect_try(ip, port);

if __name__ == "__main__":
    main();
