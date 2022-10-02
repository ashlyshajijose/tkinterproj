from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()

root.geometry("580x715")

root.title('Registration form')


def fun():
    global mydb,mycursor
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='Tkinter2'
        )
    mycursor = mydb.cursor()

def reg():
    gend()
    qlfn()
    fun()
    global first_name,last_name,addrs,Eml,mblno,gender,country,st,district,pincode,quali
    first_name=firstname.get()
    last_name=lastname.get()
    addrs=address.get()
    Eml=Email.get()
    mblno=mobileno.get()
    gender=b
    country=c.get()
    st=state.get()
    district=d.get()
    pincode=pin.get()
    quali=str(e+'\n') + str(x+'\n') + str(s1+'\n') + str(h) 

    if first_name=="" or last_name=="" or addrs=="" or Eml=="" or mblno=="" or gender=="" or country=="" or st=="" or district=="" or pincode=="" or quali=="":
        Label(root,text="Please complete the form", fg='red').place(x=50,y=660)
    else:
            sql="INSERT INTO registration VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
            val=(first_name,last_name,addrs,Eml,mblno,gender,country,st,district,pincode,quali)
            mycursor.execute(sql,val)
            mydb.commit()
            messagebox.showinfo('Registration successfull','Registration successfull')

def gend():
    global a,b
    a=var.get()
    
    if a==1:
        b='Male'
    elif a ==2:
        b='Female'
    else:
        b='Others'

def qlfn():
    global g,j,r,e,x,s1,h
    g=var1.get()
    j=var2.get()
    r=var3.get()
    h=var4.get()
    if g==1:
        e="SSLC"
    if j==1:
        x="Plus Two"
    if r==1:
        s1="Graduate"
    else:
        h="Post graduate"


firstname=StringVar()
lastname=StringVar()
address=StringVar()
Email=StringVar()
mobileno=IntVar()
state=StringVar()
pin=IntVar()


label_0 =Label(root,text="Registration form", width=20,font=("bold",20)).place(x=90,y=60)



label_1 =Label(root,text="FirstName:", width=20,font=("bold",10)).place(x=80,y=130)
entry_1=Entry(root,textvariable=firstname).place(x=240,y=130)


label_2 =Label(root,text="LastName:", width=20,font=("bold",10)).place(x=80,y=180)
entry_2=Entry(root,textvariable=lastname).place(x=240,y=180)


label_3 =Label(root,text="Address:", width=20,font=("bold",10)).place(x=80,y=230)
entry_3=Entry(root,textvariable=address).place(x=240,y=230)

label_4 =Label(root,text="Email:", width=20,font=("bold",10)).place(x=68,y=280)
entry_4=Entry(root,textvariable=Email).place(x=240,y=280)


label_5 =Label(root,text="MobileNo:", width=20,font=("bold",10)).place(x=80,y=330)
entry_5=Entry(root,textvariable=mobileno).place(x=240,y=330)




label_6 =Label(root,text="Gender:", width=20,font=("bold",10)).place(x=70,y=380)

var=IntVar()

Radiobutton(root,text="M",padx= 5, variable= var, value=1).place(x=235,y=380)
Radiobutton(root,text="F",padx= 20, variable= var, value=2).place(x=290,y=380)
Radiobutton(root,text="O",padx= 30, variable= var, value=3).place(x=350,y=380)


label_7=Label(root,text="Country:",width=20,font=("bold",10)).place(x=70,y=430)

list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']

c=StringVar()
droplist=OptionMenu(root,c, *list_of_country)
droplist.config(width=15)
c.set('Select your Country')
droplist.place(x=240,y=430)



label_8 =Label(root,text="State:", width=20,font=("bold",10)).place(x=68,y=480)
entry_8=Entry(root,textvariable=state).place(x=240,y=480)



label_9=Label(root,text="District:",width=20,font=("bold",10)).place(x=70,y=530)

list_of_district=[ 'Kasargod' ,'Palakkad' , 'Kottayam' ,'Ernakulam' ,'Malappuram']

d=StringVar()
droplist=OptionMenu(root,d, *list_of_district)
droplist.config(width=15)
d.set('Select your district')
droplist.place(x=240,y=530)


label_8 =Label(root,text="Pincode:", width=20,font=("bold",10)).place(x=68,y=580)
entry_8=Entry(root,textvariable=pin).place(x=240,y=580)


label_9=Label(root,text="Qualification:",width=20,font=('bold',10)).place(x=75,y=630)

var1=IntVar()
sslc1=StringVar()
Checkbutton(root,text="SSLC", variable=var1, onvalue=1, offvalue=0).place(x=230,y=630)

var2=IntVar()
plus_two1=StringVar()
Checkbutton(root,text="Plustwo", variable=var2, onvalue=1, offvalue=0).place(x=290,y=630)

var3=IntVar()
graduate1=StringVar()
Checkbutton(root,text="Graduate", variable=var3, onvalue=1, offvalue=0).place(x=370,y=630)

var4=IntVar()
postgraduate1=StringVar()
Checkbutton(root,text="PostGraduate", variable=var4, onvalue=1, offvalue=0).place(x=460,y=630)


Button(root, text='Submit' , width=10,bg="green",fg='white',command=reg).place(x=180,y=670)


root.mainloop()