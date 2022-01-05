#!/bin/bash

#python test.py
start=$1 #$(($1+1))
increment=$2
Numjobs=$(($3-1))
ReffileName=$4
dPATH=/mnt/g/Herbarium22_Downloads/api.idigbio.org/
PATHLogfn=/mnt/e/My\ Drive/Herb22_NewScripts/log_idigbio.txt
echo "${dPATH}" "${PATHlogfn}"

for j in $(seq $start $increment $(($start+$increment*$Numjobs)))
do
    echo $j $(($j+$increment-1)) $Numjobs
    bash DownloadScript_nStart_nEnd_RefName_dPATH_PATHLogfn.sh $j $(($j+$increment-1)) "${4}" "${dPATH}" "${PATHlogfn}" & 
    #python Download_and_resize --start $j --end $(($j+$increment-1)) --outPATH /mnt/g/Harvard_down/ --readfn harvard_downloadleft.tsv &
    n=$(($n+1))
    done
