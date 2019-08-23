// color_recog_dll.cpp : 定义 DLL 应用程序的导出函数。
//

#include "stdafx.h"
#include "color_recog_dll.h"




// 这是导出函数的一个示例。
COLOR_RECOG_DLL_API int fncolor_recog_dll(int a)
{
    return a;
}



COLOR_RECOG_DLL_API int recog_color(uchar* frame_data,int img_height,int img_width, int x, int y, int w, int hi)
{
	clock_t start_time, end_time;
	start_time = clock();

	//转换数据
	int count = 0;
	Mat hsv_img(img_height, img_width, CV_8UC3);
	uchar* pxvec = hsv_img.ptr<uchar>(0);

	for (int row = 0; row < img_height; row++)
	{
		pxvec = hsv_img.ptr<uchar>(row);
		for (int col = 0; col < img_width; col++)
		{
			for (int c = 0; c < 3; c++)
			{
				pxvec[col * 3 + c] = frame_data[count];
				count++;
			}
		}
	}



	int h, s, v;
	int color_data[10] = { 0 };
	for (int i = y + hi / 2; i < y + hi; i++)
	{
		for (int j = x; j < x + w; j++)
		{
			h = hsv_img.at<Vec3b>(i, j)[0];
			s = hsv_img.at<Vec3b>(i, j)[1];
			v = hsv_img.at<Vec3b>(i, j)[2];
			hsv_img.at<Vec3b>(i, j)[0] = 255;
			hsv_img.at<Vec3b>(i, j)[1] = 255;
			hsv_img.at<Vec3b>(i, j)[2] = 255;
			//	cout<<"H" << h << " " << s << " " << v << " ";
			if (h >= 0 && h <= 180 && s >= 0 && s <= 255 && v >= 0 && v <= 46)
			{
				color_data[0]++;
			}
			else if (h >= 0 && h <= 180 && s >= 0 && s <= 43 && v >= 46 && v <= 220)
			{
				color_data[1]++;
			}
			else if (h >= 0 && h <= 180 && s >= 0 && s <= 30 && v >= 221 && v <= 255)
			{
				color_data[2]++;
			}
			else if (h >= 0 && h <= 10 && s >= 43 && s <= 255 && v >= 46 && v <= 255)
			{
				color_data[3]++;
			}
			else if (h >= 156 && h <= 180 && s >= 43 && s <= 255 && v >= 46 && v <= 255)
			{
				color_data[3]++;
			}
			else if (h >= 11 && h <= 25 && s >= 43 && s <= 255 && v >= 46 && v <= 255)
			{
				color_data[4]++;
			}
			else if (h >= 26 && h <= 34 && s >= 43 && s <= 255 && v >= 46 && v <= 255)
			{
				color_data[5]++;
			}
			else if (h >= 35 && h <= 77 && s >= 43 && s <= 255 && v >= 46 && v <= 255)
			{
				color_data[6]++;
			}
			else if (h >= 78 && h <= 99 && s >= 43 && s <= 255 && v >= 46 && v <= 255)
			{
				color_data[7]++;
			}
			else if (h >= 100 && h <= 124 && s >= 43 && s <= 255 && v >= 46 && v <= 255)
			{
				color_data[8]++;
			}
			else if (h >= 125 && h <= 155 && s >= 43 && s <= 255 && v >= 46 && v <= 255)
			{
				color_data[9]++;
			}
		}
		//cout << endl;
	}
	end_time = clock();
	int max_id = 0;
	int max_data = color_data[0];
	for (int i = 0; i < 10; i++)
	{
		if (color_data[i] > max_data)
		{
			max_id = i;
			max_data = color_data[i];
		}
		//cout << i << ":" << color_data[i] << endl;
	}
	//cout << "运行时间:" << (double)(end_time - start_time) / CLOCKS_PER_SEC << endl;
	return max_id;
}

