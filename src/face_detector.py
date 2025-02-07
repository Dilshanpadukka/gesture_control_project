import cv2
import numpy as np
import mediapipe as mp


class FaceDetector:
    def __init__(self):
        self.mp_face = mp.solutions.face_detection
        self.face_detection = self.mp_face.FaceDetection(min_detection_confidence=0.5)
        self.mp_draw = mp.solutions.drawing_utils

    def detect_face(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.face_detection.process(image_rgb)
        faces = []

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = image.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
                faces.append(bbox)
                cv2.rectangle(image, bbox, (0, 255, 0), 2)

        return image, faces