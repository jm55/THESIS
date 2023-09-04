import os

filename = input("Enter filename: ")

file = open(filename, mode="r")

for line in file:
    print(line)
    input()