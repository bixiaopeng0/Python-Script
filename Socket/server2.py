# -*- coding: UTF-8 -*-
import socket
import os
import sys
import struct
# from test import dete_img
# from class_convert import key_value
#服务器端





def socket_service_image():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 1234))
        #s.bind(('服务器的ip', 6666))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    print("Wait for Connection.....................")
    flagout=[1]
    while flagout[0]:
        sock, addr = s.accept()  # addr是一个元组(ip,port)
        deal_image(sock, addr,flagout)



def deal_image(sock, addr,flagout):
    # print("Accept connection from {0}".format(addr))  # 查看发送端的ip和端口

    cnt = 0
    while True:

        if cnt == 100:
            cnt = 0
        cnt+=1

        fileinfo_size = struct.calcsize('128sq')

        buf = sock.recv(fileinfo_size)  # 接收图片名
        if buf==b'exit':
            flagout[0]=0
            break


        if buf:
            filename, filesize = struct.unpack('128sq', buf)
            fn = filename.decode().strip('\x00')
            new_filename = os.path.join('./',
                                        'new_' + fn)  # 在服务器端新建图片名（可以不用新建的，直接用原来的也行，只要客户端和服务器不是同一个系统或接收到的图片和原图片不在一个文件夹下）

            recvd_size = 0
            fp = open(new_filename, 'wb')
            # sock.send(cnt)
            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = sock.recv(1024)
                    recvd_size += len(data)
                else:
                    data = sock.recv(1024)
                    recvd_size = filesize
                fp.write(data)  # 写入图片数据
            fp.close()
            img_path = new_filename
            print(img_path)
            # s= dete_img.test_img(img_path).cpu().numpy()[0]
            # sock.send(str(key_value[s]).encode('utf-8'))      #.decode('utf-8')).encode('utf-8')
            #print(s)
            flagout[0]=1

        sock.close()

        break






if __name__ == '__main__':
    socket_service_image()



