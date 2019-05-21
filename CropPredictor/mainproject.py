import re
f=open('mainfile.txt','r')

f2=open('index.txt','r')
'''
location=(input("Enter the location: \npress 1 for U.P.\npress 2 for for Maharashtra\npress 3 for Rajasthan \npress 4 for Uttrakhand\npress 5 for Karnataka "))
colortype=(input("Enter the Colortype: \npress 1 for Alluvial\npress 2 for Red\npress 3 for Black\npress 4 for Arid "))
whcapacity=(input("Enter the Water holding capacity: \npress 1 for 30-49%\npress 2 for capacity between 40-49%\npress 3 for capacity between 50-59%\npress 4 for capacity between 60-70%"))
ph=(input("Enter the ph: 1 for 3\n2 for 5\n3 for 7\n4 for 9"))
s='|'+colortype+'|'+location+'|'+ph+'|'+whcapacity+'|'

flag=0
for line in f:
    if(s==line[4:13]):
        print(line,"\n")
        
'''        
        
        
        
location=(input("Enter the location: \npress 1 for U.P.\npress 2 for for Maharashtra\npress 3 for Rajasthan \npress 4 for Uttrakhand\npress 5 for Karnataka "))
colortype=(input("Enter the Colortype: \npress 1 for Alluvial\npress 2 for Red\npress 3 for Black\npress 4 for Arid "))
whcapacity=(input("Enter the Water holding capacity: \npress 1 for 30-49%\npress 2 for capacity between 40-49%\npress 3 for capacity between 50-59%\npress 4 for capacity between 60-70%"))
ph=(input("Enter the ph: 1 for 3\n2 for 5\n3 for 7\n4 for 9"))       
s2=colortype+location+ph+whcapacity
flag2=0
for line2 in f2:
    if s2==line2[0:4]:
        offs=int(line2[5:])
print(offs)
f.seek(offs,0)
print(f.readline()[-3])