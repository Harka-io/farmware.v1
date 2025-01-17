import unittest
from core.navigation.planner import PathPlanner

class TestNavigation(unittest.TestCase):
    def test_plan_route(self):
        planner = PathPlanner()
        field_map = {
            "rows": [
                {"id": 1, "coordinates": [{"lat": 49.12345, "lng": -123.12345}, {"lat": 49.12350, "lng": -123.12350}]},
                {"id": 2, "coordinates": [{"lat": 49.12351, "lng": -123.12351}, {"lat": 49.12356, "lng": -123.12356}]}
            ]
        }
        route = planner.plan_route(field_map)
        expected_route = [
            {"lat": 49.12345, "lng": -123.12345}, {"lat": 49.12350, "lng": -123.12350},
            {"lat": 49.12351, "lng": -123.12351}, {"lat": 49.12356, "lng": -123.12356}
        ]
        self.assertEqual(route, expected_route)

if __name__ == "__main__":
    unittest.main()

#use the following command to test /// python -m unittest discover -s tests -p "test_*.py" /// or else you will get module error