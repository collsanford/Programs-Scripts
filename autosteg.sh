###################################################################
# !/bin/sh
# autosteg.sh
# Cheese-it Grooves
# Collin Sanford, Matthew Reed, Madison Gay
# Runs the steg.py program and iterates through offsets/intervals
###################################################################

# If no arguments given
if [ "$1" = "" ]; then
	echo "No arguments, -h for help"

else
	# display help 
	if [ $1 = "-h" ]; then
		echo "autosteg.sh V1.2(May 7, 2018)"
		echo "Usage: autosteg.sh -bB filename output"
		echo "Cycles through combinations of offsets and intervals"
		exit 0
	
	# for bit method
	elif [ $1 = "-b" ]; then
		
		i=66
		
		# iterate from 66 - 100
		while [ $i -lt  101 ]; do
			
			offset=$[$i]
			
			if [ $1 = "-b" ]; then
				filename="$3-$offset"
				python steg.py $1 "-r"  "-o$offset" "-w$2" > "$filename"
			fi

			filetype=$(file "$filename")
			
			# filter out useless files
			if [ "$filetype" != "$filename: data" -a "$filetype" != "$filename: empty" ]; then
				echo "$filetype"
			else
				rm $filename
			fi

			((i++))
		done
		break
	else
		echo "Wrong arguments, -h for help"
		exit 0
	fi
fi

