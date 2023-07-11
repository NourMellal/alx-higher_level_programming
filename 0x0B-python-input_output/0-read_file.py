#!/usr/bin/python3
def read_file(filename=""):
    """ read file and print its content"""
    with open(filename, "r", encoding='uft-8') as file:
        print(file.read())
