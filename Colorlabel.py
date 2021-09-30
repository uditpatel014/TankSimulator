from tkinter import *
import time
import tkinter.messagebox
from threading import Thread

m = Tk()
m.title("Color Labels")
m.configure(bg="powder blue")
m.resizable(width=False,height=False)
m.geometry("1920x1080")
sec = StringVar()
Entry(m, textvariable=sec, width = 3,justify='center',font = 'Helvetica 14').place(width=30,height=40,x=90, y=120)
sec.set('00')
mins= StringVar()
Entry(m, textvariable=mins, width = 3,justify='center',font = 'Helvetica 14').place(width=30,height=40,x=50, y=120)
mins.set("15")
hrs = StringVar()
Entry(m, textvariable=hrs, width = 3,justify='center',font = 'Helvetica 14').place(width=30,height=40,x=10, y=120)
hrs.set('00')

def gogreen():
    lab1.config(bg="Green")

def countdowntimer():
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
      m.update()
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('15')
         hrs.set('00')
      times -= 1

Fr1=Frame(m)
Fr2=Frame(m,pady=10)

#labels
lab1 = Label(Fr1, text="Tank_1", bg="Yellow", width=8,fg="Black", font=("none", 30, "bold"))
#lab4.grid(row=1,column=0,padx=10)
lab2 = Label(Fr1, text="Tank_2", bg="Black", width=8,fg="White", font=("none", 30, "bold"))
#lab2.grid(row=1,column=1,padx=10)
lab3 = Label(Fr1, text="Tank_3", bg="Blue", width=8,fg="Black", font=("none", 30, "bold"))
#lab3.grid(row=1,column=2,padx=10)

#Button
StrtBtn = Button(Fr2, text="START", bg="red", font=("none", 20), command = lambda:[gogreen(),countdowntimer()])
#StrtBtn.grid(row=2,column=1,padx=10)
ExtBtn = Button(Fr2, text="Exit",bg="red", font=("none", 20), command=m.destroy)
#ExtBtn.place(x=1750, y=850)

#pack
Fr1.pack()
Fr2.pack()
lab1.pack()
lab2.pack()
lab3.pack()
ExtBtn.pack()
StrtBtn.pack()

m.mainloop()