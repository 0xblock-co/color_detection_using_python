import numpy as np
import cv2

def detect_color(frame):
    cvt = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    color_ranges = {
        'red': ([0, 100, 100], [10, 255, 255]),
        'yellow': ([20, 100, 100], [30, 255, 255]),
        'green': ([40, 100, 100], [80, 255, 255]),
        'cyan': ([80, 100, 100], [100, 255, 255]),
        'blue': ([100, 100, 100], [140, 255, 255]),
        'purple': ([140, 100, 100], [160, 255, 255]),
        'magenta': ([160, 100, 100], [180, 255, 255]),
        'white': ([0, 0, 200], [180, 20, 255]),
        'black': ([0, 0, 0], [180, 255, 30]),
        'white': ([0, 0, 200], [180, 20, 255]),
    }
    detected_color_name = None
    for color_name, (lower, upper) in color_ranges.items():
        lowest = np.array(lower)
        high = np.array(upper)
        mask = cv2.inRange(cvt, lowest, high)
        is_color_find, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if is_color_find:
            detected_color_name = color_name
            break

    return detected_color_name