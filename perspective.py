import cv2
import numpy as np

def warp_wall(raw_image):
    # Manually picked corner points (start simple)
    # Order: top-left, top-right, bottom-right, bottom-left
    src_pts = np.array([
        [320, 180],
        [980, 210],
        [1020, 720],
        [300, 700]] , dtype=np.float32)

    width = 800
    height = 500

    dst_pts = np.array(
        [
        [0, 0],
        [width, 0],
        [width, height],
        [0, height]], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warped = cv2.warpPerspective(raw_image, matrix, (width, height))

    # Known real-world measurement (example: red laser width = 2000 mm)
    real_width_mm = 2000
    pixel_width = width
    scale = real_width_mm / pixel_width

    return warped, scale