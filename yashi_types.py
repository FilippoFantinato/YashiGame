from typing import Dict, NewType, Tuple

Coordinate = NewType("Coordinate", float)
Point_ID = NewType("Point_ID", int)
Line_ID = NewType("Line_ID", int)

Point = NewType("Point", Tuple[Coordinate, Coordinate])
Line = NewType("Line", Tuple[Point_ID, Point_ID])

Lines = NewType("Lines", Dict[Line_ID, Line])
Points = NewType("Points", Dict[Point_ID, Point])
PointsToLine = NewType("PointsToLine", Dict[Point_ID, Dict[Point_ID, Line_ID]])
