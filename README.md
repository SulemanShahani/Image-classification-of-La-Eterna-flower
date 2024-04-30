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
I approached the challenge by following these steps:
1. **Data Preparation**: I used the provided dataset and split it into training and validation sets.
2. **Model Development**: I built an image classification model using TensorFlow and Keras. The model architecture included convolutional layers followed by pooling and fully connected layers.
3. **Training**: I trained the model on the training data and validated its performance using the validation set. I used techniques like data augmentation to improve generalization.
4. **Evaluation**: I evaluated the model's performance on the provided submission set to ensure its effectiveness in classifying La Eterna flowers.
5. **Deployment**: I deployed the trained model using Flask, creating a simple web application where users can upload images to get predictions on whether they depict La Eterna or other flowers.

## Results
The trained model achieved satisfactory performance in classifying La Eterna flowers from other types of flowers. It demonstrated robustness and accuracy in its predictions.

## Future Improvements
In the future, I aim to enhance the model's performance by exploring advanced techniques such as transfer learning, fine-tuning, and ensembling. Additionally, I plan to incorporate user feedback and further refine the web application interface for a seamless user experience.

## Conclusion
Participating in Z by HP Unlocked Challenge 4 was an enriching experience that allowed me to apply my machine learning skills to a real-world problem. I'm excited about the potential impact of this project and look forward to further refining and expanding it in the future.

## Repository
The code and related resources for this project are available in my GitHub repository: [Z by HP Unlocked Challenge 4 - Image Classification](https://github.com/sulemanshahani/image-classification-of-la-eterna)

## Contact Information
For inquiries or collaborations, feel free to reach out to me via email or LinkedIn. Thank you for considering my submission!

---

**Your Name**  
**Email:** csspreparation1994@gmail.com
