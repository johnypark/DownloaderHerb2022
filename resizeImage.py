import cv2
import numpy as np
from argparse import ArgumentParser 

def getReSizeFactor(N, image):
    img_x=image.shape[0]
    img_y=image.shape[1]
    if img_x>img_y:
        ratio=N/img_x
        tpl_resize=(int(img_y*ratio),N)
    else:
        ratio=N/img_y
        tpl_resize=(N,int(img_x*ratio))
    return(tpl_resize, (img_x, img_y))


parser = ArgumentParser()
parser.add_argument('--ImageName', help='Name of the Iamge to resize')
parser.add_argument('--ParamResize', default=int(4000), help='Resize parameter. Default:4000')
parser.add_argument('--outPATH', default='/mnt/g/Harvard_down/',help='output PATH')
parser.add_argument('--quality', default=int(98),help='Image quality for resizing.')

args = parser.parse_args()
image = cv2.imread(args.ImageName, cv2.IMREAD_COLOR)
ft_resize, img_shape =getReSizeFactor(args.ParamResize,image)
print(ft_resize,img_shape)
print('image size:{} resizing it to x4000...'.format(img_shape))
image=cv2.resize(image,ft_resize)
print(args.outPATH+args.ImageName)
cv2.imwrite(args.outPATH+args.ImageName, image,[int(cv2.IMWRITE_JPEG_QUALITY), args.quality])