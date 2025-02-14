import cv2
import numpy as np
import math

def create_video(message:str):
    width, height = 100, 100
    out = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 24, (width, height))
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    x, y = width, height // 2

    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)

    text_size, _ = cv2.getTextSize(message, font, font_scale, font_thickness)
    total_distance = width + text_size[0]
    speed = 1 + total_distance / 72.0

    for t in range(72):
        frame.fill(0)
        x -= math.floor(speed)
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)
        out.write(frame)

    out.release()
