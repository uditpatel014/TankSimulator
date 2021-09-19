import tkinter as tk
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP) # start switch to gnd
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP) # stop switch to gnd
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) # lap switch to gnd
GPIO.setup(6,  GPIO.IN, pull_up_down=GPIO.PUD_UP) # reset switch to gnd
 
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.nglabel = tk.Label(self, text="00:00:00.00", width="12", relief="sunken")
        self.nglabel.config(font=('times', 32, 'bold'))
        self.nglabel.pack(side="top")
        self.ngbtstart = tk.Button(self, text="Start", command=self.ngstart )
        self.ngbtstart.pack(side="left")
        self.ngbtlap = tk.Button(self, text="Lap", command=self.nglap )
        self.ngbtlap.pack(side="left")
        self.ngbtstop = tk.Button(self, text="Stop", command=self.ngstop )
        self.ngbtstop.pack(side="left")
        self.ngbtreset = tk.Button(self, text="Reset", command=self.ngreset )
        self.ngbtreset.pack(side="left")
        self.quit = tk.Button(self, text="Quit", command=root.destroy)
        self.quit.pack(side="right")
        self.start_time = time.time()
        self.update_timeText()

    def ngstart(self):
        global state
        if state==0:
          self.start_time = time.time()
          self.after(0, self.update_timeText)
          state=1

    def ngstop(self):
        global state
        state = 0
        self.nglabel.config(fg = "black")

    def nglap(self):
        global state,count
        if state == 1:  
            state = 2
            count = 1

    def ngreset(self):
        global state,t
        state = 0
        self.nglabel.config(fg = "black")
        self.nglabel["text"]="00:00:00.00"

    def update_timeText(self):
        global state,count,t
        if GPIO.input(26) == 0:
            self.ngstart()
        if GPIO.input(6) == 0:
            self.ngreset()
        if state > 0:
          now = time.time() - self.start_time
          m,s = divmod(now,60)
          h,m = divmod(m,60)
          ss = (now - int(now)) *100
          if state == 1:
              self.nglabel.config(fg = "black")
              self.nglabel["text"]="%02i:%02i:%02i.%02i" % (h,m,s,ss)
          else:
              self.nglabel.config(fg = "red")
          if GPIO.input(19) == 0:
              self.ngstop()
          elif GPIO.input(13) == 0:
              self.nglap()
          if count > 0:
              count +=1
              if count > 500: # defines length of time the lap time appears
                  state = 1
                  count = 0
        self.after(10, self.update_timeText)

state=0
count=0
root = tk.Tk()
app = Application(master=root)
app.master.title("Timer in 100th sec")
app.mainloop()