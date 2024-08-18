# https://github.com/computervisioneng/sign-language-detector-python
# https://www.youtube.com/watch?v=MJCSjXepaAM&t=1192s

# dir is used to find the attributes of objects 

import os
import pickle

import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = r'C:\Users\Admin\OneDrive - University at Buffalo\Documents\2. Projects\My Projects\SL_Recog\Collect_images'

data = []
labels = []

for dir_ in os.listdir(DATA_DIR)[1]:
    for image in os.listdir(os.path.join(DATA_DIR,dir_))[2]:
        img = os.path.join(os.path.join(DATA_DIR,dir_,image))
        data_aux = []
        x_ = []
        y_ = []
        cv_img = cv2.imread(img)
        cv_img_rgb = cv2.cvtColor(cv_img,cv2.COLOR_BGR2RGB)
        result = hands.process(cv_img_rgb)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    
                    x_.append(x)
                    y_.append(y)
                print(len(result.multi_hand_landmarks))
                print(len(hand_landmarks.landmark))
                print(len(x_),len(y_))



                    

                        

'''
# To check the no. of hands = 2

for image in os.listdir(folder_path)[:10]:
    image = os.path.join(folder_path,image)
    img = cv2.imread(image)
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    # Process the image to find landmarks
    results = hands.process(img_rgb)
    if results.multi_hand_landmarks:
        print(f'yes, the no of hands are {len(results.multi_hand_landmarks)}')
# to check the no. of landmarks if the atleast a hand is present.        
'''
'''
for hand_landmarks in results.multi_hand_landmarks:
     for i, landmark in enumerate(hand_landmarks.landmark):
        print(f'Landmark {i} = {landmark}')
    total_landmarks = len(hand_landmarks.landmark)
    print(f"Total number of landmarks: {total_landmarks}")
'''
# Cleanup
hands.close()
'''
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    
                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            data.append(data_aux)
            labels.append(dir_)
                    
f = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()
'''
