#(2-5001)
#Next (5002 - 10001)
#Next (10002 - 15001)
#Next (15002 - 20001)
#Next (20002 - 25001)
#Next (25002 - 30001)
#Next (30002 - 35001)


line_start=$1
line_end=$2
fileName=$3
DownFolder=$4
DownLogfileName=$5
wc -l $3

declare -i setParamResize=4000

cat $3 | awk "NR==$line_start, NR==$line_end" | while IFS=$'\t' read -r occurrenceID collectionCode downloadHost scientificName url taxaNumber rest #taxaName taxaNumber uniquefileName 
do
    # $line is a single line of the file, as a single string
    #cd /mnt/g/Harvard_down
    cd $4 #/mnt/g/pnwherbaria_down
    pwd
    echo "$(date). URL: $url, taxa: $scientificName from $collectionCode::" 
    uniq_file_name="${scientificName}__${taxaNumber}__${collectionCode}.jpg"
    echo "${uniq_file_name}"
    curl -LsS ${url} -o "${uniq_file_name}"
    echo "$(date). URL: $url, taxa: $sname from $inst" >> $5
    
    #convert: requires imagemagick
    echo converting image dimension. 
    IFS=" " read -a imdim <<<`identify -format "%w %h" "${uniq_file_name}"`
    #https://linuxhint.com/bash_split_examples/
    #"",'',`` are differnet in Linux Bash. How?
    #echo ${setParamResize}
    #https://stackoverflow.com/questions/16034749/if-elif-else-statement-issues-in-bash
    if [ ${imdim[0]} -gt ${setParamResize} ] || [ ${imdim[1]} -gt ${setParamResize} ] #SPACES_ARE_NEEDED_AROUND_THE_BRACKETS 
    then
        echo "Image is larger than the set size: ${setParamResize}. Image dimension: (${imdim[0]},${imdim[1]})"
        echo "Resizing..."
        echo python resizeImage.py --ImageName "${uniq_file_name}" --outPATH "${DownFolder}"
        python resizeImage.py --ImageName "${uniq_file_name}" --outPATH "${DownFolder}"
        #mogrify -resize "${setParamResize}>" "${uniq_file_name}" 
        # IMagemgaick is super slow when doing resize 100x https://stackoverflow.com/questions/11727860/imagemagick-batch-resizing-performance
        #https://legacy.imagemagick.org/discourse-server/viewtopic.php?t=13175
        echo "Done."
        #">" keeps the aspect ratio. https://stackoverflow.com/questions/5694823/how-do-i-resize-an-image-so-that-the-longest-size-is-shorter-or-equal-to-an-amou
    fi
    #i=i+1
    cd ..
done   
cd 