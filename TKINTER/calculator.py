from tkinter import *

def total ():
 a = int(num1.get())
 b = int(num2.get())
 c = a+b
 tot.set(c)

def differ():
 a = int (num1.get())
 b = int (num2.get())
 d = a-b
 diff.set(d)

def multiplay():
 a = int (num1.get())
 b = int (num2.get())
 m = a*b
 mul.set(m)

def divide():
 a = int (num1.get())
 b = int (num2.get())
 q = a/b
 div.set(q) 
 
mgui=Tk()
mgui.geometry ('250x250')
mgui.config(background="yellow")
mgui.title('simple calculator')

label3=Label(mgui,text="Simple Calculator",background="black",foreground="white").grid(row=1,column=6)
label8=Label(mgui,text="    ",background="yellow").grid(row=2,column=6)

num1 = StringVar()
num2 = StringVar()
tot = StringVar() 
diff = StringVar()
mul = StringVar()
div = StringVar()
label8=Label(mgui,text="       ",background="yellow").grid(row=2,column=3)
label1=Label(mgui,text='Numl', fg='blue',bg='white').grid(row=3,column=4)
labe12=Label(mgui,text='Num2', fg='blue',bg='white').grid(row=4,column=4)


entry1=Entry (mgui,textvariable=num1).grid(row=3,column=6) 
entry2=Entry (mgui,textvariable=num2).grid(row=4,column=6)

entry3=Entry (mgui,textvariable=tot).grid(row=5,column=6) 
entry4=Entry (mgui,textvariable=diff).grid(row=6,column=6)
entry5=Entry (mgui,textvariable=mul).grid(row=7,column=6)
entry6=Entry (mgui,textvariable=div).grid(row=8,column=6)

button1=Button(mgui,text='SUM',fg='red',bg='white',command = total).grid(row=5,column=4)
button2=Button(mgui, text='diff',fg='red',bg='white',command = differ).grid(row=6,column=4)
button3=Button(mgui, text='mul',fg='red',bg='white',command = multiplay).grid(row=7,column=4)
button4=Button(mgui, text='div',fg='red',bg='white',command = divide).grid(row=8,column=4)



mgui.mainloop()