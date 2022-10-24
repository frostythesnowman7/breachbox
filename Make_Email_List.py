#!/usr/bin/python
###This script is not safe###
###Written by Jason Evans 2022###

import re, sys, getopt

def parsefile(file_name, out_filename):
    file1 = open(out_filename, "a")
    with open(file_name, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            try:
                data = list(eval(line))
            except:
                pass
            for email in data:
                try:   
                    writestr = str(email[0]) + ":" + email[1]
                    file1.writelines(writestr + "\n")
#                    print(writestr)
                except:
                    pass

    file1.close()

argumentList = sys.argv[1:]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            print ("This script sorts through linkedin data and isolates emails\n %s inputfile outputfile", sys.argv[0])
             
        elif len(argumentList) = 2:
            parsefile(sys.argv[1], sys.argv[2])
             
        
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))


