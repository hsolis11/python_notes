import unittest
from elevator_maintenance import solution

class TestElevatorMaintenance(unittest.TestCase):

    def test_solution(self):
        tests = {
            "test1": {
                "input": ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"],
                "solution": ['0.1', '1.1.1', '1.2', '1.2.1', '1.11', '2', '2.0', '2.0.0']
            },
            "test2": {
                "input": ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"],
                "solution": ['1.0', '1.0.2', '1.0.12', '1.1.2', '1.3.3']
            }
        }
        for key in tests.keys():
            self.assertEqual(solution(tests[key]["input"]), tests[key]["solution"])


if __name__ == "__main__":
    unittest.main()