import mysql.connector
from tkinter import *
from tkinter import messagebox
form= Tk()
form.geometry('300x700')
def conn():
    global mydb, data
    mydb=mysql.connector.connect(
        host='localhost', user='root', passwd='', database='form')
    data=mydb.cursor()

def sbmt():
    gend()
    qlfn()
    conn()
    global fname,lname,addr,emid,mob,birth,gen,educ
    fname= fName.get()
    lname=lName.get()
    addr=Address.get()
    emid=email.get()
    mob=phnb.get()
    birth=dob.get()
    gen=b
    educ=str(e+'\n') + str(x+'\n') + str(s1)
    if fname=='' or lname=='' or addr=='' or emid=='' or mob=='' or birth=='' or gen=='' or educ=='':
        Label(form,text="Please complete the form", fg='red').place(x=50 ,y=660)
    else:
        sql=('INSERT INTO register values(%s,%s,%s,%s,%s,%s,%s,%s)')
        val=(fname,lname,addr,emid,mob,birth,gen,educ)
        data.execute(sql,val)
        mydb.commit()
        messagebox.showinfo('success', 'Success')
def gend():
    global a,b
    a=radio.get()
    
    if a==1:
        b='Male'
    elif a ==2:
        b='Female'
    else:
        b='Others'

def qlfn():
    global g,c,d,e,x,s1,h
    g=sslc.get()
    c=plus_two.get()
    d=graduate.get()
    h=grad.get()
    if g==1:
        e="SSlC"
    if c ==1:
        x="Plus Two"
    if d==1 and h=='Mechanical Engg':
        s1='Mechanical Engg'
    elif d==1 and h=="Civil Engg":
        s1='Civil Engg'
    elif d ==1 and h=='Electrical Engg':
        s1='Electrical Engg'
    

fName=StringVar()
lName=StringVar()
Address=StringVar()
email=StringVar()
phnb=IntVar()
dob=StringVar()

head=Label(form, text='REGISTRATION', fg='purple').pack()
PermissionError=Label(form, text='Personal Details.').place(x=5, y=50)
name1=Label(form, text='First Name:').place(x=5, y=90)
e1=Entry(form,textvariable=fName).place(x=130, y=90)
name2=Label(form, text='Last Name:').place(x=5, y=130)
e2=Entry(form,textvariable=lName).place(x=130, y=130)
Addres=Label(form, text='Address: ').place(x=5, y=170)
e3=Entry(form,textvariable=Address).place(x=130, y=170)
eml=Label(form,text='E-mail_ID:').place(x=5, y=210)
e4=Entry(form,textvariable=email).place(x=130, y=210)
phb=Label(form,text='PH Number:').place(x=5, y=250)
e4=Entry(form,textvariable=phnb).place(x=130, y=250)
d1=Label(form,text='DOB:').place(x=5, y=290)
e4=Entry(form,textvariable=dob).place(x=130, y=290)


radio= IntVar()
genter=Label(form, text='GENDER').place(x=10, y=340)
mal=Radiobutton(form, text='Male',variable=radio, value=1).place(x=10, y=380)
femal=Radiobutton(form, text='Female',variable=radio, value=2,).place(x=10, y=420)
othe=Radiobutton(form, text='Others',variable=radio, value=3).place(x=10, y=460)



sslc=IntVar()
sslc1=StringVar()
plus_two=IntVar()
plus_two1=StringVar()
graduate=IntVar()
graduate1=StringVar()
grad=StringVar()
grad.set('SELECET ANY')
quali=Label(form, text='Qulification').place(x=10, y=500)
qual1=Checkbutton(form, text='SSLC', variable=sslc, onvalue=1, offvalue=0,).place(x=10, y=540)
qual2=Checkbutton(form, text='PLUS TWO',variable=plus_two, onvalue=1, offvalue=0).place(x=120, y=540)
qual3=Checkbutton(form, text='Graduated',variable=graduate, onvalue=1, offvalue=0).place(x=10, y=580)
qual_3=OptionMenu(form, grad, 'None','Mechanical Engg','Civil Engg', 'Electrical Engg').place(x=120, y=580)

sbbtn=Button(form, text='Submit', bg='blue', fg='white', activeforeground='black', activebackground='yellow', command=sbmt).place(x=130, y=660)

form.mainloop()