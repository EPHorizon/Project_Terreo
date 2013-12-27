# -*- coding: utf-8 -*-
#These are the keyboard mappings
#q = Go forward
#a = Stop going forward or back
#z = Go back
#1-4 denotes power in 25% increments

####Main body of code
import os
while True:
    MyChar = raw_input("Press a character:")
    print "You pressed: " + MyChar
    if MyChar == "q1":
        os.system('mono /home/pi/smc_linux/SmcCmd --speed 800 --resume')
        os.system('mono /home/pi/smc_linux/SmcCmd --speed 800 --resume')
        print "Forward 25%"
    elif MyChar == "q2":
        os.system('mono /home/pi/smc_linux/SmcCmd --speed 1400 --resume')
        os.system('mono /home/pi/smc_linux/SmcCmd --speed 1400 --resume')
        print "Forward 50%"
    elif MyChar == "q3":
        os.system('mono /home/pi/smc_linux/SmcCmd --speed 2400 --resume')
        os.system('mono /home/pi/smc_linux/SmcCmd --speed 2400 --resume')
        print "Forward 75%"
    elif MyChar == "q4":
        os.system('mono /home/pi/smc_linux/SmcCmd --speed 3200 --resume')
        os.system('mono /home/pi/smc_linux/SmcCmd --speed 3200 --resume')
        print "Forward 100%"
    elif MyChar == "a":
        os.system('mono /home/pi/smc_linux/SmcCmd --stop')
        print "Stop"
    elif MyChar == "z1":
        os.system('mono /home/pi/smc_linux/SmcCmd --speed -800 --resume')
        os.system('mono /home/pi/smc_linux/SmcCmd --speed -800 --resume')
        print "Reverse 25%"
    elif MyChar == "z2":
        os.system('mono /home/pi/smc_linux/SmcCmd --speed -1600 --resume')
        os.system('mono /home/pi/smc_linux/SmcCmd --speed -1600 --resume')
        print "Reverse 50%"
    elif MyChar == "z3":
        os.system('mono /home/pi/smc_linux/SmcCmd --speed -2400 --resume')
        os.system('mono /home/pi/smc_linux/SmcCmd --speed -2400 --resume')
        print "Reverse 75%"
    elif MyChar == "z4":
        os.system('mono /home/pi/smc_linux/SmcCmd --speed -3200 --resume')
        os.system('mono /home/pi/smc_linux/SmcCmd --speed -3200 --resume')
        print "Reverse 100%"
    elif MyChar =="help":
        print "Type q plus a number between 1 and 4 to advance the motor forward."
        print "Do the same with z to reverse the motor."
        print "Adding 1 denotes 25% power, 2 = 50%, 3 = 75%, and 4 =100%."
        print "Type a to stop the motors"
    else:
        print "Not a command"
