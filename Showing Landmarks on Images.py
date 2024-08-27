'''The Process of dectection is the landmark detection in which the hand 
    is identified and the gestures is predicted from the landmark.
    This is more robust and efficient process as compared 
    to taking the whole image and then performing classification.
'''

#### In this code we are just drawing land marks on the images and displaying them ####

# create Dataset
import mediapipe as mp
import cv2
import os
import matplotlib.pyplot as plt

# Detect and draw these landmarks at the top of the images.

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode = True,min_detection_confidence = 0.3)

Data_dir = r'C:\Users\Admin\OneDrive - University at Buffalo\Documents\2. Projects\My Projects\SL_Recog\Collect_images'
for dir_ in os.listdir(Data_dir)[:1]:
    for img_path in os.listdir(os.path.join(Data_dir,dir_))[:1]:# [:1] is used to plot for 1 image per dirctroy.
        img = cv2.imread(os.path.join( Data_dir, dir_, img_path ))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb) # it depicts the hand landmark.
        if results.multi_hand_landmarks: # here, multi_hand_landmarks are the attributes of results. 
                                        # if the one hand or two hands or more are detected then the landmarks will be drawn.
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    img_rgb, # image to draw.
                    hand_landmarks, # draw the landmarks on the images.
                    mp_hands.HAND_CONNECTIONS, # draw the connection between dots to form the figure, resembling to hands.
                    mp_drawing_styles.get_default_hand_landmarks_style(), #  This function provides the default style (like color, thickness) 
                                                                          #  for drawing the landmarks (the dots).
                    mp_drawing_styles.get_default_hand_connections_style()) # This function provides the default style for 
                                                                            # drawing the connections between landmarks (the lines). 
        plt.figure() # It's useful when you want to create multiple figures and need a fresh canvas for each one.
        plt.imshow(img_rgb)
plt.show()




