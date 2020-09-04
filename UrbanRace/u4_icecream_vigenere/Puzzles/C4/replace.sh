#!/bin/bash

# This array was filled in (manually) after running the Encryption Program
# Sadly it is not fully automated yet.

# Replace this content with the results of running run.sh (the arrX) values
# Also replace "31" below with the correct number of nodes
arr0=( 19 14 11 12 8 15 11 16 15 8 12 14 26 16 16 10 17 16 13 13 15 9 13 )
arr1=( 19 16 12 18 14 14 16 20 17 11 18 13 26 15 11 12 11 22 19 18 19 15 22 )
arr2=( 19 13 10 15 12 18 14 15 17 10 15 13 27 20 10 7 17 19 26 24 28 19 19 )
arr3=( 22 17 15 16 8 16 14 19 16 10 14 14 28 19 11 9 17 20 17 21 20 14 17 )
arr4=( 17 9 9 14 14 19 21 15 18 16 25 16 22 19 15 7 17 19 16 13 11 15 22 )
arr5=( 21 16 15 22 18 15 20 18 16 12 21 12 19 16 8 7 13 22 19 17 18 15 19 )
arr6=( 28 18 16 16 15 21 16 18 17 10 19 9 22 16 20 8 17 20 18 15 14 14 20 )
arr7=( 19 18 16 16 13 18 13 14 12 9 13 11 16 22 13 10 12 15 25 21 24 22 15 )

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

