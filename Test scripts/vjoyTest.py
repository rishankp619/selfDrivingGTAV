import pyvjoy
import time

#Pythonic API, item-at-a-time
j = pyvjoy.VJoyDevice(1)
j.reset()
j.reset_buttons()

# j.data.wAxisY= 0x4000
# j.data.wAxisX= 0x4000
# j.data.lButtons = 1
# j.update()

while True:
  j.data
  j.data.lButtons = 1 
  j.data.wAxisX = 8192 #0x2000
  j.data.wAxisY= 29952 #0x7500
  j.update()

  time.sleep(1)
  j.data.wAxisY = 0x2000 
  j.data.wAxisX= 0x7500
  j.data.lButtons = 0
  j.update()
  time.sleep(1)
  print("playing")
  