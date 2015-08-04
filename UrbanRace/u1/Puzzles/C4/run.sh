#!/bin/bash

PASSWORD=COOLMOON
scala ../../Code/Scala/domEncrypt.scala $PASSWORD < graphInput.txt > worksheet.txt

# Use the scrambler here for effect.  But it needs some find tuning.
echo "the key for june twenty ninth is" | scala ../../Code/Scala/messageShuffle.scala > scrambled.txt
