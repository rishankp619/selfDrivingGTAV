import cv2
import numpy as np

x=100
y=50
training_data = []
for i in range(1, 82):
    train_data = np.load('E:/College Work/TY Project/training_data/td-{}.npy'.format(i), allow_pickle=True)
    for data in train_data:
        img = data[0][x:x+132, y:y+400,:]
        img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
        img = cv2.resize(img, (200,66))
        #print(img.shape) #(270, 480, 3)
        choice = data[1]
        training_data.append([img, choice])
        # cv2.imshow('test', img)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break
        # print(choice)
    file_name = "E:/College Work/TY Project/trimmed_td/ttd-{}".format(i)
    np.save(file_name, training_data)
    print("Trimmed Training data", i, "saved!")
    training_data = []
