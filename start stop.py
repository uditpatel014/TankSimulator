import time
from Tkinter import *
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.IN)
GPIO.setup(38, GPIO.IN)

class ClockCount(Frame):
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        serial = spi(port=0, device=0, gpio=noop())
        device = max7219(serial, cascaded=1)
        global seg
        seg = sevensegment(device)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.counterh = 0
        self.countera = 0
        self.segh = "00"
        self.sega = "00"
        self.segt = "00"
        self.timestr = StringVar()
        self.ch = StringVar()
        self.ca = StringVar()
        self._check_gpio()
        self._update_counter()
        #if GPIO.input(40) == TRUE : print "test"

    def _update_counter(self):
        seg.text = str(self.segt)+str(self.segh)+str(self.sega)
        self.ch.set(str(self.counterh))
        self.ca.set(str(self.countera))

    def _check_gpio(self):
        if GPIO.input(40) == TRUE : print "test"
        if GPIO.input(40) == TRUE : self.Stop()

    def _update(self): 

        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
        seg.text = str(self.segt)+str(self.segh)+str(self.sega)
        if GPIO.input(40) == TRUE : print "test"
        if GPIO.input(40) == TRUE : self.Stop()
        if GPIO.input(38) == TRUE : self.Start()   

    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d' % (minutes, seconds))
        if len(str(minutes)) < 2 : self.segt = "0" + str(minutes)
        else: self.segt = str(minutes)

    def Start(self):                                                     
        """ Start the stopwatch, ignore if running. """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        

    def Stop(self):                                    
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0

    def Halbzeit(self):                                    
        """ Stop the stopwatch, ignore if stopped. """
        if not self._running: 
            self._start = time.time()         
            self._elapsedtime = 2700.00  
            self._setTime(self._elapsedtime)

    def Reset(self):                                  
        """ Reset the stopwatch. """
        if not self._running:
            self._start = time.time()         
            self._elapsedtime = 0.0    
            self._setTime(self._elapsedtime)

    def counth_up(self):
        self.counterh += 1
        if self.counterh > 99 : self.counterh = 0
        if len(str(self.counterh)) < 2 : self.segh = "0" + str(self.counterh)
        else: self.segh = str(self.counterh)
        self._update_counter()

    def counth_down(self):
        self.counterh -= 1
        if self.counterh < 0 : self.counterh = 0
        if len(str(self.counterh)) < 2 : self.segh = "0" + str(self.counterh)
        else: self.segh = str(self.counterh)
        self._update_counter()

    def counta_up(self):
        self.countera += 1
        if self.countera > 99 : self.countera = 0
        if len(str(self.countera)) < 2 : self.sega = "0" + str(self.countera)
        else: self.sega = str(self.countera)
        self._update_counter()

    def counta_down(self):
        self.countera -= 1
        if self.countera < 0 : self.countera = 0
        if len(str(self.countera)) < 2 : self.sega = "0" + str(self.countera)
        else: self.sega = str(self.countera)
        self._update_counter()

def main():
    root = Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()  
    """root.geometry("%dx%d+0+0" % (w, h))"""
    root.geometry('1000x1000')  
    clockcount = ClockCount(root)

    Button(root, font=('Arial',30), width=7, text='Start', command=clockcount.Start).place(x=120, y=200)
    Button(root, font=('Arial',30), width=7, text='Stop', command=clockcount.Stop).place(x=350, y=200)
    Button(root, font=('Arial',30), width=7, text='Halbzeit', command=clockcount.Halbzeit).place(x=580, y=200)  
    Button(root, font=('Arial',30), width=7, text='Reset', command=clockcount.Reset).place(x=810, y=200)
    Button(root, font=('Arial',30), width=7, text='Heim +', command=clockcount.counth_up).place(x=250, y=520)   
    Button(root, font=('Arial',30), width=7, text='Heim -', command=clockcount.counth_down).place(x=250, y=600)
    Button(root, font=('Arial',30), width=7, text='Gast +', command=clockcount.counta_up).place(x=550, y=520)   
    Button(root, font=('Arial',30), width=7, text='Gast -', command=clockcount.counta_down).place(x=550, y=600)
    Button(root, font=('Arial',30), width=7, text='Quit', command=root.destroy).place(x=10, y=10)
    clock_label = Label(root, font="Arial 100 bold", fg="RED", textvariable=clockcount.timestr).place(x=400, y=20)
    counterhome_label = Label(root, font="Arial 100 bold", fg="RED", textvariable=clockcount.ch).place(x=320, y=350)
    counteraway_label = Label(root, font="Arial 100 bold", fg="RED", textvariable=clockcount.ca).place(x=620, y=350)

    #if GPIO.input(40) == TRUE : clockcount.Start()
    #if GPIO.input(40) == TRUE : print "test"

    root.mainloop()


if __name__ == '__main__':
    main()