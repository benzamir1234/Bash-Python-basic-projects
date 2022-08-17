#!/bin/bash
echo "Enter rows number: "
read rows
echo "Enter column number: "
read colum
while [ $rows -ge 1 ]
do
	for (( i=1; i<=$colum; i++))
	do
		echo -n "Net4U "
		if  [ $i == $colum ] ; then
			echo -e "\n"
		fi
	done
	let "rows = rows - 1"
done
