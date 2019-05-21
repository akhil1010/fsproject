f1=open("mainfile.txt",'r')
f2=open("index.txt",'w')
pos='0'
line=f1.readline()
while line:
    s=line[0:5]+pos
    f2.write(s)
    f2.write('\n')
    pos=str(f1.tell())
    line=f1.readline()
f1.close()
f2.close()