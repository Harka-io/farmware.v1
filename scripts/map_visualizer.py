import json
import matplotlib.pyplot as plt

def visualize_field_map(map_path):
    with open(map_path, 'r') as f:
        field_map = json.load(f)

    boundaries = field_map.get("boundaries", [])
    rows = field_map.get("rows", [])

    # Extract coordinates for plotting
    boundary_coords = [(b["lat"], b["lng"]) for b in boundaries]
    row_coords = [
        [(p["lat"], p["lng"]) for p in row["coordinates"]]
        for row in rows
    ]

    # Plot the field boundaries
    if boundary_coords:
        lats, lngs = zip(*boundary_coords)
        plt.plot(lngs + (lngs[0],), lats + (lats[0],), 'b-', label='Boundaries')

    # Plot the rows
    for i, row in enumerate(row_coords):
        lats, lngs = zip(*row)
        plt.plot(lngs, lats, 'g--', label=f'Row {i + 1}')

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Field Map Visualization")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    map_path = "data/field_maps/field1.json"
    visualize_field_map(map_path)
