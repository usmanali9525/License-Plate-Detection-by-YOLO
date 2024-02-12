from flask import Flask, render_template, request, jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES
from ultralytics import YOLO
import cv2
import easyocr
import re
import os

app = Flask(__name__)

photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "uploads"
configure_uploads(app, photos)

model = YOLO(r'Models\best.pt')
reader = easyocr.Reader(['en'])

def process_image(image_path):
    frame = cv2.imread(image_path)
    resized_img = cv2.resize(frame, (640, 480))
    results = model.predict(resized_img)

    output_data = []

    for r in results:
        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]
            plate_roi = resized_img[int(b[1]):int(b[3]), int(b[0]):int(b[2])]

            number_plate_results = reader.readtext(plate_roi)
            number_plate_text = ''
            for result in number_plate_results:
                text = result[1]
                text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
                number_plate_text += text + ' '

            output_data.append({
                "Plate Coordinates": list(map(int, b)),
                "Number Plate Text": number_plate_text.strip()
            })

    return output_data


@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST" and "photo" in request.files:
        photo = request.files["photo"]
        if photo:
            photo_path = os.path.join("uploads", photos.save(photo))
            results = process_image(photo_path)
            return render_template("result.html", results=results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
