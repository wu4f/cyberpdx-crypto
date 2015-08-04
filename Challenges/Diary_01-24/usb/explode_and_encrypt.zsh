#!/bin/zsh
pdftk Diary.pdf burst output p6-%02d.pdf compress
rm p6-0[123456].pdf
pdftk p6-07.pdf output 6-07.pdf owner_pw cyd user_pw keylogging encrypt_128bit
pdftk p6-08.pdf output 6-08.pdf owner_pw cyd user_pw backdoor encrypt_128bit
pdftk p6-09.pdf output 6-09.pdf owner_pw cyd user_pw tripwire encrypt_128bit
pdftk p6-10.pdf output 6-10.pdf owner_pw cyd user_pw stegosaurus encrypt_128bit
pdftk p6-11.pdf output 6-11.pdf owner_pw cyd user_pw exploit encrypt_128bit
pdftk p6-12.pdf output 6-12.pdf owner_pw cyd user_pw poser encrypt_128bit
pdftk p6-13.pdf output 6-13.pdf owner_pw cyd user_pw rockhop encrypt_128bit
pdftk p6-14.pdf output 6-14.pdf owner_pw cyd user_pw subterfuge encrypt_128bit
pdftk p6-15.pdf output 6-15.pdf owner_pw cyd user_pw codebook encrypt_128bit
pdftk p6-16.pdf output 6-16.pdf owner_pw cyd user_pw webster encrypt_128bit
pdftk p6-17.pdf output 6-17.pdf owner_pw cyd user_pw surveillance encrypt_128bit
pdftk p6-18.pdf output 6-18.pdf owner_pw cyd user_pw horse encrypt_128bit
pdftk p6-19.pdf output 6-19.pdf owner_pw cyd user_pw whitelist encrypt_128bit
pdftk p6-20.pdf output 6-20.pdf owner_pw cyd user_pw privacy encrypt_128bit
pdftk p6-21.pdf output 6-21.pdf owner_pw cyd user_pw impersonate encrypt_128bit
pdftk p6-22.pdf output 6-22.pdf owner_pw cyd user_pw totalrecall encrypt_128bit
pdftk p6-23.pdf output 6-23.pdf owner_pw cyd user_pw intercept encrypt_128bit
pdftk p6-24.pdf output 6-24.pdf owner_pw cyd user_pw mirrored encrypt_128bit
pdftk p6-25.pdf output 6-25.pdf owner_pw cyd user_pw fortress encrypt_128bit
pdftk p6-26.pdf output 6-26.pdf owner_pw cyd user_pw attacksurface encrypt_128bit
pdftk p6-27.pdf output 6-27.pdf owner_pw cyd user_pw maliciousinput encrypt_128bit
pdftk p6-28.pdf output 6-28.pdf owner_pw cyd user_pw administrator encrypt_128bit
pdftk p6-29.pdf output 6-29.pdf owner_pw cyd user_pw leak encrypt_128bit
pdftk p6-30.pdf output 6-30.pdf owner_pw cyd user_pw jumblesarefun encrypt_128bit
