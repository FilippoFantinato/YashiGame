import matplotlib.pyplot as plt


def sat_plot(lines, points):
    x = []
    y = []

    for r, c in points.values():
        x.append(r)
        y.append(c)

    plt.plot(x, y, "ro")

    for u, v in lines.values():
        (x1, y1), (x2, y2) = points[u], points[v]
        plt.plot([x1, x2], [y1, y2], "k-")
        plt.annotate(u, (x1, y1))
        plt.annotate(v, (x2, y2))

    plt.show()
