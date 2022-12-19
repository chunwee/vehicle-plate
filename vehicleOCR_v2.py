# Import libraries
# import pytesseract
import cv2
import v_plate_regex2
# import image_processing
import paddle
# import easygui
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr
import os
import cv2
import glob

# os.chdir("C:/Users/Sean/Desktop/Project/vehicle")
# img = easygui.fileopenbox()

folders = glob.glob('C:/Users/Chun Wee/Desktop/Projects/vehicle-plate/extracted')
image_list = []
for folder in folders:
    for f in glob.glob(folder+'/*.jpg'):
        image_list.append(f)
    print(image_list)

def carplate(img):
    plate_list = []
    for img in image_list:
        # img = image_processing.resize_img(img)
        # img = image_processing.sharp(img)
    
        ocr = PaddleOCR(use_angle_cls=True, lang='en')
        result = ocr.ocr(img, cls=True)
        for line in result:
            print(line)
            if len(line) == 1:
                print('\n', line, '\n')
                print(line[0][1][0])
                plate_list.append(line[0][1][0])
            else:
                temp = line[0][1][0]
                for i in range(1, len(line)):
                    print(line[i][1][0])
                    temp = temp + line[i][1][0]
                plate_list.append(temp)

    print('Car Plates Detected:', plate_list, '\n')

    for carplates in plate_list:
        print("\n", "Detected:", carplates, '\n')
    
    v_plate_regex2.all_vehicles(plate_list)

carplate(image_list)
