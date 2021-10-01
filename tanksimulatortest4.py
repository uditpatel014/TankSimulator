import tkinter as tk
from tkinter import *
import time
import tkinter.messagebox
import threading
# import RPi.GPIO as GPIO

root=Tk()
root.title("Tank Simulator")
root.configure(bg="powder blue")
root.resizable(width=False,height=False)
root.geometry("1920x1080")

def entrybox(l1,l2,l3,m1,min):
    sec = StringVar()
    Entry(root, textvariable=sec, width = 3,justify='center',font = 'Helvetica 14').place(width=30,height=40,x=l1, y=m1)
    sec.set('00')
    mins= StringVar()
    Entry(root, textvariable=mins, width = 3,justify='center',font = 'Helvetica 14').place(width=30,height=40,x=l2, y=m1)
    mins.set(min)
    hrs = StringVar()
    Entry(root, textvariable=hrs, width = 3,justify='center',font = 'Helvetica 14').place(width=30,height=40,x=l3, y=m1)
    hrs.set('00')

    time=[hrs,mins,sec]
    return time



e1=entrybox(80,50,20,120,15)
e2=entrybox(220,190,160,120,10)
e3=entrybox(360,330,300,120,5)


calc = Frame(root)
calc.grid()
# label_1=Label(root,width=20,height=2,font=('arial',30,'bold'),bd=4,text="Scientific Calculator",justify=CENTER).grid(row=0,column=4,columnspan=5)
#lab1 = Label(Fr1, text="Tank_1", bg="Yellow", width=8,fg="Black", font=("none", 30, "bold"))grid(row=1,column=0,padx=10)
t1 = Label(root,width=7,height=2,font=('arial',20,'bold'),bg="yellow",bd=5,text=("Tank_1"))
t1.grid(row=1,column=1,padx=10)
t2 = Label(root,width=7,height=2,font=('arial',20,'bold'),bg="yellow",bd=5,text=("Tank_2"))
t2.grid(row=1,column=2,padx=10)
t3 = Label(root,width=7,height=2,font=('arial',20,'bold'),bg="yellow",bd=5,text=("Tank_3"))
t3.grid(row=1,column=3,padx=10)

#tankName = ["Tank_1","Tank_2","Tank_3","Tank_4","Tank_5"]
#tankLabel = []
#for tnum, tname in enumerate(tankName):
    #label = Label(root,width=7,height=2,font=('arial',20,'bold'),bg="yellow",bd=5,text=("Tank_"+str(tnum+1))).grid(row=1,column=tnum,padx=10)
    #if (tname=="Tank_1"):
#tankLabel.append(label)

#print(tankLabel)

#Create Entry Widgets for HH MM SS
# sec = StringVar()
# Entry(win, textvariable=sec, width = 2, font = 'Helvetica 14').place(x=220, y=120)
# sec.set('00')
# mins= StringVar()
# Entry(win, textvariable = mins, width =2, font = 'Helvetica
# 14').place(x=180, y=120)
# mins.set('00')
# hrs= StringVar()
# Entry(win, textvariable = hrs, width =2, font = 'Helvetica 14').place(x=142, y=120)
# hrs.set('00')
# #Define the function for the timer
def countdowntimer(hrs,mins,sec):
   times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
   while times > -1:
      minute,second = (times // 60 , times % 60)
      hour =0
      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)
      #Update the time
      root.update()
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('15')
         hrs.set('00')
      times -= 1

def gogreen(t):
    print("here")
    t.config(bg="#00ff00")


# timer1 = threading.Thread(target=countdowntimer(e1[0],e1[1],e1[2])).start()
Startbutton = Button(root, text='START_1', bd ='2', bg = 'IndianRed1',font =('Helvetica bold',10), command = lambda:[gogreen(t1),threading.Thread(target=countdowntimer, args=(e1[0],e1[1],e1[2])).start()]).place(x=20, y=180)
Startbutton2 = Button(root, text='START_2', bd ='2', bg = 'IndianRed1',font =('Helvetica bold',10), command = lambda:[gogreen(t2),threading.Thread(target=countdowntimer, args=(e2[0],e2[1],e2[2])).start()]).place(x=160, y=180)
Startbutton3 = Button(root, text='START_3', bd ='2', bg = 'IndianRed1',font =('Helvetica bold',10), command = lambda:[gogreen(t3),threading.Thread(target=countdowntimer, args=(e3[0],e3[1],e3[2])).start()]).place(x=300, y=180)
Exitbutton = Button(root, text="Exit",bg="red", command=root.destroy).place(x=1750, y=0)

#pack
#t1.pack()
#t2.pack()
#t3.pack()
#Startbutton.pack()

# win.mainloop()

#========================================================================================================================================#

# def App():
#     Win_App=Tk()
#     Win_App.title("Life Apps Calculator")
#     Win_App.configure(bg="Orange")
#     Win_App.resizable(width=False,height=False)
#     Win_App.geometry("450x580")

#     life_inter = Frame(Win_App)

#     life=('BMI','AGE','Discount','Percent','Date','Length','Area','Volume','currency','Per-Loan','Split-Bill','GST')
#     i=0
#     life_btn=[]
#     for j in range(1,5):
#         for k in range(3):
#             life_btn.append(Button(Win_App,width=8,height=3,font=('arial',20,'bold'),bd=4,text=life[i]))
#             life_btn[i].grid(row=j,column=k,pady=2)
#             i+=1

# =========================================================================================================================================#

# menubar=Menu(root)


# root.configure(menu=menubar)
root.mainloop()