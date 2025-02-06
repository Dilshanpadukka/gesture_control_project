import cv2


class VirtualObject:
    def __init__(self, x, y, width, height, color, shape='rectangle'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.shape = shape
        self.is_grabbed = False
        self.grab_offset_x = 0
        self.grab_offset_y = 0

    def draw(self, image):
        if self.shape == 'rectangle':
            cv2.rectangle(
                image,
                (self.x, self.y),
                (self.x + self.width, self.y + self.height),
                self.color,
                cv2.FILLED
            )
        elif self.shape == 'circle':
            cv2.circle(
                image,
                (self.x + self.width // 2, self.y + self.height // 2),
                min(self.width, self.height) // 2,
                self.color,
                cv2.FILLED
            )

    def contains_point(self, x, y):
        return (self.x <= x <= self.x + self.width and
                self.y <= y <= self.y + self.height)

    def update_position(self, x, y):
        self.x = x - self.grab_offset_x
        self.y = y - self.grab_offset_y