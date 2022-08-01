from pysat.formula import CNF


def no_crossing(lines, points):
    phi_no_crossing = CNF()
    items = lines.items()
    for i, l1 in items:
        for j, l2 in items[i + 1 :]:
            if is_crossing(l1, l2, points):
                phi_no_crossing.append([i, j])
                phi_no_crossing.append([-i, -j])

    return phi_no_crossing


def is_crossing(l1, l2, points) -> bool:
    (l1_p1_x, l1_p1_y), (l1_p2_x, _) = points[l1[0]], points[l1[1]]
    (l2_p1_x, l2_p1_y), (l2_p2_x, l2_p2_y) = points[l2[0]], points[l2[1]]

    if l1_p1_x == l1_p2_x:
        a, b = (l2_p1_x, l2_p2_x) if l2_p1_x < l2_p2_x else (l2_p2_x, l2_p1_x)
        return l1_p1_x >= a and l1_p1_x <= b
    else:  # l1_p1_y == l1_p2_y
        a, b = (l2_p1_y, l2_p2_y) if l2_p1_y < l2_p2_y else (l2_p2_y, l2_p1_y)
        return l1_p1_y >= a and l1_p1_y <= b
