
#from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np
import os
import sys
import time
from argparse import ArgumentParser
import random
import logging
import cv2        





def getReSizeFactor(fftr, image):
    img_x=image.shape[0]
    img_y=image.shape[1]
    if img_x>img_y:
        ratio=fftr/img_x
        tpl_resize=(int(img_y*ratio),fftr)

    else:
        ratio=fftr/img_y
        tpl_resize=(fftr,int(img_x*ratio))
    return(tpl_resize, (img_x, img_y))

def url_to_jpg(DataFrame,file_path=None,timeout_param=60,resize_max=4000,image_quality=98):
    import os
    if file_path is None:
        file_path=os.getcwd()
    dURL=DataFrame[cn_url].values[0]
    filename=DataFrame[cn_fname].values[0] #https://stackoverflow.com/questions/14270698/get-file-size-using-python-requests-while-only-getting-the-heade
    #Check if filename has .jpg extension, if not, add '.jpg' to the name. 
    resp = requests.get(dURL, stream=True).raw
    #if len(resp.read())< 400000:
    #    return('size_error')
    
        #resp=response.raw
        #resp = requests.get(dURL, stream=True)
        #Load image and resize to 5500, output with quality 98
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    ft_resize, img_shape =getReSizeFactor(resize_max,image)
        
    if max(img_shape)>resize_max:
        print('image size:{} resizing it to x4000...'.format(img_shape))
        image=cv2.resize(image,ft_resize)
        print(filename)
    cv2.imwrite(file_path+filename, image,[int(cv2.IMWRITE_JPEG_QUALITY), image_quality])
    #return('complete')
    
    #with open(file_path+filename, "wb") as file:
    #    file.write(resp.content)
    #print('saved to:{}\n'.format(filename,file_path))
    resp.close()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--start', help='starting row')
    parser.add_argument('--end', help='ending row')
    parser.add_argument('--outPATH', default='/mnt/g/pnwherbaria_down/',help='output PATH')
    parser.add_argument('--Nscript', default=int(1), help='number of script')
    parser.add_argument('--readfn',default='h22-v2_1-limited-pnwherbaria-DownList_Jan4th2022.tsv',help='filename of read')
    parser.add_argument('--log',default='pnw-download-log.txt',help='filename of read')
    cn_url=['url']
    cn_fname=['uniquefileName']
    cn_TxNm=['scientificName']
    cn_Nmbr=['taxaNumber']
    cn_inst=['collectionCode']
    args = parser.parse_args()
    print('Called with args:')
    print(args)

    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=args.log,
                    filemode='a')

    print('{}th python script is running: Starting from {} upto {}'.format(args.Nscript, args.start, args.end))
    time_start=time.time()
    Nstart=int(args.start)
    Nend=int(args.end)
    df_curr=pd.read_csv(args.readfn,sep="\t")
    df_curr=df_curr.iloc[(Nstart-1):(Nend)]
    nROW=df_curr.shape[0]
    count=0
    for i in range(nROW):
        count=count+1
        df_row=df_curr.iloc[i]
        print(str(df_row[cn_url].values[0]))
        try:
            url_to_jpg(df_row,file_path=args.outPATH)
            #print(res)
            #if res=='size_error':
            #    print('size error: too small.')
            #    logging.error('size too small!')
            #    continue  
            logging.info('Downloading URL:{} to filename {} complete.'.format(df_row[cn_url].values[0], args.outPATH+df_row[cn_fname].values[0]))

        except:
            print('Something went wrong. Waiting for 60+ seconds and retry...')
            logging.error('URL:{}. Waiting for 60+ seconds and retry...'.format(df_row[cn_url].values[0]))
            time.sleep(int(random.random()*20+60))
        #https://stackoverflow.com/questions/55872164/how-to-rotate-proxies-on-a-python-requests/68451842#68451842
            for j in range(2): 
                try:
                    url_to_jpg(df_row,file_path=args.outPATH)
                    logging.info('Downloading URL:{} to filename {} complete.'.format(df_row[cn_url].values[0], args.outPATH+df_row[cn_fname].values[0]))
                    break
                except:
                    print('Trying another 30 seconds to wait...')
                    logging.error('URL:{}. Waiting for 30+ seconds and retry...'.format(df_row[cn_url].values[0]))
                    time.sleep(int(random.random()*10+30))
        print('{}/{} complete.............................'.format((i+1),nROW))
        time_now=time.time()
        if (count)%100==0:
            time_passed=time_now-time_start
            print('Total time passed after running the script:{} minutes'.format(time_passed/60))
            print('efficiency:{}check/per1hour'.format((i+1)/time_passed*3600))





