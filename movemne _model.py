import cv2
import mediapipe as mp

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize MediaPipe Drawing module for visualization
mp_drawing = mp.solutions.drawing_utils

# Initialize the camera (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to RGB (MediaPipe requires RGB input)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect both hands
    results = hands.process(rgb_frame)

    # Create a black frame for hand landmarks
    hand_landmarks_frame = frame * 0

    # If hands are detected, draw landmarks on the hand_landmarks_frame
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Draw landmarks on the hand_landmarks_frame
            mp_drawing.draw_landmarks(hand_landmarks_frame, landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the original frame with hand landmarks in a separate window
    cv2.imshow("Original Frame with Hand Landmarks", frame)

    # Display the hand_landmarks_frame in a separate window with a black background
    cv2.imshow("Hand Landmarks on Black Background", hand_landmarks_frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
