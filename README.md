# EsameAbilitaInformaticheTelematiche
This is the repository for the 2024-2025 exam for "Abilità informatiche e telematiche" course

The exercises chosen were Ex1, Ex3, Ex5, Ex8 and the python Ex9.

Exercise 1: Creates 5 different files in the current directory with predetermined names and extensions stored in a array. Reading the contents of the directory it stores it in a different array later used to print in the standard output its contents.
Lastly checks current date and adds it to the names of the files in the directory. A safeguard is added to prevent the script from renaming itself but DOES NOT prevent other .sh files from being renamed. 
A dedicated folder for this script usage is recommended.

Exercise 3: Simple script containing the LineCount function. Saves current directory in a local variable, then using a one liner appends "/" to directory names, excludes them from the count and finally counts the remaining lines.  
Finally prints in the standard output the number of files.

Exercise 5: Creates an empty file named Gauss.txt with touch command, if the files already exists the sed command is used to remove the first 11 lines of the file to prevent multiple appends. 
it then loops from 1-10 and appends the cycle number in the Gauss.txt file using the echo and tee command. Lastly the awk command is used to sum through the 10 lines in the file and prints the result in the standard output. The result is checked with a if statement and a exist status is given.

Exercise 8: Script that finds all files inside a directory that was given as an argument. If no argument is given or if the directory does not exists, exits the program with an error message. Otherwise use the find command to list all files in the directory and exits with 0 exit value.
It should be noted that directories without permission are not considered and the search is limited only to certain directories as stated in DIR_PATH.

Exercise 9: Plots different relations for the data inside the "file2Groups_AGN-wWU_500Mpc_Data" file. The libraries numpy, matplotlib and matplotlib.colors are needed to run the program. The plots are displayed on screen and need user input to save (Automatic save has not been implemented).
 
Usage Instructions:
After cloning the repository navigate to the desired folder and run the scripts by executing one of the following commands:

	Exercise 1 -> './Es1.sh'
	Exercise 3 -> './Es3.sh'
	Exercise 5 -> './Es5.sh'
	Exercise 8 -> './Es8.sh "dir_name"'
	Exercise 9 -> 'python3 EsPy.py'
	
Ensure the dependancies for the python script are installed with: pip install numpy matplotlib
