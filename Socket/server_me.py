import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 1234))
# s.bind(('服务器的ip', 6666))
s.listen(10)
sock, addr = s.accept()
cnt = 0
# while True:
#     cnt+=1
#     print(cnt)
#     data = sock.recv(1024)
#     print(data)
#     sock.send(data)
# s.close()


def deal_image(sock):
    # print("Accept connection from {0}".format(addr))  # 查看发送端的ip和端口
    cnt = 0
    new_filename = "cat1.jpg"
    fp = open(new_filename, 'wb')
    data = sock.recv(2000)
    start_time = time.time()
    while True:
            # sock.send(cnt)

        print(cnt)
        cnt+=1
        # print(len(data))
        # print(data[0:4])
        string = data.decode('utf-8','ignore').split('\x00')
        # print(type(data),type(string))
        print(string[0])

        if string[0]=='exit':
            print("over")
            break

        fp.write(data)  # 写入图片数据
        data = sock.recv(2000)
            # s= dete_img.test_img(img_path).cpu().numpy()[0]
            # sock.send(str(key_value[s]).encode('utf-8'))      #.decode('utf-8')).encode('utf-8')
            #print(s)
    end_time = time.time()
    print(end_time-start_time)
    fp.close()
    sock.close()


deal_image(sock)
