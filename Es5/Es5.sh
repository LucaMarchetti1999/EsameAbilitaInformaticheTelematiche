#!/bin/bash

filename='Gauss.txt'
touch $filename

for e in *; do		#loops for all files and directories inside current dir
	if [ "$(basename "$e")" = "$filename" ]; then	#find the file named Gauss.txt
		sed -i '1,11d' "$filename"		#if file exists removes the first 11 lines to prevent overwriting
	fi 
done

for k in {1..10}; do		
	echo "$k" | tee -a "$filename"		#echos from 1 to 10 and sends the output to Gauss.txt
done

sum=$(awk '{s+=$1} END {print s}' "$filename" | xargs)		#saves awk sum output inside sum variable
echo "Debug: Sum is '$sum'"		#prints the result of sum

if [ "$sum" -eq 55 ]; then		#checks if result is correct
	echo "Result is correct"
	exit 0
else
	echo "Incorrect result"
	exit 1
fi
