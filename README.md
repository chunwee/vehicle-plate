# Classification of Vehicles in Singapore

**3 Components:**
1. Automatic Number-Plate Recognition (ANPR)
2. Optical Character Recognition (OCR)
3. Classification

## ANPR
A custom model for number plates was trained using [yolov7](https://github.com/WongKinYiu/yolov7): [<code>carplate.pt</code>](https://github.com/chunwee/vehicle-plate/blob/main/carplate.pt)
The dataset used in the model was divided into 70:20:10 (Train:Test:Validation) splits.


## OCR
OCR was done using [PaddleOCR toolkit](https://github.com/PaddlePaddle/PaddleOCR).

## Classification
Classification was done using a simple regex script that takes in strings from the OCR and split them into categories based on different characteristics.

Categories include:
- S-plate cars
- E-plate cars
- Motorcycles
- Light goods vehicles
- Private hire vehicles
- Heavy goods vehicles (Class 3)
- Heavy goods vehicles (Class 4 or 5)
