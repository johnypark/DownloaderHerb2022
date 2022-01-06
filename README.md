# DownloaderHerb2022
Scripts for downloading herbarium specimen images from the source. Additionally the repo includes the script to control parallel download and to resize images to custom resolution using openCV.

### Dataset
```herbarium2022-v2_2_limited.tsv``` has the most recently updated list for downloading images for this project. It consists of 8 columns: occurrenceID	collectionCode	downloadHost	scientificName	url	taxaNumber	uniquefileName	herb21PATH.

```
occurrenceID	collectionCode	downloadHost	scientificName	url	taxaNumber	uniquefileName	herb21PATH
0	cfb9c9be-d01d-4490-9edd-7a0b8411d14c	A	data.huh.harvard.edu	Fraxinus caroliniana Mill.	http://data.huh.harvard.edu/cfb9c9be-d01d-4490...	1	Fraxinus caroliniana Mill.__1__A.jpg	NaN
1	4dab015f-43ff-463f-b889-83372677c13a	A	data.huh.harvard.edu	Fraxinus caroliniana Mill.	http://data.huh.harvard.edu/4dab015f-43ff-463f...	2	Fraxinus caroliniana Mill.__1__A.jpg	NaN
2	5e4801ce-307b-4637-8668-06c5e1fc008d	A	data.huh.harvard.edu	Fraxinus caroliniana Mill.	http://data.huh.harvard.edu/5e4801ce-307b-4637...	3	Fraxinus caroliniana Mill.__1__A.jpg	NaN
3	c37e7862-d314-46d6-aa11-8578474249b3	A	data.huh.harvard.edu	Fraxinus caroliniana Mill.	http://data.huh.harvard.edu/c37e7862-d314-46d6...	4	Fraxinus caroliniana Mill.__1__A.jpg	NaN
4	26cb0ddc-975a-4504-8e7d-e704553e22c6	A	data.huh.harvard.edu	Fraxinus caroliniana Mill.	http://data.huh.harvard.edu/26cb0ddc-975a-4504...	5	Fraxinus caroliniana Mill.__1__A.jpg	NaN
...	...	...	...	...	...	...	...	...
1240844	urn:catalog:cas:bot-bc:2240	CAS	researcharchive.calacademy.org	Cuscuta suaveolens Ser.	http://researcharchive.calacademy.org/image_db...	100	Fraxinus caroliniana Mill.__1__A.jpg	NaN
1240845	urn:catalog:cas:bot-bc:33119	CAS	researcharchive.calacademy.org	Cryptantha hooveri I.M.Johnst.	http://researcharchive.calacademy.org/image_db...	10	Fraxinus caroliniana Mill.__1__A.jpg	NaN
1240846	urn:catalog:cas:bot-bc:26729	CAS	researcharchive.calacademy.org	Downingia bella Hoover	http://researcharchive.calacademy.org/image_db...	35	Fraxinus caroliniana Mill.__1__A.jpg	NaN
1240847	urn:catalog:cas:bot-bc:33307	CAS	researcharchive.calacademy.org	Downingia bella Hoover	http://researcharchive.calacademy.org/image_db...	36	Fraxinus caroliniana Mill.__1__A.jpg	NaN
1240848	urn:catalog:cas:bot-bc:123463	CAS	researcharchive.calacademy.org	Hypericum adpressum W.P.C.Barton	http://researcharchive.calacademy.org/image_db...	100	Fraxinus caroliniana Mill.__1__A.jpg	NaN
```


Update 1/5/22:

Download hosts completed download: ```n2t.net```, ```data.huh.harvard.edu```
```www.pnwherbaria.org```, ```api.idigbio.org```, ```cdn.plantatlas.org```,```botanydb.colorado.edu``` , ```arctos.database.museum ```,      
Download left for each download host:

```
sweetgum.nybg.org                     35000
mediaphoto.mnhn.fr                   159136
fm-digital-assets.fieldmuseum.org     36371
www.tropicos.org                      31409
swbiodiversity.org                    25999
prc-symbiota.tacc.utexas.edu          25957
www.kew.org                           17909
researcharchive.calacademy.org         3252
```

This repository contain two seperate codes to download and resize files from both bash shell and Python. They are:
DownloadScript_nStart_nEnd_RefName_dPATH_PATHLogfn.sh
Download_and_resize.py

Basic usage of the downloder is that you take a reference table, and refer URLs from the reference table to download files. For example:
```
bash DownloadScript_nStart_nEnd_RefName_dPATH_PATHLogfn.sh 2 10000 h22-limited.tsv /mnt/h22/down/ /mnt/h22/logs/
```
Would search URL from h22-limited.tsv and download 2nd to 10000th files to /mnt/h22/down/, leaving the log file to /mnt/h22/logs.

Python file works similarly. For more detail, use --help option to see all the arguments:
```
python Download_and_resize.py -h
usage: Download_and_resize.py [-h] [--start START] [--end END] [--outPATH OUTPATH] [--Nscript NSCRIPT] [--readfn READFN] [--log LOG]

optional arguments:
  -h, --help         show this help message and exit
  --start START      starting row
  --end END          ending row
  --outPATH OUTPATH  output PATH
  --Nscript NSCRIPT  number of script
  --readfn READFN    filename of read
  --log LOG          filename of read
```

There is a shell script for runnning multiple jobs at a time:
ControlDownloadScript.sh

Usage:
```
bash ControlDownloadScript.sh nStart nIncrement nJobs referenceFileName 
```
Where ```nStart``` is row number of the reference file that the script start submitting jobs from, and ```nIncrement``` is the number of rows that single job is handling. ```nJobs``` define number of jobs running at the same time.
You need to modify download PATH and logfile PATH within the shell script to run it as well. 

dlHosts.txt include list of all the download host we plan to get the data from.
```
sweetgum.nybg.org                    356950
n2t.net                              178853
mediaphoto.mnhn.fr                   159136
data.huh.harvard.edu                 138666
www.pnwherbaria.org                   74834
api.idigbio.org                       54636
cdn.plantatlas.org                    53943
botanydb.colorado.edu                 43535
arctos.database.museum                39399
fm-digital-assets.fieldmuseum.org     36371
www.tropicos.org                      31409
swbiodiversity.org                    25999
prc-symbiota.tacc.utexas.edu          25957
www.kew.org                           17909
researcharchive.calacademy.org         3252
```

CheckDownFolder.py lists all the filenames downloaded in the target folder and matches the reference table, outputs the list that have not yet downloaded. 
```
python CheckDownFolder.py -h
usage: CheckDownFolder.py [-h] [--dfpath DFPATH] [--refpath REFPATH] [--refname REFNAME] [--outname OUTNAME] [--fnformat FNFORMAT]

optional arguments:
  -h, --help           show this help message and exit
  --dfpath DFPATH      download files path
  --refpath REFPATH    list path
  --refname REFNAME    reference file name
  --outname OUTNAME    output list name
  --fnformat FNFORMAT  format of filename. Options: uniquefileName, lastStringURL.
  ```
  
  
 ## Data table meta data
 
 
 ## Data table explanation



