from flask import Flask, render_template, request
from tensorflow.keras.models import load_model # type: ignore
import numpy as np
import cv2
import os
import nbformat # type: ignore
from nbconvert.preprocessors import ExecutePreprocessor # type: ignore

app = Flask(__name__)

# Function to execute a Jupyter notebook
def execute_notebook(notebook_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': './'}})
    return nb

# Path to your Jupyter notebook source file
notebook_path = 'juptersourcefile.ipynb'  # Update with the correct path

# Execute the notebook to convert the model
execute_notebook(notebook_path)

# Load the trained model
model = load_model('model_a.h5')  # Assuming your trained model is saved as 'model.h5' in the data_cleaned directory

# Save the model as HDF5 format in the data_cleaned directory
model.save('deployable_model_a.h5')

# Define function to preprocess uploaded image
def preprocess_image(image):
    # Resize image to match model input shape (224, 224)
    image = cv2.resize(image, (224, 224))
    # Preprocess image (e.g., rescale pixel values)
    image = image.astype('float32') / 255.0
    # Add batch dimension
    image = np.expand_dims(image, axis=0)
    return image

# Map numerical predictions to class labels
class_labels = {0: 'la_eterna', 1: 'other_flower'}


# Define route for main page
@app.route('/')
def index():
    return render_template('index.html')

# Define route for image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Check if request contains file
    if 'file' not in request.files:
        return "No file uploaded"
    file = request.files['file']
    # Read image file
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
    # Preprocess image
    preprocessed_image = preprocess_image(image)
    # Make prediction
    prediction = model.predict(preprocessed_image)
    # Map numerical predictions to class labels
    predicted_label = class_labels[np.argmax(prediction)]
    # Return prediction
    return predicted_label

if __name__ == '__main__':
    app.run(debug=True)
