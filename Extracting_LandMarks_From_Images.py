# https://github.com/computervisioneng/sign-language-detector-python
# https://www.youtube.com/watch?v=MJCSjXepaAM&t=1192s
# dir is used to find the attributes of objects 

import os
import pickle

import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

mp_hands = mp.solutions.hands # It is used to detect the handlandmarks(like fingers, palm,etc)
mp_drawing = mp.solutions.drawing_utils #  It is used to dectect dots on the detected landmarks(like fingers, palm,etc) 
                                        # and lines to indicate the connections.
mp_drawing_styles = mp.solutions.drawing_styles #  is used to apply a specific style to the drawing.

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3) # this line creates the instance of the
                                                                             # module to detect landmarks in images.

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
        result = hands.process(cv_img_rgb) # .process() takes image as an input and processes it to detect hands
                                           # and their landmarks.
        if result.multi_hand_landmarks:    # this wil look if at least one hand is detected.
            for hand_landmarks in result.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y 
                    x_.append(x)
                    y_.append(y)
                print(len(result.multi_hand_landmarks))
                print(len(hand_landmarks.landmark))
                print(len(x_),len(y_))
# Cleanup
hands.close()
