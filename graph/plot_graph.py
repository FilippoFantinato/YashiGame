import matplotlib.pyplot as plt


def plot_yashi_grid(G, yashi_dict):
    x = []
    y = []

    for _, (r, c) in yashi_dict.items():
        x.append(r)
        y.append(c)

    plt.plot(x, y, "ro")

    def connect_points(x, y, p1, p2):
        x1, x2 = x[p1], x[p2]
        y1, y2 = y[p1], y[p2]
        plt.plot([x1, x2], [y1, y2], "k-")

    for s, t, _ in G.get_edges():
        connect_points(x, y, s, t)

    plt.show()
