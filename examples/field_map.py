import json
from core.sensors.mapping import FieldMapper

def save_field_map(field_map, output_path):
    """Save the mapped field data to a JSON file."""
    with open(output_path, 'w') as f:
        json.dump(field_map, f, indent=4)
    print(f"Field map saved to {output_path}")

def main():
    gps_port = "/dev/ttyUSB0"  # Replace with your GPS port
    camera_index = 0          # Default camera index

    # Initialize field mapper
    field_mapper = FieldMapper(gps_port, camera_index)

    # Map the field
    field_map = field_mapper.map_field()

    # Save the field map
    save_field_map(field_map, "data/field_maps/field1.json")

if __name__ == "__main__":
    main()
