from tkinter import *
from tkinter.messagebox import showinfo


def about():
   label3=Label(root, text="Total Calories Burnt :", bg="#33BBFF", font=("Latin",10,"bold"))
   label3.grid(row=9,column=0)
   entry2=Entry(root, textvariable=result,font=("Latin",10,"bold"))
   entry2.grid(row=9, column=1)
   
   res=(float(entry1.get())*float(0.045))
   result.set(res)
   
   lblheart=Label(root, text="Maximum Heart Points :", bg="#33BBFF", font=("Latin",10,"bold"))
   lblheart.grid(row=10,column=0)
   heartpts=Entry(root, textvariable=heart,font=("Latin",10,"bold"))
   heartpts.grid(row=10, column=1)
   
   res1=(float(entry3.get())*float(0.685))
   res2=(float(205.8)-res1)
   heart.set(res2)
   
   lblsqt=Label(root,text="Calories burnt from squates :", bg="#33BBFF", font=("Latin",10,"bold"))
   lblsqt.grid(row=11,column=0)
   heartpts=Entry(root, textvariable=sqtres,font=("Latin",10,"bold"))
   heartpts.grid(row=11, column=1)
   sqt=(float(entry5.get())*float(0.32))
   sqtres.set(sqt)
   
   lblpush=Label(root,text="Calories burnt from One Pushup :", bg="#33BBFF", font=("Latin",10,"bold"))
   lblpush.grid(row=12,column=0)
   entpush=Entry(root, textvariable=pushres,font=("Latin",10,"bold"))
   entpush.grid(row=12, column=1)
   push=(float(entry6.get())*float(0.34))
   pushres.set(push)
   
def button_clear():
   entry1.delete(0, END)
   entry3.delete(0, END)
   entry5.delete(0, END)
   entry6.delete(0, END)
   
   
root = Tk()
result=StringVar();
heart=StringVar();
sqtres=StringVar();
pushres=StringVar();

root.title('Health Tracker')
root.geometry('500x500')
root.iconbitmap("icon.ico")
root.config(bg="#33BBFF")   
   
label1=Label(root, text='HEALTH TRACKER',bg="#33BBFF", font=("Latin",25,"bold"), fg="#FFA833")
label1.grid(row=0, column=1)
label2=Label(root, text='Good Health is the best way live life in happiness', bg="#33BBFF", font=("Latin",10,"italic"))
label2.grid(row=1, column=1)
label3=Label(root, text="Enter Steps :", bg="#33BBFF",font=("Latin",10,"bold"))
label3.grid(row=3,column=0)
label4=Label(root, text="Enter Age :", bg="#33BBFF",font=("Latin",10,"bold"))
label4.grid(row=4,column=0)
label5=Label(root, text="Total number of squates :", bg="#33BBFF",font=("Latin",10,"bold"))
label5.grid(row=5,column=0)
label6=Label(root, text="Total number of pushup :", bg="#33BBFF",font=("Latin",10,"bold"))
label6.grid(row=6,column=0)
entry5=Entry(root,font=("Latin",10,"bold"))
entry5.grid(row=5,column=1)
entry3=Entry(root,font=("Latin",10,"bold"))
entry3.grid(row=4,column=1)
entry1=Entry(root,font=("Latin",10,"bold"))
entry1.grid(row=3,column=1)
entry6=Entry(root,font=("Latin",10,"bold"))
entry6.grid(row=6,column=1)


button1=Button(root, text="TRACK YOUR HEALTH",command=about, borderwidth=2,font=("Latin",10,"bold"))
button1.grid(row=7, column=1)
exitbutton=Button(root, text="EXIT", command=root.quit, bg="#33FF96")
exitbutton.grid(row=20, column=3)
button3=Button(root, text="Clear", command=button_clear, bg="#33FF96")
button3.grid(row=20, column=0)

root.mainloop()