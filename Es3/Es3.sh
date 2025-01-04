#!/bin/bash

LineCount () {
	local dir="${1:-.}"			#sets the directory to current dir with local variable
	ls -p "$dir" | grep -v '/$' | wc -l	#appends / to directory names, exclude lines containing / and finally count the remaining lines 
}

echo "There are $(LineCount) files in the current directory"	#prints the current number of files excluding directories
