#!/usr/bin/env python3

def ws():
    count = 0
    f1=input("Enter the file name : ")
    word = input("Enter the word that need to be checked : ")
    with open(f1,"r") as x1:
        for i in x1:
            w = i.split()
            for j in w:
                if(j == word):
                    count += 1
    print(word," occurs ",count," times ")

ws()
