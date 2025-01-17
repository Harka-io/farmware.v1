import json
from core.navigation.planner import PathPlanner
from core.sensors.mapping import FieldMapper
from core.control.steering import SteeringController
from core.control.sprayer import SprayerController

def load_config(config_path):
    """Load configuration from a JSON file."""
    with open(config_path, 'r') as f:
        return json.load(f)

def run_simulation():
    # Load configurations
    config = load_config("data/config.json")
    print("Configuration loaded:", config)

    # Initialize components
    field_mapper = FieldMapper()
    path_planner = PathPlanner()
    steering_controller = SteeringController()
    sprayer_controller = SprayerController(config["spray_rate"], config["tank_capacity"])

    # Step 1: Map the field
    print("Mapping the field...")
    field_map = field_mapper.map_field()
    print("Field map created:", field_map)

    # Step 2: Plan the route
    print("Planning the route...")
    route = path_planner.plan_route(field_map)
    print("Route planned:", route)

    # Step 3: Execute the route
    print("Executing the route...")
    for waypoint in route:
        steering_controller.navigate_to(waypoint)
        sprayer_controller.spray()

    print("Simulation completed successfully!")

if __name__ == "__main__":
    run_simulation()
