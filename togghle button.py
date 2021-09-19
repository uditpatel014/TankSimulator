from tkinter import *
from threading import Thread
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN)

class check_button(Thread):

    def __init__(self, labelText):
        Thread.__init__(self)
        self.labelText = labelText
        self.b = False

    def checkloop(self):
        while True:
            if GPIO.input(16) == 1:
                if self.b == False :
                    self.labelText.set("on")
                    print ("on")
                    self.b = True
                else:
                    self.labelText.set("off")
                    print ("off")
                    self.b = False
                while GPIO.input(16) == 1: pass

mamdouh = Tk()
labelText1 = StringVar()
x1 = Label(mamdouh,textvariable=labelText1) 
x1.config(font=('Helvetica',25,'bold'))
x1.grid(row=0,column=0)
mamdouh.title("mamdouh") 
mamdouh.geometry('1200x700')

chk1 = check_button(labelText1)
c1 = Thread(target=chk1.checkloop)
c1.start()

mamdouh.mainloop()