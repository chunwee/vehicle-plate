# Classification of Vehicles in Singapore

**3 Components:**
1. Automatic Number-Plate Recognition (ANPR)
2. Optical Character Recognition (OCR)
3. Classification

## ANPR
A custom model for number plates was trained using [yolov7](https://github.com/WongKinYiu/yolov7): [<code>carplate.pt</code>](https://github.com/chunwee/vehicle-plate/blob/main/carplate.pt)


## OCR
OCR was done using [PaddleOCR toolkit](https://github.com/PaddlePaddle/PaddleOCR).

## Classification
Classification was done using a simple regex script that takes in strings from the OCR and split them into categories based on different characteristics.
