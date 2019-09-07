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
	if (connect(sock, (SOCKADDR*)&sockAddr, sizeof(SOCKADDR)) == SOCKET_ERROR)		//��������
	{
		cout << "����������ʧ��" << endl;
	}
	else
	{
		cout << "���������ӳɹ���" << endl;
	}

	int x1 = (img.cols - img.rows) / 2;
	cv::Rect rect = cv::Rect(x1, 0, img.rows, img.rows);
	img = img(rect);
	std::vector<uchar> data_encode;
	std::vector<int> quality;
	quality.push_back(CV_IMWRITE_JPEG_QUALITY);
	quality.push_back(90);//����90%��ѹ��
	imencode(".jpg", img, data_encode, quality);//��ͼ�����
	int nSize = data_encode.size();
	string s1 = "p," + to_string(p) + "," + to_string(nSize) + ",";
	const char* c = s1.c_str();
	for (long int i = 0; i < nSize; i++)
	{
		encodeImg[i] = data_encode[i];
	}
	send(sock, c, 200, 0);
	//����ͼƬ
	long int send_num = 0;
	while (send_num < nSize)
	{
		send(sock, encodeImg + send_num, 2000, 0);
		send_num += 2000;
	}

	send(sock, "end", 100, 0);
	cout << "��һ�η������" << endl;
}


sendsocket::~sendsocket()
{
}




vector<string> sendsocket::split(const string& str, const string& delim) {
	vector<string> res;
	if ("" == str) return res;
	//�Ƚ�Ҫ�и���ַ�����string����ת��Ϊchar*����  
	char * strs = new char[str.length() + 1]; //��Ҫ����  
	strcpy(strs, str.c_str());

	char * d = new char[delim.length() + 1];
	strcpy(d, delim.c_str());

	char *p = strtok(strs, d);
	while (p) {
		string s = p; //�ָ�õ����ַ���ת��Ϊstring����  
		res.push_back(s); //����������  
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
	quality.push_back(90);//����90%��ѹ��
	imencode(".jpg", img, data_encode, quality);//��ͼ�����
	int nSize = data_encode.size();
	string s1 = "p," + to_string(p) + "," + to_string(nSize) + ",";
	const char* c = s1.c_str();
	for (long int i = 0; i < nSize; i++)
	{
		encodeImg[i] = data_encode[i];
	}
	send(sock, c, 200, 0);
	//����ͼƬ
	long int send_num = 0;
	while (send_num < nSize)
	{
		send(sock, encodeImg + send_num, 2000, 0);
		send_num += 2000;
	}

	send(sock, "end", 100, 0);
	//��������
	recv(sock, recv_buf, 400, 0);
	vector<string> img_info = split(recv_buf, ",");
	memset(recv_buf, '\0', sizeof(recv_buf));
	memset(&encodeImg, '\0', sizeof(encodeImg));  //��ʼ���ṹ��
	return img_info;

}
