#!/usr/bin/env python 2.7

import RPi.GPIO as GPIO
import time
import SimpleMFRC522
import pygame

pygame.init()
pygame.mixer.init()
chime = pygame.mixer.Sound('put-staff-in-altar_temp.wav')
failSnd = pygame.mixer.Sound('staff-fail_cat3.wav')
clickSnd = pygame.mixer.Sound('8_button_click_b.wav')
secondfailSnd = pygame.mixer.Sound('meow.wav')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#setup pins for the maglocks
GPIO.setup(2, GPIO.OUT)
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
staffloop = '0'
lastbutton = '0'
button1 = GPIO.input(23)
GPIO.output(2, GPIO.HIGH)
GPIO.output(3, GPIO.HIGH)

while True:
    while loop == '1':
        num = ''
        id, text = reader.read()
        print(id)
        print(text)

        if id == 742561995189 or id == 907954385802 or id == 24533234571: 
		#this is the id of the RFID Chip in the first and second (still gonna put it in) statues
        #if text == unlockcode:
            num = '1'
            print('ran id check' + str(num))
            GPIO.output(2, GPIO.LOW)
            print('output to gpio on')
            print('1st maglock unlocked')
            clickSnd.play()
            time.sleep(1)
            loop = '2'
            print('phase 2')

    #here's when we ask for a signal from the button to detect if the staff has been inserted
    while loop == '2':
        input_one = GPIO.input(27)
        input_two = GPIO.input(23)
        input_three = GPIO.input(17)
        input_four = GPIO.input(22)
        time.sleep(.5)
        #Leftmost = 1
        #1=27
        #2=23
        #3=17
        #4=22 - correct
        #if button1 == False:
        if input_four == False:
            chime.play()
            print('music playing')
            #music plays
            time.sleep(12.5)
            GPIO.output(3, GPIO.LOW)
            print('output to gpio on')
            print('2nd maglock unlocked')
            time.sleep(1)            
            loop = '3'
            print('phase 3')
        if input_two == False and lastbutton != '2':
            print('WRONG BUTTON. You pressed 2')
            if staffloop == '1':
                secondfailSnd.play()
                loop = '3'
                print('progressing to phase 3')
            if staffloop == '0':
                failSnd.play()
                staffloop = '1'
                lastbutton = '2'
            time.sleep(.5)
        if input_three == False and lastbutton != '3':
            print('WRONG BUTTON. You pressed 3')
            if staffloop == '1':
                secondfailSnd.play()
                loop = '3'
                print('progressing to phase 3')
            if staffloop == '0':
                failSnd.play()
                staffloop = '1'
                lastbutton = '3'
            time.sleep(.5)
        if input_one == False and lastbutton != '1':
            print('WRONG BUTTON. You pressed 1')
            if staffloop == '1':
                secondfailSnd.play()
                loop = '3'
                print('progressing to phase 3')
            if staffloop == '0':
                failSnd.play()
                staffloop = '1'
                lastbutton = '1'
            time.sleep(.5)
            

    while loop == '3':
        id, text = reader.read()
        print(id)
        print(text)

        if id == 552222697650 or id == 256092369827:
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
            staffloop = '0'
            lastbutton = '0'
            print('phase 1')
#GPIO.cleanup()
