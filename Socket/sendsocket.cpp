#include "sendsocket.h"



sendsocket::sendsocket()
{
}

void sendsocket::initSocket(cv::Mat img, int p)
{
	WSAStartup(MAKEWORD(2, 2), &wsaData);
	memset(&sockAddr, 0, sizeof(sockAddr));				 
	sockAddr.sin_family = PF_INET;
	sockAddr.sin_port = htons(1234);
	sockAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
	if (connect(sock, (SOCKADDR*)&sockAddr, sizeof(SOCKADDR)) == SOCKET_ERROR)		//建立链接
	{
		cout << "服务器连接失败" << endl;
	}
	else
	{
		cout << "服务器连接成功！" << endl;
	}

	int x1 = (img.cols - img.rows) / 2;
	cv::Rect rect = cv::Rect(x1, 0, img.rows, img.rows);
	img = img(rect);
	std::vector<uchar> data_encode;
	std::vector<int> quality;
	quality.push_back(CV_IMWRITE_JPEG_QUALITY);
	quality.push_back(90);//进行90%的压缩
	imencode(".jpg", img, data_encode, quality);//将图像编码
	int nSize = data_encode.size();
	string s1 = "p," + to_string(p) + "," + to_string(nSize) + ",";
	const char* c = s1.c_str();
	for (long int i = 0; i < nSize; i++)
	{
		encodeImg[i] = data_encode[i];
	}
	send(sock, c, 200, 0);
	//发送图片
	long int send_num = 0;
	while (send_num < nSize)
	{
		send(sock, encodeImg + send_num, 2000, 0);
		send_num += 2000;
	}

	send(sock, "end", 100, 0);
	cout << "第一次发送完成" << endl;
}


sendsocket::~sendsocket()
{
}




vector<string> sendsocket::split(const string& str, const string& delim) {
	vector<string> res;
	if ("" == str) return res;
	//先将要切割的字符串从string类型转换为char*类型  
	char * strs = new char[str.length() + 1]; //不要忘了  
	strcpy(strs, str.c_str());

	char * d = new char[delim.length() + 1];
	strcpy(d, delim.c_str());

	char *p = strtok(strs, d);
	while (p) {
		string s = p; //分割得到的字符串转换为string类型  
		res.push_back(s); //存入结果数组  
		p = strtok(NULL, d);
	}

	return res;
}

vector<string> sendsocket::getSocketInfo(cv::Mat img, int p)
{
	int x1 = (img.cols - img.rows) / 2;
	cv::Rect rect = cv::Rect(x1, 0, img.rows, img.rows);
	img = img(rect);
	std::vector<uchar> data_encode;
	std::vector<int> quality;
	quality.push_back(CV_IMWRITE_JPEG_QUALITY);
	quality.push_back(90);//进行90%的压缩
	imencode(".jpg", img, data_encode, quality);//将图像编码
	int nSize = data_encode.size();
	string s1 = "p," + to_string(p) + "," + to_string(nSize) + ",";
	const char* c = s1.c_str();
	for (long int i = 0; i < nSize; i++)
	{
		encodeImg[i] = data_encode[i];
	}
	send(sock, c, 200, 0);
	//发送图片
	long int send_num = 0;
	while (send_num < nSize)
	{
		send(sock, encodeImg + send_num, 2000, 0);
		send_num += 2000;
	}

	send(sock, "end", 100, 0);
	//接受数据
	recv(sock, recv_buf, 400, 0);
	vector<string> img_info = split(recv_buf, ",");
	memset(recv_buf, '\0', sizeof(recv_buf));
	memset(&encodeImg, '\0', sizeof(encodeImg));  //初始化结构体
	return img_info;

}
