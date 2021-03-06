#!/usr/bin/env python3

import socket
import time

address = 'xxx.xxx.xxx.xxx';

#即使主机一个端口也没开放，仍会生成被扫描主机的结果文件
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
    start_time = time.time();
    for i in range(1, 65536):
        ip = address;
        port = i;
        connect_try(ip, port);
    stop_time = time.time();
    used_time = start_time - stop_time;
    print("共耗时" + used_time + "秒");

if __name__ == "__main__":
    main();
