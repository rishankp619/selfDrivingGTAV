import cv2
import numpy as np
import math
import d3dshot
import time

classNames = []
with open('E:/College Work/TY Project/Object Detection/coco.names', 'r') as file:
  for line in file:
    classNames.append(line[:-1])
#print(classNames[2])


configPath = 'E:/College Work/TY Project/Object Detection/ssd_mobilenet_v3.pbtxt'
weightsPath = 'E:/College Work/TY Project/Object Detection/frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def detectObj(img):
  classIds, confs, bbox = net.detect(img, confThreshold = 0.6)
  # print(len(classIds))
  dist = []
  dist.append(0)
  for i in range(len(classIds)):
    classId = classIds[i][0]
    box = bbox[i]
    conf = confs[i]
    className = classNames[classId - 1]

    if className not in ['person', 'car', 'truck', 'motorcycle', 'bicycle']:
      continue
    
    dist.append(round(math.sqrt((box[0]-box[2])**2 + (box[1]-box[3])**2), 1))
    # print(classId, box, conf, dist)
    cv2.rectangle(img, box, color=(0, 0, 255), thickness=2)
    cv2.putText(img, className.upper() + ": " + str(dist[i-1]), (box[0], box[1] - 5), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1.5, color=(0, 0, 255), thickness=2)

  cv2.imshow('window', img)
  cv2.imshow('window', cv2.resize(img, (16*40, 9*40)))
  cv2.waitKey(1)
  # print("Dist : ", max(dist))
  # return max(dist)


# # Capturing screen and testing
# d = d3dshot.create(capture_output="numpy")

# while True:
#   last_time = time.time()
#   img = d.screenshot()
#   img = cv2.resize(img, (320, 320))
#   detectObj(img)
#   print("FPS: ", round(1/(time.time()-last_time), 0))

# Testing on data_set
train_data = np.load('E:/College Work/TY Project/training_data/td-35.npy', allow_pickle=True)
for data in train_data:
  last_time = time.time()
  img = data[0]
  # print(img.shape)
  img = cv2.resize(img, (320, 320))
  detectObj(img)
  print("FPS: ", round(1/(time.time()-last_time), 0))


# train_data = np.load('E:/College Work/TY Project/training_data/td-35.npy', allow_pickle=True)
# # train_data = np.load('E:/College Work/TY Project/trimmed_td/ttd-35.npy', allow_pickle=True)
# img = train_data[850][0]
# print(img.shape)
# # x = 100
# # y = 10
# # img = img[y:y+250, x:x+250, :]
# img = cv2.resize(img, (320, 320))
# detectObj(img)