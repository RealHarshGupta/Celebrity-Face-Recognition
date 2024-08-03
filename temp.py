import os
#import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import face_recognition
import joblib
from sklearn.metrics import classification_report

def load_images_from_folder(folder):
    images = []
    labels = []
    for label in os.listdir(folder):
      label_folder = os.path.join(folder, label)
      if not os.path.isdir(label_folder):
        continue
      print('working on :',label)
      for filename in os.listdir(label_folder):
        img_path = os.path.join(label_folder, filename)
        img = face_recognition.load_image_file(img_path)
        face_locations = face_recognition.face_locations(img)  # Find faces in the image
        if len(face_locations) > 0:
          # Only process images with faces
          face_encoding = face_recognition.face_encodings(img, face_locations)[0]  # Get encoding for the first face
          images.append(face_encoding)
          labels.append(label)
    return images, labels
    # ... function code ...

def train_model(dataset_folder, model_path):
    image_encodings, labels = load_images_from_folder(dataset_folder)
    print('images are loaded')

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(image_encodings, labels, test_size=0.2, random_state=42)

    # Train SVM model
    clf = svm.SVC(kernel='linear', probability=True)
    clf.fit(X_train, y_train)

    # Test the model
    y_pred = clf.predict(X_test)
    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
    print(print(classification_report(y_test,y_pred)) )

    # Save the trained model
    joblib.dump(clf, model_path)
    print('training done and model saved')
    return labels

    # ... training code ...

# Example usage:
dataset_folder = "C:/Users/Lenovo/Desktop/celebrity_recogniton/bollywood_celeb_faces_0"
dataset_folder_2 = "C:/Users/Lenovo/Desktop/celebrity_recogniton/celebs"
model_path = "C:/Users/Lenovo/Desktop/celebrity_recogniton/clf.pkl"
labels = train_model(dataset_folder, model_path)

def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")

label_file_path = "C:/Users/Lenovo/Desktop/celebrity_recogniton/labels_2.txt"


write_list_to_file(label_file_path, labels)

