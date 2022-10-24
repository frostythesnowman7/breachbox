#!/bin/bash
#Written by Miles Golding 2022

if [ $# -ne 2 ]
then
	echo 'Usage: This script will parse zipped files for a company name'
	echo 'qnd-parse.sh [zips dir] [company]'
else

## Setting up variables
OUTFILE=$(echo ./$2.out | tr ' ' '-')
#total_Files=$(find "$1" -type f -not -path '*/\.gz' | wc -l)
total_Files=$(ls $1/*.gz | wc -l)
file_Count=0

function ProgressBar() {

        let _progress=$(((file_Count * 100 / total_Files * 100) / 100))
        let _done=$(((_progress * 4) / 10))
        let _left=$((40 - _done))

        _fill=$(printf "%${_done}s")
        _empty=$(printf "%${_left}s")

        printf "\rProgress : [${_fill// /\#}${_empty// /-}] ${_progress}%%"

    }



	for FILE in $1/*.gz
	do
		#echo "DEBUG: File is $FILE"
		FID=temp$RANDOM
		#echo "Begining on $FILE"
		#read -p "Press any button to continue..."
		gunzip -c $FILE > $FID
		#echo DEBUG: grep -i "$2" $FID >> $OUTFILE
		grep -ia "$2" $FID >> $OUTFILE
		rm ./$FID
		((++file_Count))
		ProgressBar ${number} ${total_Files}
	done
	
	echo
	echo "Matches placed in $OUTFILE"
fi


