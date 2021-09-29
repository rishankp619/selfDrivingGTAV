import numpy as np
import cv2
import time
import os
import win32api as wapi
import pygame
import d3dshot


# Adding TY to pause or exit in a list of characters
keylist = ["\b"]
for char in "TY":
        keylist.append(char)

def key_check():
        keys = []
        for key in keylist:
                # Determines weather a key is up or down at the time the function is called
                if wapi.GetAsyncKeyState(ord(key)):
                        keys.append(key)
        return keys


file_name = "training_data.npy"
training_data = []

# Intialise D3dshot
d3dshotObj = d3dshot.create(capture_output="numpy")
print("d3dshot Intialised")

# Initialize Pygame
pygame.init()

# Initialize the joysticks.
pygame.joystick.init()

if pygame.joystick.get_count() >= 1:
        play = True
else:   play = False

# Get first connected joystick
joystick = pygame.joystick.Joystick(0)
#Initialize the first joystick
joystick.init()

name = joystick.get_name()
print("Joystick connected: {}".format(name))

last_time = time.time()

for i in range(5):
        print("----PLAYING IN {}----".format(5-i))
        time.sleep(1)

# Training data number
tdno = 100
i = 1
while(True):
        if play:
                # Update axis values for every iteration of loop
                pygame.event.get()
                joystick = pygame.joystick.Joystick(0)
                joystick.init()

                screen = d3dshotObj.screenshot(region=(0,40,800,640))
                last_time = time.time()
                # Resize to something a bit more acceptable for a CNN
                screen = cv2.resize(screen, (480, 270))
                # Run a color convert:
                screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
                # Steering axis: Left Stick horizontal axis
                axis_0 = joystick.get_axis(0)
                # Throttle axis: Right Trigger
                axis_5 = joystick.get_axis(5)
                # [steering, throttle]
                output = [axis_0, axis_5]
                print(output)
                training_data.append([screen,output])

                if len(training_data) % 100 == 0:
                        file_name = "E:/College Work/TY Project/training_data/td-{}".format(tdno)
                        np.save(file_name, training_data)
                        print("Training data", tdno, "saved!")
                        training_data = []
                        tdno += 1
                
                time.sleep(0.05)
                print('FPS : {}'.format(1/(time.time()-last_time)))
                last_time = time.time()

        keys = key_check()
        if 'T' in keys:
                if 'Y' in keys:
                        print("----PROGRAM EXITED----")
                        import sys
                        sys.exit()
                if play:
                        play = False
                        print("----PAUSED----")
                        time.sleep(1)
                else:
                        play = True
                        for i in range(3):
                                print("----PLAYING IN {}----".format(3-i))
                                time.sleep(1)