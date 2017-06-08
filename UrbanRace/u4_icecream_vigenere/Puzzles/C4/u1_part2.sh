#!/bin/bash

# This array was filled in (manually) after running the Encryption Program
# Sadly it is not fully automated yet.

# Replace this content with the results of running 23_part1.sh (the arrX) values
# Also replace "31" below with the correct number of nodes
arr0=( 14 16 8 5 4 23 13 11 18 9 13 19 32 25 23 15 22 20 13 18 14 10 12 )
arr1=( 16 13 8 13 12 22 19 18 18 9 16 9 19 11 12 9 18 16 16 12 17 15 22 )
arr2=( 19 18 15 17 15 18 17 18 13 11 17 14 22 18 12 3 9 14 12 9 13 8 9 )
arr3=( 22 14 15 18 16 24 18 18 15 9 15 10 24 18 11 9 20 21 19 20 19 16 21 )
arr4=( 17 13 10 12 9 15 23 16 18 14 24 6 17 11 9 7 19 19 20 13 20 15 13 )
arr5=( 26 19 18 22 18 18 20 18 18 9 22 10 15 15 13 6 18 26 16 15 12 11 13 )
arr6=( 22 16 12 15 11 28 7 17 9 2 4 19 29 22 20 10 23 18 11 20 13 10 8 )

# Message X
for NUM in {0..6}; do   # <<<<<===== Length of message goes here
    echo "Processing Message $NUM"
    cp MessageBlank.graphml Message${NUM}.graphml
    for i in {0..22}; do   # <<<<========== This here
	node="arr${NUM}[$i]"
	sed /'>'N$i'<'/s//'>'${!node}'<'/ Message${NUM}.graphml > Temp.graphml
	mv Temp.graphml Message${NUM}.graphml
    done
done

