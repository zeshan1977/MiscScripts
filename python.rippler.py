
import fileinput
import re
from os.path import dirname, basename
import os



sSTART='START'
sEND='END'

sfilename=[]
#global sFILE


print "START >>> "

f = open('nf.txt', 'r')
#for line1 in fileinput.input():
for line1 in f:    
    #if sSTART.match(line):
    line = line1.rstrip()
    if re.search("swp",line):
       continue
"""
    if not re.search('^[a-zA-Z0-9_;:.<>\+\=\*\(\)\"\'\}\}\[\] \&\,\?/]+',line):
       print "FUCK " + line1 
       continue
"""
    if re.search(sSTART,line):
        print "DOH S" + line
        sfilename=line.split(':')
        if not os.path.exists(dirname(sfilename[1])):
            try: 
                os.makedirs(dirname(sfilename[1]))
            except OSError:
                if not os.path.isdir(dirname(sfilename[1])):
                   raise
    #        if not os.path.exists(sfilename[1]):
 #           print "making dirname " + dirname(sfilename[1])
            #os.mkdir(os.path.dirname(sfilename[1]),0755)
  #          os.mkdir(os.path.dirname(sfilename[1]))
            
       #     sFILE=open(sfilename[1],'w')
    if not (re.search(sSTART,line) and re.search(sEND,line)):
       print "Not Match " + line
       sFILE=open(sfilename[1],'a')
       sFILE.write(line)
       sFILE.close()
        #if sEND.match(line):
    if re.search(sEND,line):
       print "DOH E " + line
"""        
f.close()
print "END >>> "        
        
        
