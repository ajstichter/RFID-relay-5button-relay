# RFID-relay-5button-relay

Instructions for how to setup the RFID reader and test it are found here: https://pimylifeup.com/raspberry-pi-rfid-rc522/

This program runs as such:
1. The RFID reads the RFID card/chip ebedded in a statue. If the Chip's ID matches the stored ID then it triggers the first relay which unlocks the first maglock.
2. The staff then is placed in one of the holes (1-5, all with buttons attached, this may need to change depending on how many available slots we have on the RasPi's GPIO pins) and triggers either a failure sound (might allow for another try afterwards) or a success sound and triggering the relay which unlocks a 2nd maglock. 
3. The program then is ready to read a "reset" RFID tag's ID. When it does, it locks both maglocks again, allowing for the Game Masters to reset the puzzles. When this happens it loops back to 1. and is ready to read the statue's RFID tag.
This looping structure is shown in the file switch_tester_relay_rfid.py (and it works).

Files in Github RFID-relay-5button-relay:

.gitattributes - not sure what this does
Cleanup - I believe that it ends the program so that other items can use the GPIO pins, not super useful for us.
MFRC522 - needed to communicate with the RFID reader. Will not change contents of the file.
MFRC522.pyc - unknown but assume that it is similar with the file above
Read_RFID_example - this is an example read file. it shows how to Read a RFID card with code.
relay_rfid_fin_old - an old file similar to the final file.
SimpleMFRC522 - like MFRC522, we will not change it.
SimpleMFRC522.pyc - like MFRC522.pyc, we will not change it.
switch_tester_relay_rfid.py - this is the working file for how I (Adam) want the final puzzle to work. We'll need to add in support of 5 switches, but it has the basic while loop structure correct. 
Write_RFID_example.py - this is an example of how to write to a card. Most likely we will not ever have to use this code because we will use the RFID card's specific ID as the "Password" mechanism.
raspberry-pi-pinout - this is a handy tool to see what the pin numbers are for the Pi's GPIO, and what pins you can use for what purpose.

*Note: all these files must be run in Python 2.7. They will not run in Python 3.*

To Do:
Make runable file using the switch_tester_relay_rfid.py logic and the GUI_example.jpg
Adam will test when complete/working. 
