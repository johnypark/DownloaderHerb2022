#!/bin/python

#CheckDownFolder
#Input argument is downloadHost
#Input argument is df_DownList

#function is to read the folder file, and match df_DownList within downloadHost
#Output is DataFrame object write to designated file format


import os 
import pandas as pd
from argparse import ArgumentParser
import os
import pandas as pd
import numpy as np
import datetime


def getDownloadList(args):
    DOWNPATH=args.dfpath
    PATH=args.refpath
    source_fn=args.refname
    
    print('Searching PATH:{} for already downloaded files.'.format(DOWNPATH))
    ls_PATH=os.listdir(DOWNPATH)
    if args.fnformat=='scientificName_taxaNumber_collectionCode.jpg':
        dldfileNames=[fn for fn in ls_PATH if '.jpg' in fn]
    #print('Retreiving PATH:{} to lookup download list:{}'.format(PATH,source_fn))
    
    #df_reflist=pd.read_table(PATH+source_fn)[['url','downloadHost']]
    #print('Found filename:{}.\n \n \nMatching URLs from files downloaded from {}...'.format(source_fn, DOWNPATH))
    #df_reflist['turl']=[surl.split('/')[-1] for surl in df_reflist.url]
    #df_match=df_dld.merge(df_reflist,how="left",on="turl")
    return(dldfileNames)
    #return(df_match)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--dfpath', default='/mnt/g/',help='download files path')
    parser.add_argument('--refpath',default='/mnt/e/My Drive/Herb22_NewScripts/',help='list path')
    parser.add_argument('--refname', default='herbarium2022-v2_2-limited.tsv',help='reference file name')
    parser.add_argument('--outname', default='UpdateDownList-{}.tsv'.format(datetime.datetime.now().strftime("%Y%m%d-%H%M%S")), help='output list name')
    parser.add_argument('--fnformat', default='scientificName_taxaNumber_collectionCode.jpg', help='format of filename. Options: uniquefileName, lastStringURL.')

    
    args = parser.parse_args()
    print('Called with args:')
    print(args)
    ls_dld=getDownloadList(args)
    #print(df.query('url==url'))
    #df.to_csv(args.refpath+args.outname,sep='\t',index=False)
    #print("Saved to {} in {}".format(args.outname, args.refpath))
    #data_lists=os.listdir(args.savedir)
    DOWNPATH=args.dfpath
    df_h=pd.read_table(args.refpath+args.refname)
    print(df_h.shape)
    #print(ls_dld)
    df_dld=pd.DataFrame([fn.split(sep="__") for fn in ls_dld]).rename(columns={0:'scientificName',1:'taxaNumber',2:'collectionCode'})
    df_dld=df_dld.assign(collectionCode=[name.split(sep=".")[0] for name in df_dld.collectionCode])
    df_dld=df_dld.assign(statusDown=True)
    
    #i=0
    #for number in df_dld.taxaNumber:
    #    try: 
    #        calc=int(number)
    #    except:
    #        print(i)
    #        print(df_dld.iloc[i,:])
    #        print(number)
    #        print(bytes(number,encoding='utf_8'))
    #    i=i+1

    
    df_dld=df_dld.assign(taxaNumber=[int(float(number)) for number in df_dld.taxaNumber])
    print(df_dld)
    df_out=df_h.merge(df_dld,how='left',on=['scientificName','taxaNumber','collectionCode']).query('statusDown!=statusDown')
    print(df_out,args.outname)
    df_out.to_csv(args.outname,sep='\t',index=False)