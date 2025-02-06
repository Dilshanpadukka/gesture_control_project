import numpy as np

class GestureDetector:
    def __init__(self, grab_threshold=40):
        self.grab_threshold = grab_threshold

    def check_pinch(self, landmark_list):
        if len(landmark_list) < 21:
            return False, None, None

        thumb_tip = landmark_list[4]
        index_tip = landmark_list[8]

        distance = np.sqrt(
            (thumb_tip[1] - index_tip[1]) ** 2 +
            (thumb_tip[2] - index_tip[2]) ** 2
        )

        is_pinching = distance < self.grab_threshold
        pinch_pos_x = (thumb_tip[1] + index_tip[1]) // 2
        pinch_pos_y = (thumb_tip[2] + index_tip[2]) // 2

        return is_pinching, pinch_pos_x, pinch_pos_y