import RPi.GPIO as GPIO
import time
import SimpleMFRC522
from tkinter import *
import pygame
from functools import partial

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        
        #vars
        self.soundOn = True
        self.locked = True

        #Chip sensors
        
        #Sound setup
        pygame.init()
        pygame.mixer.init()
        self.altar = pygame.mixer.Sound('put-staff-in-altar_temp.wav')

        self.create_widgets()
        self.ChipCheck()
        
        
    def create_widgets(self):
        #labels
        self.lblstat = Label(self, text = "RFID Status:")
        self.lblstat.grid()
        self.lblcor = Label(self, text = "Correct Switch: ")
        self.lblcor.grid()
        self.lblid = Label(self, text = "ID #")
        self.lblid.grid()
        

        #buttons
        self.bttnsound = Button(self, text = "Sound: On", command = self.ToggleSound)
        self.bttnsound.grid()
        self.bttnlock = Button(self, text = "Closed", command = self.ToggleLock)
        self.bttnlock.grid()
        self.bttnreset = Button(self, text = "Reset", command = self.Reset)
        self.bttnreset.grid()

        #number keys
        self.bttnum1 = Button(self, text = "1", command = partial(self.PressButton, "1"))
        self.bttnum1.grid()
        self.bttnum2 = Button(self, text = "2", command = partial(self.PressButton, "2"))
        self.bttnum2.grid()
        self.bttnum3 = Button(self, text = "3", command = partial(self.PressButton, "3"))
        self.bttnum3.grid()
        self.bttnum4 = Button(self, text = "4", command = partial(self.PressButton, "4"))
        self.bttnum4.grid()
        self.bttnum5 = Button(self, text = "5", command = partial(self.PressButton, "5"))
        self.bttnum5.grid()
        
    def ChipCheck(self):

        self.after(250, self.ChipCheck)
        
    def PressButton(self, val):
        pass

    def ToggleSound(self):
        if self.soundOn:
            self.soundOn = False
            self.bttnsound['text'] = "Sound: Off"
        else:
            self.soundOn = True
            self.bttnsound['text'] = "Sound: On"
            
    def Reset(self):
        pass

    def ToggleLock(self):
        if self.locked:
            self.locked = False
            self.bttnlock['text'] = "Opened"
        else:
            self.locked = True
            self.bttnlock['text'] = "Closed"
    

            

#main
root = Tk()
root.title("RFID Switch")
root.geometry('600x500')

app = Application(root)
root.mainloop()
