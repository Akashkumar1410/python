import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the pre-trained face, right eye, left eye, and smile detection models
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
right_eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_righteye_2splits.xml')
left_eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lefteye_2splits.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Load your trained Keras models for age prediction
male_age_model = load_model('male_age_model.keras')  # Replace with the path to your male_age_model
female_age_model = load_model('female_age_model.keras')  # Replace with the path to your female_age_model

# Initialize the camera (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Open the camera feed in full screen
cv2.namedWindow("Face and Feature Detection", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Face and Feature Detection", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to grayscale for face and feature detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Loop through the detected faces
    for (x, y, w, h) in faces:
        # Draw a green rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Define regions of interest (ROI) for right eye, left eye, and smile within the face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect right eye within the face
        right_eyes = right_eye_cascade.detectMultiScale(roi_gray)
        for (rex, rey, rew, reh) in right_eyes:
            # Draw blue rectangles for right eyes
            cv2.rectangle(roi_color, (rex, rey), (rex + rew, rey + reh), (255, 0, 0), 2)

        # Detect left eye within the face
        left_eyes = left_eye_cascade.detectMultiScale(roi_gray)
        for (lex, ley, lew, leh) in left_eyes:
            # Draw red rectangles for left eyes
            cv2.rectangle(roi_color, (lex, ley), (lex + lew, ley + leh), (0, 0, 255), 2)

        # Detect smiles within the face
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))
        for (sx, sy, sw, sh) in smiles:
            # Draw yellow rectangles for smiles
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 255), 2)

        # Crop and resize the detected face region for age prediction
        face_image = cv2.resize(roi_color, (64, 64))
        face_image = np.expand_dims(face_image, axis=0)  # Add batch dimension

        # Predict ages using both male and female age models
        predicted_male_age = male_age_model.predict(face_image)[0][0]
        predicted_female_age = female_age_model.predict(face_image)[0][0]

        # Decide gender based on age predictions
        predicted_gender = "Male" if predicted_male_age < predicted_female_age else "Female"

        # Display predicted gender and age on the frame
        cv2.putText(frame, f"Predicted Gender: {predicted_gender}", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.putText(frame, f"Predicted Age: {predicted_female_age:.2f} years", (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the frame with rectangles and predictions
    cv2.imshow("Face and Feature Detection", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
