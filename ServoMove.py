import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
servoPin1 = 12
servoPin2 = 8
GPIO.setup(servoPin1, GPIO.OUT)
GPIO.setup(servoPin2, GPIO.OUT)
pwm1 = GPIO.PWM(servoPin1, 50)
pwm2 = GPIO.PWM(servoPin2, 50)
pwm1.start(0)
pwm2.start(0)
leftPosCurrent = 0
leftPosNext = 1
rightPosCurrent = 0
rightPosNext = 1

while (1):
	tempForward = open('Forward', 'r')
	fileForward = int(tempForward.read())

	tempReverse = open('Reverse', 'r')
	fileReverse = int(tempReverse.read())

	tempLeft = open('Left', 'r')
	fileLeft = int(tempLeft.read())

	tempRight = open('Right', 'r')
	fileRight = int(tempRight.read())

	tempRoam = open('Roam', 'r')
	fileRoam = int(tempRoam.read())


	while(fileRight == 1):
		for i in range(rightPosCurrent, rightPosNext, 1):
			DC = ((1./18.) * i) + 2
			pwm1.ChangeDutyCycle(DC)
			pwm2.ChangeDutyCycle(DC)
			time.sleep(0.02)
		leftPosCurrent = leftPosNext
		rightPosCurrent = rightPosNext
		leftPosNext += 1
		rightPosNext += 1
		if rightPosCurrent == 360:
			rightPosCurrent = 0
			leftPosCurrent = 0
			rightPosNext = 1
			leftPosNext = 1
		tempRight = open('Right', 'r')
	        fileRight = int(tempRight.read())

	while(fileLeft == 1):
		for i in range(rightPosNext, rightPosCurrent, -1):
			DC = ((1./18.) * i) + 2
			pwm1.ChangeDutyCycle(DC)
			pwm2.ChangeDutyCycle(DC)
			time.sleep(0.02)
		rightPosNext = rightPosCurrent
		leftPosNext = leftPosCurrent
		rightPosCurrent -= 1
		leftPosCurrent -= 1
		if rightPosNext == 0:
			leftPosCurrent = 359
			rightPosCurrent = 359
			leftPosNext = 360
			rightPosNext = 360 
		tempLeft = open('Left', 'r')
	        fileLeft = int(tempLeft.read())

	while(fileReverse == 1):
		for i in range(rightPosCurrent, rightPosNext, 1):
			DC = ((1./18.) * i) + 2
			pwm1.ChangeDutyCycle(DC)
			time.sleep(0.02)
		rightPosCurrent = rightPosNext
		rightPosNext += 1
		if rightPosCurrent == 360:
			rightPosCurrent = 0
			rightPosNext = 1
		for i in range(leftPosNext, leftPosCurrent, -1):
			DC = ((1./18.) * i) + 2
			pwm2.ChangeDutyCycle(DC)
			time.sleep(0.02)
		leftPosNext = leftPosCurrent
		leftPosCurrent -= 1
		if leftPosNext == 0:
			leftPosNext = 360
			leftPosCurrent = 359
		tempReverse = open('Reverse', 'r')
        	fileReverse = int(tempReverse.read())

	while(fileForward == 1):
		for i in range(rightPosNext, rightPosCurrent, -1):
			DC = ((1./18.) * i) + 2
			pwm1.ChangeDutyCycle(DC)
			time.sleep(0.02)
		rightPosNext = rightPosCurrent
		rightPosCurrent -= 1
		if rightPosNext == 0:
			rightPosNext = 360
			rightPosCurrent = 359
		for i in range(leftPosCurrent, leftPosNext, 1):
			DC = ((1./18.) * i) + 2
			pwm2.ChangeDutyCycle(DC)
			time.sleep(0.02)
		leftPosCurrent = leftPosNext
		leftPosNext += 1
		if leftPosCurrent == 360:
			leftPosCurrent = 0
			leftPosNext = 1
		tempForward = open('Forward', 'r')
        	fileForward = int(tempForward.read())

	while(fileRoam == 1):
		for j in range(0, 30, 1):
			for i in range(rightPosNext, rightPosCurrent, -1):
				DC = ((1./18.) * i) + 2
				pwm1.ChangeDutyCycle(DC)
				time.sleep(0.02)
			rightPosNext = rightPosCurrent
			rightPosCurrent -= 1
			if rightPosNext == 0:
				rightPosNext = 360
				rightPosCurrent = 359
			for i in range(leftPosCurrent, leftPosNext, 1):
				DC = ((1./18.) * i) + 2
				pwm2.ChangeDutyCycle(DC)
				time.sleep(0.02)
			leftPosCurrent = leftPosNext
			leftPosNext += 1
			if leftPosCurrent == 360:
				leftPosCurrent = 0
				leftPosNext = 1
		randValue = randrange(361, 720)
		for j in range(0, randValue, 1):
			for i in range(leftPosCurrent, leftPosNext, 1):
				DC = ((1./18.) * i) + 2)
				pwm1.ChangeDutyCycle(DC)
				pwm2.ChangeDutyCycle(DC)
				sleep.time(0.02)
			rightPosCurrent = rightPosNext
			leftPosCurrent = leftPosNext
			rightPosNext += 1
			leftPosNext += 1
			if rightPosCurrent == 360:
				rightPosCurrent = 0
				rightPosNext = 1
				leftPosCurrent 0
				leftPosNext = 1
		tempRoam = open('Roam', 'r')
		fileRoam = int(tempRoam.read())
	

pwm1.stop()
pwm2.stop()
GPIO.cleanup()
