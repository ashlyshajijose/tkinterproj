from tkinter import *    
top = Tk()   
top.mainloop() 

from tkinter import *
W=Tk()
W.title('mygui')

W.geometry('500x500')
W.config(background="green")

l1=Label(W,text="hello",background="black",foreground="white")
l2=Label(W,text="python",background="yellow",foreground="black")


#l1.pack(side=BOTTOM)
#l2.pack(side=RIGHT)


#l1.grid(row=0,column=0)
#l2.grid(row=2,column=2)

l1.place(x=100,y=50)
l2.place(x=150,y=150)

W.mainloop()