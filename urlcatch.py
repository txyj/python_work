import urllib
import time
import socket
import os

socket.setdefaulttimeout(1)

rst_filename = os.getcwd()+"/result"+str(time.strftime('%Y%m%d%H%M%S'))+".txt"
f = open(rst_filename,'a')
print "result path:\n" + rst_filename+"\n\n"

for line in open("E:/py/url.txt", "r"): 
    line=line.strip('\n')
    if len(line) == 0:
        break
    try:
        if urllib.urlopen(line).getcode() == 200:
            result = line+"\t"+"succeed\n"
        else:
            result = line+"\t"+"fail\n"
    except:
        result = line+"\t"+"fail\n"
  
    print result
    f.write(result)

else:
    f.close()
    
 
