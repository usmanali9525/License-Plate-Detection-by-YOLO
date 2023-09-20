from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator
import easyocr

reader = easyocr.Reader(['en'])
model = YOLO('best.pt')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() 
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model.predict(img, verbose=False)

    for r in results:
        annotator = Annotator(frame)
        boxes = r.boxes
        
        for box in boxes:
            b = box.xyxy[0]
            c = box.cls
            label = model.names[int(c)]
            plate_roi = frame[int(b[1]):int(b[3]), int(b[0]):int(b[2])]
            
            number_plate_results = reader.readtext(plate_roi)
            number_plate_text = ''
            for result in number_plate_results:
                number_plate_text += result[1] + ' '
            
            print(f"Detected: {label}, Text: {number_plate_text}")
            
            annotator.box_label(b, label)
            
        frame = annotator.result()
        cv2.imshow('YOLO V8 Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()