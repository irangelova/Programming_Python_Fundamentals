from math import floor


def center_point(x1: float, y1: float, x2: float, y2: float):
    point_x = point_y = 0
    distance_x1 = abs(x1 - 0)
    distance_x2 = abs(x2 - 0)
    if distance_x1 <= distance_x2:
        point_x = x1
    else:
        point_x = x2
    distance_y1 = abs(y1 - 0)
    distance_y2 = abs(y2 - 0)
    if distance_y1 <= distance_y2:
        point_y = y1
    else:
        point_y = y2
    return f"({floor(point_x)}, {floor(point_y)})"


coordinate_x1 = float(input())
coordinate_y1 = float(input())
coordinate_x2 = float(input())
coordinate_y2 = float(input())
print(center_point(coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2))
