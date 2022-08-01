from collections import defaultdict
import unittest

from graph.graph import Graph
from sat.no_cycles import mark_all_cycles


class NoCyclesTests(unittest.TestCase):
    def test_markAllCycles_simplegraph(self):
        g = Graph(
            [
                (5, 4, 2.0),
                (11, 10, 4.0),
                (0, 12, 6.0),
                (13, 7, 3.0),
                (7, 13, 3.0),
                (1, 4, 2.0),
                (8, 11, 2.0),
                (4, 1, 2.0),
                (8, 2, 2.0),
                (4, 3, 2.0),
                (1, 0, 4.0),
                (6, 7, 2.0),
                (2, 8, 2.0),
                (4, 5, 2.0),
                (11, 8, 2.0),
                (12, 0, 6.0),
                (12, 13, 3.0),
                (10, 6, 2.0),
                (7, 6, 2.0),
                (10, 11, 4.0),
                (7, 8, 2.0),
                (14, 13, 3.0),
                (5, 9, 2.0),
                (0, 1, 4.0),
                (9, 14, 2.0),
                (13, 12, 3.0),
                (3, 4, 2.0),
                (6, 10, 2.0),
                (9, 5, 2.0),
                (13, 14, 3.0),
                (14, 9, 2.0),
                (8, 7, 2.0),
            ]
        )

        colors = defaultdict(int)
        parents = defaultdict(lambda: -1)
        mark = defaultdict(int)

        current = mark_all_cycles(g, 0, None, 0, colors, parents, mark)
        expected = 2

        print(mark)

        self.assertEqual(expected, current)


if __name__ == "__main__":
    unittest.main()
