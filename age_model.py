import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import os
from PIL import Image
import pandas as pd

# Define the path to your image directory
image_directory = "unsamples"

# Load image data from the image directory and resize them to (64, 64)
loaded_images = []
for filename in os.listdir(image_directory):
    if filename.endswith(".jpg"):
        image = Image.open(os.path.join(image_directory, filename))
        image = image.resize((64, 64))
        loaded_images.append(np.array(image))

# Convert the list of resized images into a NumPy array
images = np.array(loaded_images)

# Load age and gender labels from a CSV file (assuming 'age_gender.csv' contains age and gender labels)
age_gender_data = pd.read_csv('age_gender.csv')  # Replace with your CSV file path
ages = age_gender_data['age'].values
genders = age_gender_data['gender'].values  # Numeric values (0 for female and 1 for male)

# Separate the data into males and females based on numeric values
male_indices = np.where(genders == 1)[0]
female_indices = np.where(genders == 0)[0]

X_male = images[male_indices]
y_male = ages[male_indices]

X_female = images[female_indices]
y_female = ages[female_indices]

# Rest of the code remains the same as before
# ...




# Define a function to create a CNN model for age prediction
def create_age_model(input_shape):
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='linear')
    ])
    return model


# Function to train and evaluate models for a specific gender
def train_and_evaluate(X, y, gender):
    input_shape = (64, 64, 3)

    # Create a model
    model = create_age_model(input_shape)

    # Compile the model
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error', metrics=['mae'])

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    batch_size = 32
    epochs = 20
    model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(X_test, y_test))

    # Evaluate the model
    loss, mae = model.evaluate(X_test, y_test)

    print(f'{gender} Test MAE: {mae}')

    return model


# Train and evaluate models for males and females separately if there is enough data
if len(X_male) >= 2:
    model_male = train_and_evaluate(X_male, y_male, 'Male')

if len(X_female) >= 2:
    model_female = train_and_evaluate(X_female, y_female, 'Female')




# Load a sample image and preprocess it
sample_image = Image.open('ak.jpg')  # Replace with the path to your sample image
sample_image = sample_image.resize((64, 64))  # Resize the image to (64, 64)
sample_image = np.array(sample_image)
sample_image = sample_image.reshape(1, 64, 64, 3)  # Reshape to match model input shape

# Make age predictions using the male and female models
predicted_male_age = model_male.predict(sample_image)
predicted_female_age = model_female.predict(sample_image)

# Determine gender based on age predictions
threshold_age = 25  # Adjust this threshold as needed
is_male = predicted_male_age[0][0] < threshold_age

# Print the predicted gender and corresponding age
if is_male:
    print(f'Predicted Gender: Male')
    print(f'Predicted Male Age: {predicted_male_age[0][0]} years')
else:
    print(f'Predicted Gender: Female')
    print(f'Predicted Female Age: {predicted_female_age[0][0]} years')

# model_male.save('male_age_model.keras')
# model_female.save('female_age_model.keras')
