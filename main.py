import cv2
import numpy as np
from src.hand_tracker import HandTracker
from src.virtual_object import VirtualObject
from src.gesture_detector import GestureDetector
from src.face_detector import FaceDetector
from src.emotion_classifier import EmotionClassifier


def main():
    cap = cv2.VideoCapture(0)

    # Initialize components
    hand_tracker = HandTracker()
    gesture_detector = GestureDetector()
    face_detector = FaceDetector()
    emotion_classifier = EmotionClassifier('models/emotion_model.h5')

    # Create virtual objects
    objects = [
        VirtualObject(100, 100, 100, 100, (255, 0, 0), 'rectangle'),
        VirtualObject(300, 100, 80, 80, (0, 255, 0), 'circle')
    ]

    mode = "menu"  # Initial mode

    while True:
        success, image = cap.read()
        if not success:
            break

        image = cv2.flip(image, 1)

        if mode == "menu":
            # Draw menu
            cv2.putText(image, "Select Mode:", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(image, "1: Gesture Control", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(image, "2: Facial Expression", (50, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('1'):
                mode = "gesture"
            elif key == ord('2'):
                mode = "face"

        elif mode == "gesture":
            image = hand_tracker.find_hands(image)
            landmark_list = hand_tracker.get_hand_position(image)

            if landmark_list:
                is_pinching, pinch_x, pinch_y = gesture_detector.check_pinch(landmark_list)

                for obj in objects:
                    if is_pinching:
                        if obj.contains_point(pinch_x, pinch_y) and not obj.is_grabbed:
                            obj.is_grabbed = True
                            obj.grab_offset_x = pinch_x - obj.x
                            obj.grab_offset_y = pinch_y - obj.y

                        if obj.is_grabbed:
                            obj.update_position(pinch_x, pinch_y)
                    else:
                        obj.is_grabbed = False

                    obj.draw(image)

        elif mode == "face":
            image, faces = face_detector.detect_face(image)

            for (x, y, w, h) in faces:
                face_roi = image[y:y + h, x:x + w]
                if face_roi.size != 0:
                    emotion, confidence = emotion_classifier.predict_emotion(face_roi)

                    # Display emotion and confidence
                    label = f"{emotion}: {confidence:.2f}"
                    cv2.putText(image, label, (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                (0, 255, 0), 2)

        # Show mode and instructions
        cv2.putText(image, f"Mode: {mode.capitalize()}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(image, "Press 'M' for menu", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Interactive System", image)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('m'):
            mode = "menu"

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()