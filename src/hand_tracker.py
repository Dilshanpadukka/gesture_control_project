import cv2
import mediapipe as mp
import numpy as np

class HandTracker:
    def __init__(self, detection_confidence=0.7, tracking_confidence=0.7):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, image, draw=True):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image_rgb)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        image,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )
        return image

    def get_hand_position(self, image):
        landmark_list = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[0]
            for id, landmark in enumerate(hand.landmark):
                height, width, _ = image.shape
                cx, cy = int(landmark.x * width), int(landmark.y * height)
                landmark_list.append([id, cx, cy])
        return landmark_list