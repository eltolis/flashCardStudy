flashCardStudy
==============

Flash card script for drilling definitions in Python

-------------

This script is useful for drilling definitions, translations etc. It runs in loop forever
and randomly selects 'flash cards' from a text file.
First it shows you the word and after hitting a key it reveals its definition.

You need to have both files ('flashCardStudy.xx.py', 'flashcards.txt') in the same directory.
The flash cards go into the file 'flashcards.txt'. There are few examples in there so you can
see how it is structured. 

flashcards.txt
--------------
Basicly each flash card needs to be on new line. In the real world
flash card has two sides, one with the word and the other with the definition. Front side is on the left,
the it's followed by colon (':') separator.
Back side is after the colon on the right. It's that easy. Modify this file to have your flash cards.

flashCardStudy.xx.py
--------------------
This is simple Python 2.7 file. Just run it in your terminal and you will get instructions on screen.
