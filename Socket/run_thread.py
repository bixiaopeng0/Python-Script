
def dealSocketMessage():
    global image,pxiel,sock,recv_flag,send_flag,lock

    # while True:
    #     cv2.waitKey(100)
    #     print("test socket")
    cnt = 0
    while True:
        # print("recv_flag",recv_flag)
        if recv_flag:
            start_time_s = time.time()
            start_time = time.time()
            data = sock.recv(200)
            print("time1",time.time()-start_time)
            string = data.decode('utf-8', 'ignore').split(',')
            if string[0] == 'p':
                pxiel = int(string[1])
            img_bytes = bytes()
            start_time = time.time()
            while True:
                start_time1= time.time()
                data = sock.recv(2000)
                print("recve img time",time.time()-start_time1)
                string = data.decode('utf-8', 'ignore').split('\x00')[0]
                if string == "end":
                    # print("接受成功")
                    lock.acquire()
                    img = np.asarray(bytearray(img_bytes), dtype="uint8")
                    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
                    image = copy.deepcopy(img)
                    lock.release()
                    break
                img_bytes = img_bytes + data
            print("time2", time.time() - start_time)
            str = ",".join(str_list) + ","
            # 发送识别到的数据
            sock.send(str.encode())
            lock.acquire()
            recv_flag = False
            lock.release()
            cnt+=1
            if cnt==101:
                cv2.waitKey()
            print("recv time ",(time.time()-start_time_s))
        else:
            cv2.waitKey(1)


def run():
    #先接受一次信息
    global sock,image,pxiel
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 1234))
    # s.bind(('服务器的ip', 6666))
    s.listen(10)
    sock, addr = s.accept()
    data = sock.recv(200)
    string = data.decode('utf-8', 'ignore').split(',')
    if string[0] == 'p':
        pxiel = int(string[1])
    img_bytes = bytes()
    while True:
        data = sock.recv(2000)
        string = data.decode('utf-8', 'ignore').split('\x00')[0]
        if string == "end":
            image = np.asarray(bytearray(img_bytes), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            print("第一次获取success!")
            break
        img_bytes = img_bytes + data


    t1 = threading.Thread(target=dealSocketMessage, args=())
    t2 = threading.Thread(target=dealDeepNetMessage, args=())
    t1.start()
    # dealDeepNetMessage()
    t2.start()
    t1.join()
    t2.join()
    sock.close()
    print("over")

if __name__ == '__main__':
    run()