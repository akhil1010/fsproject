import random

#pid=1000
typesoil=['Alluvial','Red','Black','Arid','Laterite']
location=['U.P.','Maharashtra','Rajasthan','Uttarakhand','Karnataka']
ph=[3,5,7,9]
whcapacity=[40,50,60,70]
croptype=['A','B','C','D','E']
#p=1
#pid=str(i+1)+str(j+1)+str(k+1)+str(l+1)
f=open('mainfile.txt','w')
for i in range(len(typesoil)):
    for j in range(len(location)):
        for k in range(len(ph)):
            for l in range(len(whcapacity)):
                pid=str(i+1)+str(j+1)+str(k+1)+str(l+1)
                cstring=str(pid)+'|'+str(i+1)+'|'+str(j+1)+'|'+str(k+1)+'|'+str(l+1)+'|'+random.choice(croptype)+"$"
                f.write(cstring)
                f.write("\n")
                #print(pid,'|',i,'|',j,'|',k,'|',l,end="$")
                
f.close()

                
    
    