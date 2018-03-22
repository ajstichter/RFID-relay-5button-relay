#!/usr/bin/env python 2.7

#Not sure if the "python 2.7" works, but we need to designate that it needs to open in python version 2.7 esp if it's opening it at startup.

import RPi.GPIO as GPIO
import time
import SimpleMFRC522
from tkinter import *
#instead of tkinter, this should probably be Tkinter? This is specifically for Python 2.7
#https://www.pythoncentral.io/introduction-to-pythons-tkinter/
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
        self.reader = SimpleMFRC522.SimpleMFRC522()
        
        #Sound setup
        pygame.init()
        pygame.mixer.init()
        self.altar = pygame.mixer.Sound('put-staff-in-altar_temp.wav')
        self.error = pygame.mixer.Sound('failure-short_temp.wav')

        self.create_widgets()
        self.ChipCheck()

        #Mag-lock setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(2, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        
        
        
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
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        GPIO.setup(2, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)

        GPIO.setup(23, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(27, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(22, GPIO.IN, GPIO.PUD_UP)

        loop = '1'
        button1 = GPIO.input(23)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)

        while loop == '1':
            num = ''
            id, text = reader.read()

            if id == 742561995189:
                 num = '1'
                 GPIO.output(2, GPIO.HIGH)
                 self.altar.Play()
                 time.sleep(1)
                 loop = '2'

        while loop == '2':
            input_one = GPIO.input(23)
            input_two = GPIO.input(17)
            input_three = GPIO.input(27)
            input_four = GPIO.input(22)
            time.sleep(.5)
            if input_one == False:
                self.altar.Play()
                GPIO.output(3, GPIO.HIGH)
                time.sleep(1)
                loop = '3'
            if input_two == False:
                self.error.Play()
                time.sleep(.5)
            if input_three == False:
                self.error.Play()
                time.sleep(.5)
            if input_four == False:
                self.error.Play()
                time.sleep(.5)
        while loop == '3':
            id, text = reader.read()
            print(id)
            print(text)

            if id == 552222697650:
                GPIO.output(2, GPIO.LOW)
                GPIO.output(3, GPIO.LOW)
                loop = '1'    

        
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
