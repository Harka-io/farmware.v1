import cv2
import os

class CameraHandler:

    def __init__(self, camera_index=0, output_dir="data/camera_frames"):
        self.camera = cv2.VideoCapture(camera_index)
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def capture_frame(self, frame_name="frame.jpg"):
        ret, frame = self.camera.read()
        if ret:
            filepath = os.path.join(self.output_dir, frame_name)
            cv2.imwrite(filepath, frame)
            print(f"Frame captured: {filepath}")
            return filepath
        else:
            print("Failed to capture frame.")
            return None

    def release(self):
        self.camera.release()
