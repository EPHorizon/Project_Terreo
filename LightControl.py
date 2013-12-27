### Light Control V1 ###

import wiringpi2
import time
output = 1

redRight = 0
greenRight = 1
blueRight = 2
redLeft = 3
greenLeft = 4
blueLeft = 5
redFront = 6
greenFront = 7
blueFront = 8
wiringpi2.wiringPiSetup()
wiringpi2.pinMode(redRight,output)
wiringpi2.pinMode(blueRight,output)
wiringpi2.pinMode(greenRight,output)
wiringpi2.pinMode(redLeft,output)
wiringpi2.pinMode(blueLeft,output)
wiringpi2.pinMode(greenLeft,output)
wiringpi2.pinMode(redFront,output)
wiringpi2.pinMode(blueFront,output)
wiringpi2.pinMode(greenFront,output)


wiringpi2.softPwmCreate(redRight,0,100)
wiringpi2.softPwmCreate(blueRight,0,100)
wiringpi2.softPwmCreate(greenRight,0,100)
wiringpi2.softPwmCreate(redLeft,0,100)
wiringpi2.softPwmCreate(blueLeft,0,100)
wiringpi2.softPwmCreate(greenLeft,0,100)
wiringpi2.softPwmCreate(redFront,0,100)
wiringpi2.softPwmCreate(blueFront,0,100)
wiringpi2.softPwmCreate(greenFront,0,100)

def total(b):
    wiringpi2.softPwmWrite(redLeft,b)
    wiringpi2.softPwmWrite(greenLeft,b)
    wiringpi2.softPwmWrite(blueLeft,b)
    wiringpi2.softPwmWrite(redRight,b)
    wiringpi2.softPwmWrite(greenRight,b)
    wiringpi2.softPwmWrite(blueRight,b)
    wiringpi2.softPwmWrite(redFront,b)
    wiringpi2.softPwmWrite(greenFront,b)
    wiringpi2.softPwmWrite(blueFront,b)

index = 0
while True:
    queue = raw_input()
    if queue == "" and index == 0:
        wiringpi2.softPwmWrite(blueLeft,100)
        index +=1
    elif queue == "" and index == 1:
        total(0)
        index+=1
    elif queue == "" and index == 2:
        wiringpi2.softPwmWrite(greenLeft,100)
        wiringpi2.softPwmWrite(greenRight,100)
        wiringpi2.softPwmWrite(greenFront,100)
        wiringpi2.softPwmWrite(redLeft,100)
        wiringpi2.softPwmWrite(redRight,100)
        wiringpi2.softPwmWrite(redFront,100)
        index+=1
    elif queue == "" and index == 3:
        total(0)
        index+=1
    elif queue == "" and index == 4:
        wiringpi2.softPwmWrite(redLeft,100)
        wiringpi2.softPwmWrite(redRight,100)
        wiringpi2.softPwmWrite(redFront,100)
        index+=1
    elif queue == "" and index == 5:
        total(0)
        index+=1
    elif queue == "" and index == 6:
        for i in range(50):
            wiringpi2.delay(50)
            total(0)
            wiringpi2.delay(50)
            total(100)
        total(0)
        index+=1
    elif queue == "" and index == 7:
        wiringpi2.softPwmWrite(redRight,100)
        wiringpi2.softPwmWrite(greenRight,100)
        index +=1
    elif queue == "" and index == 8:
        total(0)
        index+=1
    elif queue == "" and index == 9:
        wiringpi2.softPwmWrite(redRight,100)
        wiringpi2.softPwmWrite(greenRight,100)
        index +=1
    elif queue == "" and index == 10:
        total(0)
        index+=1
    elif queue == "" and index == 11:
        wiringpi2.softPwmWrite(redRight,100)
        wiringpi2.softPwmWrite(greenRight,100)
        index +=1
    elif queue == "" and index == 12:
        total(0)
        index+=1
    elif queue == "" and index == 13:
        wiringpi2.softPwmWrite(redLeft,100)
        index+=1
    elif queue == "" and index == 14:
        total(0)
        index+=1
    elif queue == "" and index == 15:
        wiringpi2.softPwmWrite(redRight,100)
        wiringpi2.softPwmWrite(blueRight,100)
        index +=1
    elif queue == "" and index == 16:
        for i in range(75):
            wiringpi2.delay(50)
            wiringpi2.softPwmWrite(redRight,0)
            wiringpi2.softPwmWrite(blueRight,0)
            wiringpi2.delay(50)
            wiringpi2.softPwmWrite(redRight,100)
            wiringpi2.softPwmWrite(blueRight,100)
        total(0)
        index+=1
    elif queue == "" and index == 17:
        wiringpi2.softPwmWrite(redRight,100)
        wiringpi2.softPwmWrite(redLeft,100)
        wiringpi2.softPwmWrite(redFront,100)
        index+=1
    elif queue == "" and index == 18:
        total(0)
        index+=1
    elif queue == "" and index == 19:
        wiringpi2.softPwmWrite(redRight,100)
        wiringpi2.softPwmWrite(redLeft,100)
        wiringpi2.softPwmWrite(redFront,100)
        index+=1
##    elif queue == "" and index == 20:
##        wiringpi2.softPwmWrite(greenRight,0)
##        wiringpi2.softPwmWrite(greenFront,0)
##        index+=1
    elif queue == "" and index == 20:
        total(0)
        index+=1
    elif queue == "" and index == 21:
        wiringpi2.softPwmWrite(redLeft,100)
        index +=1
    elif queue == "" and index == 22:
        wiringpi2.softPwmWrite(redLeft,0)
        wiringpi2.softPwmWrite(blueRight,100)
        index +=1
    elif queue == "" and index == 23:
        total(0)
        index +=1
    elif queue == "" and index == 24:
        wiringpi2.softPwmWrite(blueRight,100)
        index +=1
    elif queue == "" and index == 25:
        total(0)
        index+=1
    elif queue == "" and index == 26:
        wiringpi2.softPwmWrite(greenLeft,100)
        index +=1
##    elif queue == "" and index == 27:
##        total(0)
##        index+=1
    elif queue == "" and index == 27:
        wiringpi2.softPwmWrite(redRight,100)
        index +=1
    elif queue == "" and index == 28:
        wiringpi2.softPwmWrite(greenLeft,0)
        wiringpi2.softPwmWrite(redLeft,100)
        wiringpi2.softPwmWrite(redFront,100)
        index +=1
    else:
        False
        total(0)
        break
    print index

