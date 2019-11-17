#-*-coding:utf-8-*-
import torch
from torchvision import transforms
from PIL import Image
import cv2

img_path = "./rooster.jpg"


mean,std = (0.485, 0.456, 0.406), (0.229, 0.224, 0.225)
transform1 = transforms.Compose([
	transforms.CenterCrop((224,224)), # 只能对PIL图片进行裁剪
	transforms.ToTensor(),
	transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
	]
)


transform2 = transforms.Compose([
	# transforms.CenterCrop((224,224)), # 只能对PIL图片进行裁剪
	# transforms.ToTensor(),
	transforms.ToPILImage(),
	# transforms.Normalize((.5, .5, .5), (.5, .5, .5))
	]
)

transform3 = transforms.Compose([
	# transforms.CenterCrop((224,224)), # 只能对PIL图片进行裁剪
	transforms.ToTensor(),
	# transforms.ToPILImage(),
	# transforms.Normalize((.5, .5, .5), (.5, .5, .5))
	]
)


## PIL图片与Tensor互转
img_PIL = Image.open(img_path)
img_PIL_Tensor = transform1(img_PIL)

#逆归一化
for i,j in enumerate(img_PIL_Tensor):
	img_PIL_Tensor[i] = (j+mean[i]/std[i])*std[i]


#Tensor转成PIL.Image重新显示
new_img_PIL = transform2(img_PIL_Tensor).convert('RGB')
new_img_PIL.show() # 处理后的PIL图片


