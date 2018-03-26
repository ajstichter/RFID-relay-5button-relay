#!/usr/bin/env python 2.7

import RPi.GPIO as GPIO
import time
import SimpleMFRC522
import pygame

pygame.init()
pygame.mixer.init()
chime = pygame.mixer.Sound('put-staff-in-altar_temp.wav')
failSnd = pygame.mixer.Sound('failure-short_temp.wav')
clickSnd = pygame.mixer.Sound('8_button_click_b.wav')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)
#setup another pin for the 2nd maglock
GPIO.setup(3, GPIO.OUT)

#the following GPIO setup is for a button which triggers when the staff is placed in the hole.
#GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, GPIO.PUD_UP)

reader = SimpleMFRC522.SimpleMFRC522()

#unlockcode = "bastet_unlock"
loop = '1'
button1 = GPIO.input(23)
GPIO.output(2, GPIO.HIGH)
GPIO.output(3, GPIO.HIGH)

while True:
    while loop == '1':
        num = ''
        id, text = reader.read()
        print(id)
        print(text)

        if id == 742561995189: #this is the id of the RFID Chip
        #if text == unlockcode:
            num = '1'
            print('ran id check' + str(num))
            GPIO.output(2, GPIO.LOW)
            print('output to gpio on')
            print('1st maglock unlocked')
            clickSnd.play()
            #sound happens for the unlocking of the alter - will send to you
            time.sleep(1)
            loop = '2'
            print('phase 2')

    #here's when we would ask for a signal from the button to detect if the staff has been inserted
    while loop == '2':
        input_one = GPIO.input(23)
        input_two = GPIO.input(17)
        input_three = GPIO.input(27)
        input_four = GPIO.input(22)
        time.sleep(.5)
        #if button1 == False:
        if input_one == False:
            #music plays
            GPIO.output(3, GPIO.LOW)
            print('output to gpio on')
            print('2nd maglock unlocked')
            time.sleep(1)
            chime.play()
            loop = '3'
            print('phase 3')
        if input_two == False:
            #error music plays
            print('WRONG BUTTON. You pressed 2')
            failSnd.play()
            time.sleep(.5)
        if input_three == False:
            #error music plays
            print('WRONG BUTTON. You pressed 3')
            failSnd.play()
            time.sleep(.5)
        if input_four == False:
            #error music plays
            print('WRONG BUTTON. You pressed 4')
            failSnd.play()
            time.sleep(.5)
            

    while loop == '3':
        id, text = reader.read()
        print(id)
        print(text)

        if id == 552222697650:
            clickSnd.play()
            time.sleep(1)
            clickSnd.play()
            time.sleep(1)
            clickSnd.play()
            time.sleep(1)
            
            GPIO.output(2, GPIO.HIGH)
            print('output to gpio off')
            print('1st maglock in lock position')

            GPIO.output(3, GPIO.HIGH)
            print('output to gpio off')
            print('2nd maglock in lock position')
            
            loop = '1'
            print('phase 1')
    #GPIO.cleanup()
