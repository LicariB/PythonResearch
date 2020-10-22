import RPi.GPIO as GPIO #import the different libraries
import time
from time import sleep
import random
import numpy
import pygame
pygame.mixer.init()  #program to control the speaker
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pygame.mixer.music.load("Misc/start.mp3")

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #tell the Raspberry-Pi where the button, buzzer 
GPIO.setup(12, GPIO.OUT)                            #and light are on the circuit board.
GPIO.setup(22, GPIO.OUT) 
my_times=[]
fast_times=[]
print("---------------------------------")
print("DIRECTIONS: Input either light or audio and the number of rounds when prompted. Then listen for the round start voice; it will play before every round. Press the button when you see the light or hear the buzzer")

j=0

def my_callback(channel): #have the Raspberry-Pi continuously check if the button is pressed.
	global j               #if it is, then record the time between the light coming on or the
	while j<1:             #buzzer sounding and the button being pushed.  Since the program captures  
		z=time.time()         #more than 1 reaction time, then the program records the first reaction
		print("Button detected")  #time listed
		reaction=(z-x)
		reaction=round(reaction, 3)
		my_times.append(reaction)
		fast_times.append(my_times[0]) #my_times records several inputs from the duration of the button push but we need only the first one since that represents the moment the button was pushed
		my_times.clear() #after the first time was put into the new fast_times list, the rest of my_times is cleared and ready for the next round
		j=j+1

	
y=str(input("Please enter whether you want to run the program with light as the reaction test (light)\
 or audio as reation test (audio).")) #check to see if the user want the light coming on as the indicator
y=y.upper()                             #or the buzzer
if y=="LIGHT": #if the answer is the light, then follow the procedure below
	
	x=int(input("Please enter the number of rounds that you would like to perform."))
    #asks the user how many rounds they want to do
		
	GPIO.add_event_detect(11, GPIO.RISING, callback=my_callback) #completes the continuous checking
                                                                    #for the button
	for i in range(x):
		i=i+1
		print("This is the start of round: " + str(i)) 
		pygame.mixer.music.play() #plays audio file over the speaker signaling the start of the round
		time.sleep(random.randint(5,10)) #randomizes when the light appears so that test takers cannot predict when it will turn on
		GPIO.output(12,1)
		x=time.time()         #turns the lights on for the number of rounds specified
		time.sleep(1)
		GPIO.output(12,0)
		print(fast_times)
		time.sleep(3)
		j=j-1
		

		


	average=numpy.mean(fast_times)
	average=round(average, 3)      #computes the average of the recorded reaction times after all of
	print("This is your average reaction time: ", average, "| All times:", fast_times) #the rounds are completed
	pygame.mixer.music.load("Misc/complete.mp3")
	pygame.mixer.music.play()
	time.sleep(3)
	GPIO.cleanup()
elif y=="AUDIO": 
	x=int(input("Please enter the number of rounds that you would like to perform."))
    #if the answer is the buzzer, then the same procedure as above happens, only with the buzzer
    #instead of the light
	GPIO.add_event_detect(11, GPIO.RISING, callback=my_callback)
    #all comments from the light section apply to the audio section as well
	for i in range(x):
		i=i+1
		print("This is the start of round: " + str(i))
		pygame.mixer.music.play()
		time.sleep(random.randint(5,10))
		GPIO.output(22,1)
		x=time.time()
		time.sleep(1)
		GPIO.output(22,0)
		print(fast_times)
		time.sleep(3)
		j=j-1
		

		


	average=numpy.mean(fast_times)
	average=round(average, 3)
	print("This is your average reaction time: ", average, "| All times:", fast_times)
	pygame.mixer.music.load("Misc/complete.mp3")
	pygame.mixer.music.play()
	
	time.sleep(3)
	GPIO.cleanup()

