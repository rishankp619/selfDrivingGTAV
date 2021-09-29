import numpy as np
import cv2
import time
import os
import keras.models
import win32api as wapi
import d3dshot
from keras.models import load_model
import pyvjoy

# Adding TY to pause in a list of characters
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

# Load the model
model = load_model("E:/College Work/TY Project/models/steerRGBE50-50x40.h5")

# Intialise D3dshot
d3dshotObj = d3dshot.create(capture_output="numpy")
print("d3dshot Intialised")

# Initialse vJoy
vjoy = pyvjoy.VJoyDevice(1)
print("vJoy Intialised")
last_time = time.time()

# Countdown
for i in range(3):
        print("----PLAYING IN {}----".format(3-i))
        time.sleep(1)

play = True

x = 100
y = 50

while(True):
        keys = key_check()
        if 'T' in keys:
                if 'Y' in keys:
                        print("----PROGRAM EXITED----")
                        vjoy.reset_data()
                        vjoy.update()
                        import sys
                        sys.exit()
                if play:
                        play = False
                        print("----PAUSED----")
                        vjoy.data.wAxisX = 16384
                        vjoy.data.wAxisY= 1
                        vjoy.update()
                        time.sleep(1)
                else:
                        play = True
                        for i in range(3):
                                print("----PLAYING IN {}----".format(3-i))
                                time.sleep(1)
        if play:
                # Grab the screen
                screen = d3dshotObj.screenshot(region = (0,40,800,640))
                screen = cv2.resize(screen, (480, 270))
                screen = screen[x:x+132, y:y+400,:]
                screen = cv2.resize(screen, (200, 66))
                screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

                # cv2.imshow('img', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
                # cv2.imshow('img', screen)
                # if cv2.waitKey(25) & 0xFF == ord('q'):
                #         cv2.destroyAllWindows()
                #         break
                
                # Normalising the input
                screen = screen / 255.0

                # Pass the input to the model
                prediction = model.predict([screen.reshape(-1,200,66,3)])
                
                steering = prediction[0][0]
                throttle = prediction[0][1]/1.5
                steer_axis = int((steering+1)*32768/2)
                throttle_axis = int((throttle+1)*32768/2)

                # Send data to vJoy
                vjoy.data.wAxisX = steer_axis
                vjoy.data.wAxisY= throttle_axis
                vjoy.update()

                print(prediction, "FPS: ", round(1/(time.time()-last_time), 1))
                last_time = time.time()

vjoy.reset_data()
vjoy.update()