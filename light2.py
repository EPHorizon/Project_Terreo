import wiringpi2
import time
output = 1

pin0 = 0
pin1 = 1
pin2 = 2
pin3 = 3
pin4 = 4
pin5 = 5
pin6 = 6
pin7 = 7
pin8 = 8
wiringpi2.wiringPiSetup()
wiringpi2.pinMode(pin0,output)
wiringpi2.pinMode(pin1,output)
wiringpi2.pinMode(pin2,output)
wiringpi2.pinMode(pin3,output)
wiringpi2.pinMode(pin4,output)
wiringpi2.pinMode(pin5,output)
wiringpi2.pinMode(pin6,output)
wiringpi2.pinMode(pin7,output)
wiringpi2.pinMode(pin8,output)


wiringpi2.softPwmCreate(pin0,0,100)
wiringpi2.softPwmCreate(pin1,0,100)
wiringpi2.softPwmCreate(pin2,0,100)
wiringpi2.softPwmCreate(pin3,0,100)
wiringpi2.softPwmCreate(pin4,0,100)
wiringpi2.softPwmCreate(pin5,0,100)
wiringpi2.softPwmCreate(pin6,0,100)
wiringpi2.softPwmCreate(pin7,0,100)
wiringpi2.softPwmCreate(pin8,0,100)

while True:
    color = raw_input("Please enter a color: ")
    if color == "blue":
        myChar = raw_input("Please enter a number between 0 and 100: ")
        for brightness in range(int(myChar)):
            wiringpi2.softPwmWrite(pin1,brightness)
            wiringpi2.softPwmWrite(pin4,brightness)
            wiringpi2.softPwmWrite(pin7,brightness)
    elif color == "green":
        myChar = raw_input("Please enter a number between 0 and 100: ")
        for brightness in range(int(myChar)):
            wiringpi2.softPwmWrite(pin2,brightness)
            wiringpi2.softPwmWrite(pin5,brightness)
            wiringpi2.softPwmWrite(pin8,brightness)
    elif color == "red":
        myChar = raw_input("Please enter a number between 0 and 100: ")
        for brightness in range(int(myChar)):
            wiringpi2.softPwmWrite(pin0,brightness)
            wiringpi2.softPwmWrite(pin3,brightness)
            wiringpi2.softPwmWrite(pin6,brightness)
    elif color == "green blue" or "blue green":
        myChar = raw_input("Please enter a number between 0 and 100: ")
        for brightness in range(int(myChar)):
            wiringpi2.softPwmWrite(pin1,brightness)
            wiringpi2.softPwmWrite(pin4,brightness)
            wiringpi2.softPwmWrite(pin7,brightness)
            wiringpi2.softPwmWrite(pin2,brightness)
            wiringpi2.softPwmWrite(pin5,brightness)
            wiringpi2.softPwmWrite(pin8,brightness)
    elif color == "green red" or "red green":
        myChar = raw_input("Please enter a number between 0 and 100: ")
        for brightness in range(int(myChar)):
            wiringpi2.softPwmWrite(pin0,brightness)
            wiringpi2.softPwmWrite(pin3,brightness)
            wiringpi2.softPwmWrite(pin6,brightness)
            wiringpi2.softPwmWrite(pin2,brightness)
            wiringpi2.softPwmWrite(pin5,brightness)
            wiringpi2.softPwmWrite(pin8,brightness)
    elif color == "red blue" or "blue red":
        myChar = raw_input("Please enter a number between 0 and 100: ")
        for brightness in range(int(myChar)):
            wiringpi2.softPwmWrite(pin1,brightness)
            wiringpi2.softPwmWrite(pin4,brightness)
            wiringpi2.softPwmWrite(pin7,brightness)
            wiringpi2.softPwmWrite(pin0,brightness)
            wiringpi2.softPwmWrite(pin3,brightness)
            wiringpi2.softPwmWrite(pin6,brightness)
    
    elif color == "all":
        myChar = raw_input("Please enter a number between 0 and 100: ")
        for brightness in range(int(myChar)):
            wiringpi2.softPwmWrite(pin1,brightness)
            wiringpi2.softPwmWrite(pin4,brightness)
            wiringpi2.softPwmWrite(pin7,brightness)
            wiringpi2.softPwmWrite(pin0,brightness)
            wiringpi2.softPwmWrite(pin3,brightness)
            wiringpi2.softPwmWrite(pin6,brightness)
            wiringpi2.softPwmWrite(pin2,brightness)
            wiringpi2.softPwmWrite(pin5,brightness)
            wiringpi2.softPwmWrite(pin8,brightness)
            




















##wiringpi2.softPwmWrite(pin_to_pwm,0)
##for x in range(25):
##    wiringpi2.delay(20)
##    wiringpi2.softPwmWrite(pin_to_pwm,100)
##    wiringpi2.delay(20)
##    wiringpi2.softPwmWrite(pin_to_pwm,0)
##    
