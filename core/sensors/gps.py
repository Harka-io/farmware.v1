import serial

class GPSHandler:
    """Handles live GPS data collection."""

    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.gps = serial.Serial(port, baudrate, timeout=1)

    def get_coordinates(self):
        """Read GPS coordinates from the device."""
        line = self.gps.readline().decode().strip()
        if line:
            try:
                lat, lng = map(float, line.split(","))
                return {"lat": lat, "lng": lng}
            except ValueError:
                print("Invalid GPS data:", line)
                return None
        return None

    def close(self):
        """Close the GPS connection."""
        self.gps.close()
