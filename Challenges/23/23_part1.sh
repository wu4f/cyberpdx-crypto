#!/bin/bash

PASSWORD=leakybug
scala ./Code/Scala/domEncrypt.scala $PASSWORD < graphInput.txt > 23_part1_output.txt

# Use the scrambler here for effect.  But it needs some find tuning.
echo "the key for number twenty three is" | scala ./Code/Scala/messageShuffle.scala > 23a_final.txt
