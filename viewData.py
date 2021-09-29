import cv2
import numpy as np
# from objectDetect import detectObj

train_data = np.load('E:/College Work/TY Project/trimmed_td/ttd-36.npy', allow_pickle=True)
# train_data = np.load('E:/College Work/TY Project/training_data/td-50.npy', allow_pickle=True) # Data is in RGB, (270, 480, 3) i.e. 480x270x3
print("Train data: ", train_data.shape)
x=100
y=50
# x=118
# y=120
for data in train_data:
    # img = data[0][x:x+132, y:y+400,:]
    img = data[0]
    # # Working 12th May
    # img = data[0][60:260,:,:]
    img = cv2.resize(img, (400,122))
    # print(img.shape)


    # img = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)
    # img = img/255
    choice = data[1]
    # print(img.shape) #(270, 480, 3)
    # img = detectObj(cv2.resize(img[:,120:132+120,:], (320, 320)))
    # img = cv2.resize(img, (400,132))
    cv2.imshow('test', cv2.cvtColor(img, cv2.COLOR_YUV2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
      break
    # print(choice)