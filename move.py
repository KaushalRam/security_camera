import os 
import shutil

source = input("Enter the source filename:- ")
destination = input("Enter the destination filename:- ")
source = source+"/"
destination=destination+"/"
listoffiles = os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),destination)
