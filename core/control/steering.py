import time

class SteeringController:
    def navigate_to_real(self, waypoint):
        print(f"Navigating to waypoint: {waypoint['lat']}, {waypoint['lng']}")
        time.sleep(2)
        print("Arrived at waypoint.")
