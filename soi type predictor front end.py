from tkinter import *
from tkinter import messagebox

def printfun():
    soilval=soil.get()
    locval=location1.get()
    phval=pH.get()
    wh=whcap.get()
    for i in range(len(typesoil)):
        if soilval==typesoil[i]:
            soilval=str(i+1)
            break
    for i in range(len(location)):
        if locval==location[i]:
            locval=str(i+1)
            break
    for i in range(len(ph)):
        if phval==ph[i]:
            phval=str(i+1)
            break
    for i in range(len(whcapacity)):
        if wh==whcapacity[i]:
            wh=str(i+1)
            break
    print(soilval,locval,phval,wh)
    f=open('mainfile.txt','r')
    f2=open('index.txt','r')
    s2=soilval+locval+phval+wh
    flag2=0
    for line2 in f2:
        if s2==line2[0:4]:
            offs=int(line2[5:])
            print(offs)
            f.seek(offs,0)
            z=f.readline()[-3]
            print(z)
            messagebox.showinfo("yes",z)
    new=Toplevel(root)
    
    


root=Tk()
root.title("Crop Predictor")
root.geometry("500x500")
heading=Label(text="Crop Prediction",bg="LightSteelBlue1",fg="black",width="500",height="3")
heading.pack()
###################################################################################
typesoil=['Alluvial','Red','Black','Arid','Laterite']
location=['U.P.','Maharashtra','Rajasthan','Uttarkhand','Karnataka']
ph=[3,5,7,9]
whcapacity=[40,50,60,70]
##################################################
slt=Label(text="Soil Type")
slt.place(x=15,y=70)
lct=Label(text="Location")
lct.place(x=250,y=70)
phs=Label(text="pH value")
phs.place(x=15,y=200)
wc=Label(text="W.C. capacity")
wc.place(x=250,y=200)
soil=StringVar()
soilch=OptionMenu(root,soil,'Alluvial','Red','Black','Arid','Laterite')
soilch.config(font=("Arial",10))
soilch.place(x=100,y=70)
location1=StringVar()
locch=OptionMenu(root,location1,'U.P.','Maharashtra','Rajasthan','Uttarkhand','Karnataka')
locch.config(font=("Arial",10))
locch.place(x=350,y=70)
pH=IntVar()
phch=OptionMenu(root,pH,3,5,7,9)
phch.config(font=("Arial",10))
phch.place(x=100,y=200)
whcap=IntVar()
whch=OptionMenu(root,whcap,40,50,60,70)
whch.config(font=("Arial",10))
whch.place(x=350,y=200)

search=Button(text="Search",width="30",height="2",command=printfun,bg="LightSteelBlue1")
search.place(x=120,y=350)



root.mainloop()