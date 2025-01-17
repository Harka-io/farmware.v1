class PathPlanner:
    def plan_route(self, field_map):
        waypoints = []
        rows = field_map.get("rows", [])
        for row in rows:
            waypoints.extend(row["coordinates"])
        return waypoints
