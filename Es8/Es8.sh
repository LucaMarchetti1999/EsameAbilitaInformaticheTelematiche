#!/bin/bash

if [ -z "$1" ]; then		#checks if directory name is given
  echo "Error: No directory name was given."
  exit 1		#error exit status
fi

DIR_NAME="$1"
DIR_PATH=$(find /home /usr /var -type d -name "$DIR_NAME" 2>/dev/null -print -quit)		#permission errors are eliminated and restricts searches only to certain directories

if [ -z "$DIR_PATH" ]; then		#check if desired directory was found
  echo "Error: Directory '$DIR_NAME' not found."
  exit 1		#error exit status
fi

find "$DIR_PATH" -maxdepth 1 -type f		#list all files in the directory
exit 0		#good run exit status
