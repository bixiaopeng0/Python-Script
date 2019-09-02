# -*- coding: UTF-8 -*-
import socket
import os
import sys
import struct
#客户端


def sock_client_image():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 1234))  #   默认是在本机上使用  如有需要修改ip

        except socket.error as msg:
            print(msg)
            print(sys.exit(1))
        # filepath = input('input the file: ')  # 输入当前目录下的图片名 xxx.jpg
        filepath = "cat.jpg"
        if filepath=='exit':
            s.send(b'exit')
            break
        fhead = struct.pack(b'128sq', bytes(os.path.basename(filepath), encoding='utf-8'),
                            os.stat(filepath).st_size)  # 将xxx.jpg以128sq的格式打包
        s.send(fhead)#发送文件名
        print("head",fhead)
        fp = open(filepath, 'rb')  # 打开要传输的图片
        while True:
            data = fp.read(1024)  # 读入图片数据
            if not data:
                print('{0} send over...'.format(filepath))
                break
            s.send(data)  # 以二进制格式发送图片数据
        print(s.recv(1024))
        s.close()
        # break    #循环发送


if __name__ == '__main__':
    sock_client_image()