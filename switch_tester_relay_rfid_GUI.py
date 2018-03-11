import RPi.GPIO. as GPIO
import time
import SimpleMFRC522
import tkinter import *
import pygame
import functools import partial

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        

        #Chip sensors
        
        #Sound setup
        pygame.init()
        pygame.mixer.init()
        self.alter = pygame.mixer.Sound('put-staff-in-altar_temp.wav')

        self.create_widgets()
        self.ChipCheck()
        
        
    def create_widgets(self):
        #labels

        #buttons
        pass
        
    def ChipCheck(self):

        self.after(250, self.ChipCheck)

#main
root = Tk()
root.title("RFID Switch")
root.geometry('500x500')

app = Application(root)
root.mainloop()
