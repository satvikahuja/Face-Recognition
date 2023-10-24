# Computer Vision Project with Face Recognition

This project focuses on the implementation of face recognition using OpenCV's Local Binary Patterns Histogram (LBPH) in Python, especially within the Google Colab environment. 

## Prerequisites
- Python
- OpenCV
- Google Colab
- PIL

## Overview

The primary operations performed in this project are:
1. Mounting the Google Drive to access datasets.
2. Extracting and reading images from the dataset.
3. Training the LBPH Face Recognizer.
4. Testing the classifier with different images.
5. Real-time face detection and recognition using webcam.

### Files in the Project

1. `main.py`: Contains code for mounting the Google Drive, training the LBPH Face Recognizer, and testing the classifier.
2. `camera.py`: Contains code for real-time face detection using a webcam.
3. `face_recognition.py`: Contains code for real-time face detection and recognition using a webcam.

## Usage

### Training and Testing Classifier (`main.py`)
1. **Mounting Google Drive**: Use the following code to mount your Google Drive and access datasets:
    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    ```

2. **Dataset Format**: The dataset contains face images named in the format `person.id.number.jpg`. This id will be used as the label while training the classifier.

3. **Training the Classifier**: Once the dataset is processed, it will be used to train the LBPH Face Recognizer.

4. **Saving the Classifier**: After training, the classifier is saved as `lbph_classifier.yml` for future use.

5. **Testing the Classifier**: Process the test images, and the predictions alongside expected outputs will be displayed.

### Real-time Face Detection (`camera.py`)
- This is a basic implementation that captures video feed from the default camera (usually the webcam) and detects faces in real-time.
  
- Detected faces are highlighted with a rectangle overlay.

### Real-time Face Recognition (`face_recognition.py`)
- This script captures video feed from the default camera.
  
- It detects and recognizes faces in real-time, showcasing the name of the detected person based on the training data.

- The confidence score for each detected face is also displayed.

## Contributing

Feel free to fork this project, make changes, and create pull requests. Feedback and contributions are always welcome!
