#!/bin/zsh
export RACE_DAY="July 14 2017"
pdftk Diary.pdf burst output %02d.pdf compress
NAME=`date --date "$RACE_DAY - $(date +30) day" '+%B%d'`
pdftk 01.pdf output 01_$NAME.pdf owner_pw cyd user_pw catchawave encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +29) day" '+%B%d'`
pdftk 02.pdf output 02_$NAME.pdf owner_pw cyd user_pw felinebackdoor encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +28) day" '+%B%d'`
pdftk 03.pdf output 03_$NAME.pdf owner_pw cyd user_pw thepigsays encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +27) day" '+%B%d'`
pdftk 04.pdf output 04_$NAME.pdf owner_pw cyd user_pw perceiveyourgoal encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +26) day" '+%B%d'`
pdftk 05.pdf output 05_$NAME.pdf owner_pw cyd user_pw shirleysidentities encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +25) day" '+%B%d'`
pdftk 06.pdf output 06_$NAME.pdf owner_pw cyd user_pw onionroute encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +24) day" '+%B%d'`
pdftk 07.pdf output 07_$NAME.pdf owner_pw cyd user_pw atubertoolbox encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +23) day" '+%B%d'`
pdftk 08.pdf output 08_$NAME.pdf owner_pw cyd user_pw codepattern encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +22) day" '+%B%d'`
pdftk 09.pdf output 09_$NAME.pdf owner_pw cyd user_pw merriamsintrusion encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +21) day" '+%B%d'`
pdftk 10.pdf output 10_$NAME.pdf owner_pw cyd user_pw greatwhitecable encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +20) day" '+%B%d'`
pdftk 11.pdf output 11_$NAME.pdf owner_pw cyd user_pw greeksubterfuge encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +19) day" '+%B%d'`
pdftk 12.pdf output 12_$NAME.pdf owner_pw cyd user_pw shinymetal encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +18) day" '+%B%d'`
pdftk 13.pdf output 13_$NAME.pdf owner_pw cyd user_pw firstcatch encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +17) day" '+%B%d'`
pdftk 14.pdf output 14_$NAME.pdf owner_pw cyd user_pw hailmary encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +16) day" '+%B%d'`
pdftk 15.pdf output 15_$NAME.pdf owner_pw cyd user_pw mousetakeover encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +15) day" '+%B%d'`
pdftk 16.pdf output 16_$NAME.pdf owner_pw cyd user_pw muttonroast encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +14) day" '+%B%d'`
pdftk 17.pdf output 17_$NAME.pdf owner_pw cyd user_pw reverselook encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +13) day" '+%B%d'`
pdftk 18.pdf output 18_$NAME.pdf owner_pw cyd user_pw perimeterbarrier encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +12) day" '+%B%d'`
pdftk 19.pdf output 19_$NAME.pdf owner_pw cyd user_pw humanhorse encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +11) day" '+%B%d'`
pdftk 20.pdf output 20_$NAME.pdf owner_pw cyd user_pw rapidseven encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +10) day" '+%B%d'`
pdftk 21.pdf output 21_$NAME.pdf owner_pw cyd user_pw dropbobby encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +9) day" '+%B%d'`
pdftk 22.pdf output 22_$NAME.pdf owner_pw cyd user_pw ringzero encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +8) day" '+%B%d'`
pdftk 23.pdf output 23_$NAME.pdf owner_pw cyd user_pw leakybug encrypt_128bit
NAME=`date --date "$RACE_DAY - $(date +7) day" '+%B%d'`
pdftk 24.pdf output 24_$NAME.pdf owner_pw cyd user_pw iheartjumbles encrypt_128bit
zip diary.zip *_*.pdf
rm [012]*.pdf doc_data.txt
