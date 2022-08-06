import pandas
from collections import defaultdict


def init_yashi_game_sat(df: pandas.DataFrame):
    size = len(df)
    grid = defaultdict(dict)
    points = dict()
    lines = dict()

    for _, row in df.iterrows():
        v, r, c = row["vertex"], row["row"], row["column"]
        points[v] = (r, c)
        grid[r][c] = v

    addedLines = dict()
    pointsToLines = defaultdict(dict)

    j = 1
    for v, (r, c) in points.items():
        for i in range(r + 1, size):
            u = grid[i].get(c, None)
            if u != None:
                u_v = (u, v) if u <= v else (v, u)
                if not addedLines.get(u_v, False):
                    lines[j] = (v, u)
                    pointsToLines[u][v] = j
                    pointsToLines[v][u] = j
                    addedLines[u_v] = True
                    j += 1
                break

        for i in range(r - 1, -1, -1):
            u = grid[i].get(c, None)
            if u != None:
                u_v = (u, v) if u <= v else (v, u)
                if not addedLines.get(u_v, False):
                    lines[j] = (v, u)
                    pointsToLines[u][v] = j
                    pointsToLines[v][u] = j
                    addedLines[u_v] = True
                    j += 1
                break

        for i in range(c + 1, size):
            u = grid[r].get(i, None)
            if u != None:
                u_v = (u, v) if u <= v else (v, u)
                if not addedLines.get(u_v, False):
                    lines[j] = (v, u)
                    pointsToLines[v][u] = j
                    pointsToLines[u][v] = j
                    addedLines[u_v] = True
                    j += 1
                break

        for i in range(c - 1, -1, -1):
            u = grid[r].get(i, None)
            if u != None:
                u_v = (u, v) if u <= v else (v, u)
                if not addedLines.get(u_v, False):
                    lines[j] = (v, u)
                    pointsToLines[v][u] = j
                    pointsToLines[u][v] = j
                    addedLines[u_v] = True
                    j += 1
                break

    return lines, points, pointsToLines
