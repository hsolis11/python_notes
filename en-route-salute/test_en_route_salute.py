import unittest
from en_route_salute import solution

class TestEnrouteSalute(unittest.TestCase):

    def test_solution(self):

        test_values = {
            "--->-><-><-->-": 10,
            ">----<": 2,
            "<<>><": 4
        }
        for key, item in test_values.items():
            self.assertEqual(solution(key), item)


if __name__ == '__main__':
    unittest.main()