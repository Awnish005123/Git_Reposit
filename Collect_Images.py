# To look intothe current working directory---- os.getcwd()
# To change the current working directory ---- os.chdir(Dir_Path)
# Use regular Exp to avoid changing the slash ---- Dir_Path = r'Path\to\the\Dir'
# To enter into python enterpretor type in the terminal ---- python

import cv2
import os

# Change the Current Directory
Dir = r'C:\Users\Admin\OneDrive - University at Buffalo\Documents\2. Projects\My Projects\SL_Recog'
#os.chdir(Dir)

# Function to capture images
def capture_images(symbol):
    # Directory to save images
    save_dir = Dir + f'symbols/{symbol}/'
    if not os.path.exists(save_dir): # this line will check if the the path not exists, it will make a path.
        os.makedirs(save_dir)

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    # Counter for images captured
    image_count = 0

    while True:
        ret,frame = cap.read()  # here, ret is a boolean variable to check if the frame,captured or not.
        cv2.imshow('Capture', frame)
        print("Press 's' to save images.")

        key = cv2.waitKey(1) & 0xFF # cv2.waitKey(1), this ensures that the keys need to be pressed for one microsecends to
                                    # capture an image.'& 0xFF' part ensures compatibility across different systems, 
                                    # particularly with 64-bit systems. 

        # Press 'S' to save image
        if key == ord('s'):
            image_count += 1
            image_name = os.path.join(save_dir, f'{symbol}_{image_count}.jpg')
            cv2.imwrite(image_name, frame)
            print(f'Saved: {image_name}')
            if image_count == 100:
                print("100 images saved successfully.")
                break

        # Press 'T' to terminate capturing
        elif key == ord('t') or key == ord('T'):
            break

    cap.release()               # Release the video capture initiated initiated early in line 21.
    cv2.destroyAllWindows()     # To destroy all the window used to display the image in the line 28.

# Main function to capture images for different symbols
def main():
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'
               ,'Hello','Thumbsup','Thank_You',
               'Together','Help','I_Love_You','One','two','Three','Four','five']

    for symbol in symbols:
        print(f'Capturing images for symbol: {symbol}')
        capture_images(symbol)
        key = input("Press 'Enter' to capture images for the next symbol or 't' to terminate: ")
        if key.lower() == 't':
            print('Terminating the program.')
            break
    print('Finished capturing images.')

if __name__ == "__main__": # here, only the main fuction is executed.
    main()
