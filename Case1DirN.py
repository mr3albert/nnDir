#!/usr/bin/python
import os #using os.listdir, os.path.dirname, os.path.abspath, os.chdir...

DirNArray = os.listdir() #turning all of the test case files into an array
subDirArray = os.listdir() #testcase directory name array  
address = os.path.dirname(os.path.abspath(__file__)) #address of the current directory s
subDir = ''
logBools = False
sessBools = False
DirCount = 0

f = open("Case1Ns.txt", "w+")

for i in range(len(DirNArray)):
    subDir = os.path.join(address,DirNArray[i])#appends the current directory address with a subdirectory name to form the address for the sub directory
    if( os.path.isdir(subDir) != True): 
        continue 
    print(DirNArray[i])
    f.write(DirNArray[i] +"\n")
    DirCount++

print(DirCount)