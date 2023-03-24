import matplotlib.pyplot as plt

from yashi_types import Lines, Points

def yashi_plot(lines: Lines, points: Points, title=""):
    x = []
    y = []

    # Plotting all the points  
    for name in points:
        r, c = points[name]
        x.append(r)
        y.append(c)
        plt.annotate(name, (r, c))

    plt.plot(x, y, "ro")

    # Plotting all the lines
    for u, v in lines.values():
        (x1, y1), (x2, y2) = points[u], points[v]
        plt.plot([x1, x2], [y1, y2], "k-")

    plt.title(title)
    plt.grid(True)
    plt.show()