#!/usr/bin/python
import os

os.chdir('/home/kali/Desktop/name')

for f in os.listdir():
    fl, ex = f.split('.')
    n0, n1, num = fl.split(' ')
    num =num.split()
    
    for n in num:
        if int(n) < 10:
            n = "000000000" + str(n)

            
        elif int(n)<100 and int(n)>=10:
            n = "00000000" + str(n)
        
        
        elif int(n)<1000 and int(n)>=100:
            n = "0000000" + str(n)
        
        
        elif int(n)<10000 and int(n)>=1000:
            n = "000000" + str(n)
         
        
        elif int(n)<100000 and int(n)>=10000:
            n = "00000" + str(n)
            
    os.rename(f,n+"."+ex)