from tensorflow.keras.models import load_model
import cv2
import numpy as np


class EmotionClassifier:
    def __init__(self, model_path):
        self.model = load_model(model_path)
        self.emotions = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprised']

    def predict_emotion(self, face_img):
        face_img = cv2.resize(face_img, (48, 48))
        face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
        face_img = face_img / 255.0
        face_img = np.expand_dims(face_img, axis=[0, -1])

        prediction = self.model.predict(face_img)
        emotion_idx = np.argmax(prediction)
        emotion = self.emotions[emotion_idx]
        confidence = prediction[0][emotion_idx]

        return emotion, confidence