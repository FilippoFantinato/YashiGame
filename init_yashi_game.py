import pandas
from collections import defaultdict
from typing import Tuple

from yashi_types import Lines, Points, PointsToLine

def init_yashi_game(df: pandas.DataFrame) -> Tuple[Lines, Points, PointsToLine]:
    size = len(df)
    grid = defaultdict(dict)
    points = dict()
    lines = dict()

    # Creating the points and setting them to the grid
    for _, row in df.iterrows():
        p, x, y = row["point"], row["x"], row["y"]
        points[p] = (x, y)
        grid[x][y] = p

    addedLines = defaultdict(bool)
    pointsToLines = defaultdict(dict)

    j = 1  # Line identifier
    for v, (r, c) in points.items():

        # Creating the lines from a point v to the closest point above
        for i in range(r + 1, size):
            u = grid[i].get(c, None)
            if u != None:
                u_v = (u, v) if u <= v else (v, u)
                if not addedLines[u_v]:
                    lines[j] = (v, u)
                    pointsToLines[u][v] = j
                    pointsToLines[v][u] = j
                    addedLines[u_v] = True
                    j += 1
                break

        # Creating the lines from a point v to the closest point below
        for i in range(r - 1, -1, -1):
            u = grid[i].get(c, None)
            if u != None:
                u_v = (u, v) if u <= v else (v, u)
                if not addedLines[u_v]:
                    lines[j] = (v, u)
                    pointsToLines[u][v] = j
                    pointsToLines[v][u] = j
                    addedLines[u_v] = True
                    j += 1
                break

        # Creating the lines from a point v to the closest point to its right
        for i in range(c + 1, size):
            u = grid[r].get(i, None)
            if u != None:
                u_v = (u, v) if u <= v else (v, u)
                if not addedLines[u_v]:
                    lines[j] = (v, u)
                    pointsToLines[v][u] = j
                    pointsToLines[u][v] = j
                    addedLines[u_v] = True
                    j += 1
                break

        # Creating the lines from a point v to the closest point to its left
        for i in range(c - 1, -1, -1):
            u = grid[r].get(i, None)
            if u != None:
                u_v = (u, v) if u <= v else (v, u)
                if not addedLines[u_v]:
                    lines[j] = (v, u)
                    pointsToLines[v][u] = j
                    pointsToLines[u][v] = j
                    addedLines[u_v] = True
                    j += 1
                break

    return lines, points, pointsToLines
