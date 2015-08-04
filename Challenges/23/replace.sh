#!/bin/bash

# This array was filled in (manually) after running the Encryption Program
# Sadly it is not fully automated yet.

# Replace this content with the results of running run.sh (the arrX) values
# Also replace "31" below with the correct number of nodes
arr0=( 29 30 21 25 17 26 21 19 19 9 25 18 23 23 20 12 21 30 28 20 23 27 30 )
arr1=( 29 17 16 21 20 26 26 27 29 18 29 16 31 23 20 10 20 27 20 23 16 16 25 )
arr2=( 27 19 20 27 21 28 24 28 23 12 20 14 27 17 12 13 22 24 19 22 19 16 19 )
arr3=( 27 23 24 29 23 32 29 24 28 15 27 16 23 18 10 13 26 28 22 22 21 21 25 )

# Message X
for NUM in {0..3}; do   # <<<<<===== Length of message goes here
    echo "Processing Message $NUM"
    cp MessageBlank.graphml Message${NUM}.graphml
    for i in {0..22}; do   # <<<<========== This here
	node="arr${NUM}[$i]"
	sed /'>'N$i'<'/s//'>'${!node}'<'/ Message${NUM}.graphml > Temp.graphml
	mv Temp.graphml Message${NUM}.graphml
    done
done

