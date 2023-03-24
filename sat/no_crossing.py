from pysat.formula import WCNF

from yashi_types import Line, Lines, Points 


def is_crossing(l1: Line, l2: Line, points: Points) -> bool:
    (l1_p1_x, l1_p1_y), (l1_p2_x, l1_p2_y) = points[l1[0]], points[l1[1]]
    (l2_p1_x, l2_p1_y), (l2_p2_x, l2_p2_y) = points[l2[0]], points[l2[1]]

    if l1_p1_x == l1_p2_x: # Checking if l1 is horizontal
        a_x, b_x = (l2_p1_x, l2_p2_x) if l2_p1_x < l2_p2_x else (l2_p2_x, l2_p1_x)
        if l2_p1_y == l2_p2_y: # Checking if l2 is vertical, otherwise they aren't crossing
            a_y, b_y = (l1_p1_y, l1_p2_y) if l1_p1_y < l1_p2_y else (l1_p2_y, l1_p1_y)
            # Checking if the l1 points are between l2 points
            return (l1_p1_x > a_x and l1_p1_x < b_x) and (
                l2_p1_y > a_y and l2_p1_y < b_y
            )
        else:
            return False
    else:  # l1_p1_y == l1_p2_y, l1 is vertical
        a_y, b_y = (l2_p1_y, l2_p2_y) if l2_p1_y < l2_p2_y else (l2_p2_y, l2_p1_y)
        if l2_p1_x == l2_p2_x: # Checking if l2 is horizontal, otherwise they aren't crossing
            a_x, b_x = (l1_p1_x, l1_p2_x) if l1_p1_x < l1_p2_x else (l1_p2_x, l1_p1_x)
            # Checking if the l1 points are between l2 points
            return (l1_p1_y > a_y and l1_p1_y < b_y) and (
                l2_p1_x > a_x and l2_p1_x < b_x
            )
        else:
            return False


def no_crossing(lines: Lines, points: Points) -> WCNF:
    phi_no_crossing = WCNF()
    items = list(lines.items())
    # Checking if two lines are crossing, 
    # if so append the formula that forces to not use them at once
    for index, (l1_id, l1) in enumerate(items):
        for l2_id, l2 in items[index + 1 :]:
            if is_crossing(l1, l2, points):
                phi_no_crossing.append([-l1_id, -l2_id])

    return phi_no_crossing
