import unittest
from core.sensors.gps import GPSHandler
from core.sensors.camera import CameraHandler

class TestSensors(unittest.TestCase):
    def test_gps_coordinates(self):
        gps = GPSHandler(port="COM1", baudrate=9600)
        gps_data = gps.get_coordinates()
        self.assertIsNone(gps_data)  # Simulated test; replace with mock data
        gps.close()

    def test_camera_capture_frame(self):
        camera = CameraHandler(camera_index=0, output_dir="data/camera_frames")
        frame_path = camera.capture_frame("test_frame.jpg")
        self.assertIsNotNone(frame_path)
        camera.release()

if __name__ == "__main__":
    unittest.main()

#use the following command to test /// python -m unittest discover -s tests -p "test_*.py" /// or else you will get module error