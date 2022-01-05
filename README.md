# DownloaderHerb2022
Scripts for downloading herbarium specimen images from the source. Additionally the repo includes the script to control parallel download and to resize images to custom resolution using openCV.

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



