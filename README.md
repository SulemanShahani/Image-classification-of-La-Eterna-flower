# Z by HP Unlocked Challenge 4 - Image Classification

![La Eterna](data_cleaned/Train/la_eterna/la_eterna_14.jpg?raw=True "La Eterna") ![Other Flower](data_cleaned/Train/other_flowers/flower_451.jpg?raw=True "Other Flower") ![Other Flower #2](data_cleaned/Train/other_flowers/flower_151.jpg?raw=True "Other Flower #2")

## Project Overview
This project is my submission for Z by HP Unlocked Challenge 4 - Image Classification. The challenge involves building a machine learning model to classify images of "La Eterna", a specific flower captured by Eva.

## Background
The challenge was part of the Z by HP Unlocked interactive film series, designed for data scientists to sharpen their skills and solve data-driven mysteries. This particular challenge required participants to develop an image classifier using artificial neural networks (ANN).

## Data
The dataset provided for training and testing consists of images categorized into two folders:
- **la_eterna**: Contains images of La Eterna.
- **other_flowers**: Includes images of various other flowers that are not La Eterna.

Each image in the dataset has been preprocessed and formatted to the dimensions (224, 224, 3) for analysis.

## Methodology


1. **Data Preparation**: I used the provided dataset and split it into training and validation sets.
   
3. **Model Development**: I built an image classification model using TensorFlow and Keras. The model architecture included convolutional layers followed by pooling and fully connected layers.
   
4. **Training**: I trained the model on the training data and validated its performance using the validation set. I used techniques like data augmentation to improve generalization.
   
5. **Evaluation**: I evaluated the model's performance on the provided submission set to ensure its effectiveness in classifying La Eterna flowers.
   
6. **Deployment**: I deployed the trained model using Flask, creating a simple web application where users can upload images to get predictions on whether they depict La Eterna or other flowers.

## Results
The trained model achieved satisfactory performance in classifying La Eterna flowers from other types of flowers. It demonstrated robustness and accuracy in its predictions.



## Contact Information
For inquiries or collaborations, feel free to reach out to me via email or LinkedIn. Thank you for considering my submission!

---

**Your Name**   Muhammad Suleman
LinkedIn: https://www.linkedin.com/in/muhammadsulemanneduet/
**Email:** muhammadsuleman94@hotmail.com
