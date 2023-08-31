import math
from consts import ANGLE


class User:
    STEP = 1/3600 # 1 second

    def __init__(self, height, speed):
        self.fild_of_view = 2 * (float(height) * math.tan(0.5*ANGLE))
        self.distance_of_step = float(speed) * 1000 * self.STEP

    def calculate_distance(self, count_of_frames):
        return (self.distance_of_step * (count_of_frames))
