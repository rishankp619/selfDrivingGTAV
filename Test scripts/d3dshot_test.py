import d3dshot
import time
import cv2
import numpy
import pyautogui

d = d3dshot.create(capture_output="numpy")

while True:
  last_time = time.time()
  # img = d.screenshot(region = (0,40,800,640))
  image = pyautogui.screenshot(bbox = (0, 40, 800, 640))
  img = numpy.array(image)
  # d.capture(target_fps = 10)
  # img = d.get_latest_frame()
  # print(img)
  cv2.imshow("window", img)
  print("FPS: ", round(1/(time.time()-last_time), 0))
  cv2.waitKey(1)