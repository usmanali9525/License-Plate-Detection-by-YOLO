from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator
import easyocr
import re

reader = easyocr.Reader(['en'])
model = YOLO(r'Models\best.pt')

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

            plate_roi = frame[int(b[1]):int(b[3]), int(b[0]):int(b[2])]

            number_plate_results = reader.readtext(plate_roi)
            number_plate_text = ''
            for result in number_plate_results:
                text = result[1]

                text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
                number_plate_text += text + ' '

            cv2.putText(frame, number_plate_text, (int(b[0]), int(b[1]) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            annotator.box_label(b)

        frame = annotator.result()
        cv2.imshow('YOLO V8 Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break


cap.release()
cv2.destroyAllWindows()