import sys
import os

arguments = sys.argv
usage = 'pyaccess.py  /path/to/access.log  min_hit_count '

if len(arguments) == 3:
    
    logFile = arguments[1]
    minHit  = arguments[2]    
    if os.path.exists(logFile) and os.path.isfile(logFile) and minHit.isdigit():
        
        logFh = open(logFile)
        hitCounter = {}
        for logLine in logFh:
        
            host = logLine.split()[0]            
            if host not in hitCounter:          
                hitCounter[host] = 1
            else:        
                hitCounter[host] = hitCounter[host] + 1
    
        logFh.close()        
        for ip in hitCounter:    
        
            count  = hitCounter[ip]    
            if count >= int(minHit):        
                output = '{:15} : {}'.format(ip,count)    
                print(output)
        
    else:
    
        print(usage)

else:

    print()
    print(usage)
