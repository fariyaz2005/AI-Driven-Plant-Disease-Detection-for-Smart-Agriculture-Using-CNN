# AI-Driven Plant Disease Detection for Smart Agriculture Using CNN

AI-Driven Plant Disease Detection for Smart Agriculture Using CNN is a deep learning-based web application that identifies plant diseases from leaf images using Convolutional Neural Networks (CNN). The system helps farmers and agricultural researchers detect plant diseases at an early stage, improving crop health and productivity.

## Project Overview

Plant diseases significantly affect agricultural production and crop quality. Traditional disease diagnosis requires expert knowledge and manual inspection, which can be time-consuming and costly. This project uses Deep Learning and Computer Vision techniques to automatically classify plant diseases from leaf images and provide quick prediction results through a web application.

## Features

* Plant leaf disease prediction using CNN.
* User-friendly web interface.
* Image upload functionality.
* Real-time disease prediction.
* Deep learning-based classification.
* Fast and accurate results.

## Technologies Used

* Python
* TensorFlow
* Keras
* Flask
* NumPy
* Pandas
* Matplotlib
* HTML
* CSS
* Bootstrap

## Project Structure

```text
├── app.py
├── Plant_Disease_Model_Training.ipynb
├── plant_disease.json
├── models/
├── static/
├── templates/
├── uploadimages/
└── README.md
```

## Model Information

The trained CNN model file is not included in this repository because it exceeds GitHub's file size limit.

Download the model from the following Google Drive link:

https://drive.google.com/file/d/1Ond7UzrNOfdAXWedjlZr2sDXYU6MRBuj/view?usp=sharing

Place the downloaded model file inside the `models` folder:

```text
models/
└── plant_disease_recog_model_pwp.keras
```

## Installation

Clone the repository:

```bash
git clone https://github.com/fariyaz2005/AI-Driven-Plant-Disease-Detection-for-Smart-Agriculture-Using-CNN.git

cd AI-Driven-Plant-Disease-Detection-for-Smart-Agriculture-Using-CNN
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Project Workflow

1. Upload a plant leaf image.
2. Preprocess the image.
3. Pass the image to the CNN model.
4. Predict the disease class.
5. Display the prediction result.

## Applications

* Smart Agriculture
* Precision Farming
* Crop Disease Monitoring
* Agricultural Research
* Farmer Assistance Systems

## Future Improvements

* Mobile application integration.
* Real-time camera-based detection.
* Cloud deployment.
* Support for additional crop diseases.

## Author

**Md Fariyaz Rahaman**
B.Tech in Computer Science and Engineering
Aliah University

GitHub: https://github.com/fariyaz2005
Email: [fariyazrohaman8989@gmail.com](mailto:fariyazrohaman8989@gmail.com)

## License

This project is developed for educational and research purposes.

