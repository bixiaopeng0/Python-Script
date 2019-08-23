// ���� ifdef ���Ǵ���ʹ�� DLL �������򵥵�
// ��ı�׼�������� DLL �е������ļ��������������϶���� COLOR_RECOG_DLL_EXPORTS
// ���ű���ġ���ʹ�ô� DLL ��
// �κ�������Ŀ�ϲ�Ӧ����˷��š�������Դ�ļ��а������ļ����κ�������Ŀ���Ὣ
// COLOR_RECOG_DLL_API ������Ϊ�Ǵ� DLL ����ģ����� DLL ���ô˺궨���
// ������Ϊ�Ǳ������ġ�
#ifdef COLOR_RECOG_DLL_EXPORTS
#define COLOR_RECOG_DLL_API  extern "C" __declspec(dllexport)
#else
#define COLOR_RECOG_DLL_API  extern "C" __declspec(dllimport)
#endif
#include <opencv2/opencv.hpp>
using namespace cv;


COLOR_RECOG_DLL_API int fncolor_recog_dll(int a);

COLOR_RECOG_DLL_API int recog_color(uchar* frame_data, int img_height,int img_width, int x, int y, int w, int hi);