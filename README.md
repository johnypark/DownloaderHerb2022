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
```

There is a shell script for runnning multiple jobs at a time:
ControlDownloadScript.sh

Usage:
```
bash ControlDownloadScript.sh nStart nIncrement nJobs referenceFileName 

```
Where ```nStart``` is row number of the reference file that the script start submitting jobs from, and ```nIncrement``` is the number of rows that single job is handling. ```nJobs``` define number of jobs running at the same time.

You need to modify download PATH and logfile PATH within the shell script to run it as well. 


