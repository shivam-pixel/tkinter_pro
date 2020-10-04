from tkinter import *
import calendar
root=Tk()
root.title("calendar")
root.geometry("240x200")
root.resizable(0,0)
def show():
    a=int(spin.get())
    b=int(spin1.get())
    cal=calendar.month(b,a) #pass here your year and then month values
    txt.delete(0.0,END)
    txt.insert(INSERT,cal)
lb1=Label(root,text="month",font=('arial',9,'bold'),bg="red").place(x=15,y=0)
lb1=Label(root,text="year",font=('arial',9,'bold'),bg="green").place(x=113,y=0)
#create spinbox
spin=Spinbox(root,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4)
spin.place(x=60,y=0)
spin1=Spinbox(root,from_=1999,to=2100,width=4)
spin1.place(x=150,y=0)
#create button
btn=Button(root,text="show",font=('arial',9,'bold'),command=show,bg="yellow").place(x=100,y=30)
#textbox creation to display calendar
txt=Text(root,width=24,height=8)
txt.place(x=20,y=57)
root.mainloop()
