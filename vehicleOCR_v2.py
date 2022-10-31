# Import libraries
# import pytesseract
import cv2
import v_plate_regex2
import image_processing
import paddle
import easygui
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr
import os
import cv2
import glob

# os.chdir("C:/Users/Sean/Desktop/Project/vehicle")
# img = easygui.fileopenbox()

folders = glob.glob('C:/Users/Sean/Desktop/Project/vehicle/extracted')
image_list = []
for folder in folders:
    for f in glob.glob(folder+'/*.jpg'):
        image_list.append(f)

def carplate(img):
    plate_list = []
    for img in image_list:
        img = image_processing.resize_img(img)
        # img = image_processing.sharp(img)
    
        ocr = PaddleOCR(use_angle_cls=True, lang='en')
        result = ocr.ocr(img, cls=True)
        for line in result:
            # print(line[1][0])
            plate_list.append(line[1][0])
    # print(plate_list)

    for carplates in plate_list:
        print("\n", "Detected:", carplates)
    
    v_plate_regex2.all_vehicles(plate_list)

carplate(image_list)
