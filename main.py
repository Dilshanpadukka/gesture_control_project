import cv2
import numpy as np
from src.hand_tracker import HandTracker
from src.virtual_object import VirtualObject
from src.gesture_detector import GestureDetector


def main():
    # Initialize components
    cap = cv2.VideoCapture(0)
    hand_tracker = HandTracker()
    gesture_detector = GestureDetector()

    # Create virtual objects
    objects = [
        VirtualObject(100, 100, 100, 100, (255, 0, 0), 'rectangle'),
        VirtualObject(300, 100, 80, 80, (0, 255, 0), 'circle'),
        VirtualObject(500, 100, 120, 120, (0, 0, 255), 'rectangle')
    ]

    while True:
        success, image = cap.read()
        if not success:
            break

        # Flip image horizontally for more intuitive interaction
        image = cv2.flip(image, 1)

        # Detect hand and landmarks
        image = hand_tracker.find_hands(image)
        landmark_list = hand_tracker.get_hand_position(image)

        if landmark_list:
            # Check for pinch gesture
            is_pinching, pinch_x, pinch_y = gesture_detector.check_pinch(landmark_list)

            # Handle object interaction
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

                # Draw object
                obj.draw(image)

        # Draw all objects
        for obj in objects:
            obj.draw(image)

        # Display
        cv2.imshow("Gesture Drag and Drop", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()