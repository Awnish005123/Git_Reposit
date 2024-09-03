# https://github.com/computervisioneng/sign-language-detector-python
# https://www.youtube.com/watch?v=MJCSjXepaAM&t=1192s
# dir is used to find the attributes of objects 
# To enter Python interpeter - python
# To Exit Python shell press - exit()

import os
import pickle
import mediapipe as mp
import cv2
import matplotlib.pyplot as plt
import pandas as pd

mp_hands = mp.solutions.hands # It is used to detect the handlandmarks(like fingers, palm,etc)
mp_drawing = mp.solutions.drawing_utils #  It is used to dectect dots on the detected landmarks(like fingers, palm,etc) 
                                        # and lines to indicate the connections.
mp_drawing_styles = mp.solutions.drawing_styles #  is used to apply a specific style to the drawing.

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3) # this line creates the instance of the
                                                                             # module to detect landmarks in images.

DATA_DIR = r'C:\Users\Admin\OneDrive - University at Buffalo\Documents\2. Projects\My Projects\SL_Recog\Collect_images'

data = []
labels = []
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):

        data_aux = []
        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
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

symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Hello', 'I', 'J', 'Thumbsup']

# Create a dictionary that maps each symbol to its index
symbol_dict = {sym: i for i, sym in enumerate(symbols)}

Labels_num = []

# Iterate over each item in data and append the corresponding index to Labels_num
for a in labels:
    if a in symbol_dict.keys():
        Labels_num.append(symbol_dict[a])

f = open('dataset.pickle', 'wb') # wb stands for write binary.
pickle.dump({'data': data, 'labels': Labels_num}, f)
f.close()

## Exploring the dataset. Not related to very relevant to the project.

# Open the file in binary read mode
with open('dataset.pickle', 'rb') as f: # rb here is read binary.
    # Load the data from the file
    dataset = pickle.load(f)

df = pd.DataFrame()
for key,values in dataset.items():
    df[key] = values

# Print the data to see its contents
print(df.head(10))

# one row comprises a single list, it will give csv in which the list fits in one cell.
df.to_csv('sl_dataset.csv',index=False )

# Create a DataFrame where each element in the list becomes its own column
df_features = pd.DataFrame(df['data'].tolist(), index=df.index) # index will add index to col.
print(df_features.head(10))

# Concatenate the new DataFrame with the output column
df_final = pd.concat([df_features, df['labels']], axis=1)

# Print the data to see its contents
print(df_final.head(10))

# one row comprises a single list, it will give csv in which the list fits in one cell.
df.to_csv('sl_dataset_final.csv',index=False )

