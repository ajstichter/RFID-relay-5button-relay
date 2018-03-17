#!/usr/bin/env python 2.7

#Not sure if the "python 2.7" works, but we need to designate that it needs to open in python version 2.7 esp if it's opening it at startup.

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
        self.lblstat.grid(row = 0, column = 0)
        self.lblcor = Label(self, text = "Correct Switch: ")
        self.lblcor.grid(row = 2, column = 0)
        self.lblid = Label(self, text = "ID #")
        self.lblid.grid(row = 0, column = 2)
 
        #buttons
        self.bttnsound = Button(self, text = "Sound: On", command = self.ToggleSound)
        self.bttnsound.grid(row = 3, column = 0)
        self.bttnlock = Button(self, text = "Closed", command = self.ToggleLock)
        self.bttnlock.grid(row = 0, column = 1)
        self.bttnreset = Button(self, text = "Reset", command = self.Reset)
        self.bttnreset.grid(row = 3, column = 1)

        #number keys
        self.bttnum1 = Button(self, text = "1", command = partial(self.PressButton, "1"))
        self.bttnum1.grid(row = 1, column = 0)
        self.bttnum2 = Button(self, text = "2", command = partial(self.PressButton, "2"))
        self.bttnum2.grid(row = 1, column = 1)
        self.bttnum3 = Button(self, text = "3", command = partial(self.PressButton, "3"))
        self.bttnum3.grid(row = 1, column = 2)
        self.bttnum4 = Button(self, text = "4", command = partial(self.PressButton, "4"))
        self.bttnum4.grid(row = 1, column = 3)
        self.bttnum5 = Button(self, text = "5", command = partial(self.PressButton, "5"))
        self.bttnum5.grid(row = 1, column = 4)
        
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
