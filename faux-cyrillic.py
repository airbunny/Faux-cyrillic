#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

################################
#   translate singal letter
################################
def lettertofaux(letter):
    
    if letter == "R" or letter =="r":
        res = "Я"
    elif letter == "B" or letter =="b":
        res = "Ь"
    elif letter == "E" or letter == "e":
        res = "Э"
    elif letter == "W" or letter == "w":
        res = "Ш"
    elif letter == "Y" or letter == "y":
        res = "Ч"
    elif letter == "U" or letter == "u":
        res = "Ц"
    elif letter == "O" or letter == "o":
        res = "Ф"
    elif letter == "Y" or letter == "y":
        res = "У"
    elif letter == "J" or letter == "j":
        res = "Ԓ"
    elif letter == "N" or letter == "n":
        res = "И"
    elif letter == "X" or letter == "x":
        res = "Ж"
    elif letter == "A" or letter == "a":
        res = "Д"
    elif letter == "F" or letter == "f":
        res = "Г"
    elif letter == "G" or letter == "g":
        res = "Б"
    else:
        res = letter.upper();
    return res;
################################
#   translate string
################################
def latintofauxcyrillic(latin):

    #get string lenth
    lens = len(latin);

    #cutof singal word from the string from start to 
    outstring = ""

    for i in range(lens+1): 
        outstring += lettertofaux(latin[i-1:i]);

    return outstring;


################################
#   string transelate interface
################################
def transe():
    string = input("input latin word>>");
    string = latintofauxcyrillic(string);
    print(string);

################################
#   console
################################
def comdpro(command):
    res = 1

    if command == "help":
        print("exit:        Exit");
        print("transe:      Transe string to faux Cyrillic");
    elif command == "exit":
        res = 0
    elif command == "transe":
        transe();
    else:
        print("Error!Not legal command!");
    return res;

################################
#   main process
################################
loop = 1

while(loop == 1):
    bash = input("CMD>>");
    loop = comdpro(bash);

input("Press any key to continud...");
