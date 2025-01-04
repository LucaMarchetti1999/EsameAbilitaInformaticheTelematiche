#!/bin/bash

a=("dog.jpg" "cat.jpg" "vacation.jpg" "wallpaper.png" "shuf_manual.pdf") #random files to be added

for e in "${a[@]}"; do	#loops through elements of the array
	touch "$e"	#creates files in working dir with names equal to array elements
done


e_array=( $(ls -A) )	#stores results of ls -A in e_array

if [ ${#e_array[@]} -eq 0 ]; then	#check if e_array is empty or not
	echo "List is empty"
else
	echo "Elements inside the list are"
	for e in "${e_array[@]}"; do
		echo "$e"	#prints each element of the array
	done
fi

day=$(date +'%Y-%m-%d')		#Date stored in day variable
bash_name=$(basename "$BASH")	#These two lines are used inside the if contition to skip directories and prevent the bash script renaming itself
script_name=$(basename "$0")

for e in *; do
	if [ -d "$e" ] || [ "$(basename "$e")" = "$bash_name" ] || [ "$(basename "$e")" = "$script_name" ]; then	#if conditions to skip bash executable and directories
		continue
	fi
	
	mv "$e" "${day}-${e}"	#renaming of directory files
done

echo " "
echo "New file names are: "
ls -A

