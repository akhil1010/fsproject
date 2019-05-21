import random

#pid=1000
typesoil=['Alluvial','Red','Black','Arid','Laterite']
location=['U.P.','Maharashtra','Rajasthan','Uttarakhand','Karnataka']
ph=[3,5,7,9]
whcapacity=[40,50,60,70]
#croptype=['A','B','C','D','E']
#p=1
#pid=str(i+1)+str(j+1)+str(k+1)+str(l+1)
croptype='A'
f=open('mainfilenew.txt','w')
for i in range(len(typesoil)):
    for j in range(len(location)):
        for k in range(len(ph)):
            for l in range(len(whcapacity)):
                pid=str(i+1)+str(j+1)+str(k+1)+str(l+1)
                if pid[0]=='2' and pid[1]=='3':
                    croptype='D'
                elif (pid[0]=='3' or pid[0]=='4' or pid[0]=='5') and pid[1]=='1':
                    croptype='D'
                elif ( pid[0]=='1' or pid[0]=='4' or pid[0]=='5' ) and pid[1]=='5':
                    croptype='D'
                elif (pid[0]=='2' or pid[0]=='3' or pid[0]=='4' or pid[0]=='5') and pid[1]=='4':
                    croptype='D'
                elif (pid[0]=='1' or pid[0]=='4' or pid[0]=='5' ) and pid[1]=='2':
                    croptype='D'
                cstring=str(pid)+'|'+str(typesoil[i])+'|'+str(location[j])+'|'+str(ph[k])+'|'+str(whcapacity[l])+'|'+random.choice(croptype)+"$"
                croptype='a'
                f.write(cstring)
                f.write("\n")
                #print(pid,'|',i,'|',j,'|',k,'|',l,end="$")
                
f.close()


                
    
    