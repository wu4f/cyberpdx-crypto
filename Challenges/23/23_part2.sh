#!/bin/bash

# This array was filled in (manually) after running the Encryption Program
# Sadly it is not fully automated yet.

# Replace this content with the results of running 23_part1.sh (the arrX) values
# Also replace "31" below with the correct number of nodes
arr0=( 29 23 17 21 16 29 28 24 26 16 30 19 29 27 22 8 26 29 24 24 20 20 21 )
arr1=( 20 31 16 24 18 38 26 19 23 12 20 27 28 20 19 13 23 24 15 20 19 14 23 )
arr2=( 30 21 22 25 20 26 24 22 20 13 22 13 27 21 17 11 21 25 19 18 17 15 20 )
arr3=( 27 21 17 21 17 30 27 22 23 17 27 20 34 25 20 10 24 31 23 25 21 19 31 )
arr4=( 26 30 20 20 14 28 31 19 24 23 31 20 35 28 22 14 20 23 30 25 32 24 26 )
arr5=( 27 29 17 20 14 24 19 22 23 13 22 23 33 20 17 12 21 22 17 17 23 14 20 )
arr6=( 35 26 21 30 24 31 18 24 23 7 22 21 41 26 20 17 27 35 26 22 23 21 27 )
arr7=( 28 30 21 18 12 26 16 15 20 11 24 20 34 22 22 17 23 34 22 20 19 18 24 )

# Message X
for NUM in {0..7}; do   # <<<<<===== Length of message goes here
    echo "Processing Message $NUM"
    cp MessageBlank.graphml Message${NUM}.graphml
    for i in {0..22}; do   # <<<<========== This here
	node="arr${NUM}[$i]"
	sed /'>'N$i'<'/s//'>'${!node}'<'/ Message${NUM}.graphml > Temp.graphml
	mv Temp.graphml Message${NUM}.graphml
    done
done

