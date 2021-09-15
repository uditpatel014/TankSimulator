from tkinter import *
import time
import tkinter.messagebox

root=Tk()
root.title("Tank Simulator")
root.configure(bg="powder blue")
root.resizable(width=False,height=False)
root.geometry("680x980")
sec = StringVar()
Entry(root, textvariable=sec, width = 3,justify='center',font = 'Helvetica 14').place(width=30,height=40,x=90, y=120)
sec.set('00')
mins= StringVar()
Entry(root, textvariable=mins, width = 3,justify='center',font = 'Helvetica 14').place(width=30,height=40,x=50, y=120)
mins.set("15")
hrs = StringVar()
Entry(root, textvariable=hrs, width = 3,justify='center',font = 'Helvetica 14').place(width=30,height=40,x=10, y=120)
hrs.set('00')


calc = Frame(root)
calc.grid()
# label_1=Label(root,width=20,height=2,font=('arial',30,'bold'),bd=4,text="Scientific Calculator",justify=CENTER).grid(row=0,column=4,columnspan=5)

tankName = ["Tank_1","Tank_2","Tank_3","Tank_4","Tank_5"]
tankLabel = []
for tnum, tname in enumerate(tankName):
    print(tankLabel.count("Tank_2"))
    label = Label(root,width=7,height=2,font=('arial',20,'bold'),bg="yellow",bd=5,text=("Tank_"+str(tnum+1))).grid(row=1,column=tnum,padx=3)
   
tankLabel.append(label)

# print(tankLabel.count(tank)+1)

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
      root.update()
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('15')
         hrs.set('00')
      times -= 1
Button(root, text='START', bd ='2', bg = 'IndianRed1',font =('Helvetica bold',10), command = countdowntimer).place(x=30, y=180)
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
