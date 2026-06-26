from flask import Flask, render_template, request, redirect, send_from_directory
import numpy as np
import json
import uuid
import tensorflow as tf
import os

# ---------------- APP ----------------
app = Flask(__name__)

# ---------------- FOLDER ----------------
UPLOAD_FOLDER = "uploadimages"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------- MODEL ----------------
MODEL_PATH = r"C:\Users\HP\Downloads\Plant-Disease-Recognition-System-main\Plant-Disease-Recognition-System-main\models\plant_disease_recog_model_pwp.keras"

model = tf.keras.models.load_model(
    MODEL_PATH,
    compile=False
)

# ---------------- LABELS ----------------
label = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Background_without_leaves',
    'Blueberry___healthy',
    'Cherry___Powdery_mildew',
    'Cherry___healthy',
    'Corn___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn___Common_rust',
    'Corn___Northern_Leaf_Blight',
    'Corn___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# ---------------- JSON ----------------
with open("plant_disease.json", "r") as file:
    plant_disease = json.load(file)

# ---------------- ROUTES ----------------
@app.route('/uploadimages/<path:filename>')
def uploaded_images(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

# ---------------- IMAGE PROCESS ----------------
def extract_features(image_path):
    image = tf.keras.utils.load_img(image_path, target_size=(160, 160))
    image = tf.keras.utils.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

# ---------------- PREDICTION ----------------
def model_predict(image_path):

    img = extract_features(image_path)

    prediction = model.predict(img)

    predicted_index = int(np.argmax(prediction))

    # SAFE FIX (handles list or dict JSON)
    if isinstance(plant_disease, list):
        result = plant_disease[predicted_index]

    elif isinstance(plant_disease, dict):
        result = plant_disease.get(str(predicted_index), label[predicted_index])

    else:
        result = label[predicted_index]

    return result

# ---------------- UPLOAD ----------------
@app.route('/upload/', methods=['POST', 'GET'])
def uploadimage():

    if request.method == "POST":

        if 'img' not in request.files:
            return "No image uploaded"

        image = request.files['img']

        if image.filename == '':
            return "No selected file"

        unique_name = f"temp_{uuid.uuid4().hex}_{image.filename}"
        image_path = os.path.join(UPLOAD_FOLDER, unique_name)

        image.save(image_path)

        try:
            prediction = model_predict(image_path)

            return render_template(
                'home.html',
                result=True,
                imagepath=f'/uploadimages/{unique_name}',
                prediction=prediction
            )

        except Exception as e:
            return f"Prediction Error: {str(e)}"

    return redirect('/')

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)