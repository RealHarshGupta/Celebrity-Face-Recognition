import cv2
import numpy as np
import face_recognition
import joblib
import os
import random

def read_list_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Example usage
label_file_path = "C:/Users/Lenovo/Desktop/celebrity_recogniton/labels_2.txt"
labels = read_list_from_file(label_file_path)

known_labels = np.unique(labels)

def recognize_faces_in_video(video_path, model_path, output_base_folder):
    # Load the trained model
    clf = joblib.load(model_path)
    
    def recognize_faces(frame):
        try:
            # Convert BGR to RGB format (expected by face_recognition)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            # 128-dimensional face_encodings
            
            face_names = []
            for face_encoding in face_encodings:
                # Use the trained SVM model for recognition
                probabilities = clf.predict_proba([face_encoding])[0]
                # 128 array list contains probability of face_encoding with every label
                best_match_index = np.argmax(probabilities)
                # np.argmax returns index of highest probability
                name = known_labels[best_match_index] if probabilities[best_match_index] > 0.5 else "Unknown"
                face_names.append(name)

            return face_locations, face_names
        except Exception as e:
            print("Error during face recognition:", e)

    # Load the video
    video_capture = cv2.VideoCapture(video_path)
    
    # Create a dictionary to store video writers for each recognized name
    video_writers = {}

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break
        
        face_locations, face_names = recognize_faces(frame)
        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Draw rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
            # Draw label
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            
            # Create a new folder for the recognized name if it doesn't exist
            output_folder = os.path.join(output_base_folder, name)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            # Initialize the video writer for this name if not already done
            if name not in video_writers:
                video_name = os.path.basename(video_path)
                output_video_path = os.path.join(output_folder, video_name)
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                video_writers[name] = cv2.VideoWriter(output_video_path, fourcc, 20.0, (int(video_capture.get(3)), int(video_capture.get(4))))

            # Write the frame to the appropriate video writer
            video_writers[name].write(frame)
        
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    for writer in video_writers.values():
        writer.release()
    cv2.destroyAllWindows()

def select_random_video(folder_path):
    # List all video files in the folder
    video_files = [f for f in os.listdir(folder_path)
                   if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.mp4', '.avi', '.mov'))]

    if not video_files:
        print("No video files found in the folder.")
        return None

    # Select a random video file
    selected_video = random.choice(video_files)
    return os.path.join(folder_path, selected_video)

# Example usage:

model_path = "C:/Users/Lenovo/Desktop/celebrity_recogniton/clf.pkl"
folder_path = 'C:/Users/Lenovo/Desktop/celebrity_recogniton/downloded_videos'  # Replace with your folder path
output_base_folder = 'C:/Users/Lenovo/Desktop/celebrity_recogniton/output_videos'  # Base folder for output videos

#video_path = select_random_video(folder_path)
video_path = "C:/Users/Lenovo/Desktop/celebrity_recogniton/downloded_videos/amitabh bachchan giving award to aishwarya rai ｜ Aishwarya touch feet of Amitabh Bachchan.mp4"
recognize_faces_in_video(video_path, model_path, output_base_folder)
