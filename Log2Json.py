# Mohammad Javad Abaei #
import sys
import fileinput
import re
import json

#Read file
def readfile(file):
    filecontent = {}
    index = 0
    for line in fileinput.input(file):
            index = index+1
            if line != "\n": #don't read newlines
                filecontent[index] = line2dict(line)

    fileinput.close()
    return filecontent

#1.Get Line Of String  2.Convert into Dict Obj
def line2dict(line):
    parts = [
    r'(?P<IP>\S+)',                 
    r'(?P<identity>\S+)',               
    r'(?P<username>\S+)',             
    r'\[(?P<time>.+)\]',               
    r'"(?P<request>.+)"',               
    r'(?P<response_status>[0-9]+)',     
    r'(?P<response_size>\S+)',          
]
    pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
    m = pattern.match(line)
    res = m.groupdict()
    return res

#Let's Do It 
out_file = open("log.json", "w")
entities = readfile(sys.argv[1])
json.dump(entities, out_file, indent = 4)
out_file.close()