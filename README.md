# License Plate Detection and Recognition
This repository contains Python code for detecting and recognizing license plates in car images using the Roboflow API, OpenCV, and EasyOCR. You can use this code to process images/videos of cars and extract the text from their license plates.

## Prerequisites
Before running the code, make sure you have the following libraries and dependencies installed:

1. Roboflow
2. OpenCV
3. Ultralytics
4. EasyOCR

You can install these dependencies using pip:

```
pip install roboflow opencv-python easyocr, ultralytics
```

## Getting Started
1. Clone this repository to your local machine:
```
git clone https://github.com/usmanali9525/License-Plate-Detection-by-YOLO.git
```
2. Navigate to the project directory:
```
cd License-Plate-Detection-by-YOLO
```
3. Replace 'PATH OF CAR IMAGE' in the code with the path to the image you want to process.

## Usage
### Detection_with_API.ipynb file
1. Run the Detection_with_API.ipynb file.
1. The code will use the Roboflow API to detect the license plate in the specified image and extract the relevant information.
2. The detected license plate text will be displayed in the console.

### Custom_Model_Live_Detection.py file
1 Run the Custom_Model_Live_Detection.py file to initiate the license plate detection system.
2. Upon execution, a camera feed will open, and the system will begin real-time license plate detection from the video stream.
3. The detected license plate number will be displayed on the screen, providing you with the identified information.

## Additional Testing
The "Cars Images" directory in this repository contains multiple images of cars for testing purposes. You can replace the 'PATH OF CAR IMAGE' with the paths to these images to test the code on different car images.

## Notes
The code is set to detect license plates with a confidence threshold of 60% and an overlap of 30%. You can adjust these parameters based on your specific requirements.
Ensure that you have an active internet connection when running the code to use the Roboflow API for license plate detection.

## Acknowledgments
Feel free to use, modify, and distribute this code as needed. If you encounter any issues or have suggestions for improvements, please open an issue or create a pull request. Enjoy using this license plate detection and recognition tool!
