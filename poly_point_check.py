"""
To check if a point P lies within the N sided polygon:
Step 1: Area of the polygon = sum of area of N-2 triangles formed by the polygon points.
Step 2: Area Covered by P = sum of areas of N triangles formed by P and any two adjasecnt sides of the ploygon.
If areas obtain from step 1 and 2 are equal then P lies with the polygon, else outside.
"""
import sys


def area(point_1, point_2, point_3):
    return abs(point_1[0] * (point_2[1] - point_3[1])
               + point_2[0] * (point_3[1] - point_1[1])
               + point_3[0] * (point_1[1] - point_2[1]))


def get_coordinate(data):
    l = data.split(",")
    return tuple([int(c) for c in l])


def check_within():
    points = []
    c = int(raw_input("Nth sided polygon:: "))
    if c > 4 or c < 3:
        print("Program only works for rectangle and triangles")
        sys.exit(1)
    for i in range(c):
        data = raw_input("Enter the polygon point:: ")
        point = get_coordinate(data)
        points.append(point)
    test_data = raw_input("Enter the point to check:: ")
    test_point = get_coordinate(test_data)
    points.append(test_point)
    if c == 3:
        poly_area = area(points[0], points[1], points[2])
    else:
        poly_area = area(points[0], points[1], points[2]) + \
            area(points[1], points[2], points[3])
    while(True):
        point_area = 0
        if c == 3:
            point_area += area(points[-1], points[0], points[1])
            point_area += area(points[-1], points[0], points[2])
            point_area += area(points[-1], points[1], points[2])
        else:
            point_area += area(points[-1], points[0], points[1])
            point_area += area(points[-1], points[0], points[2])
            point_area += area(points[-1], points[1], points[3])
            point_area += area(points[-1], points[2], points[3])
        if poly_area == point_area:
            print("Point lies with polygon")
        else:
            print("Point does not lies with ploygon")
        print("Lets check another point")
        test_data = raw_input("Enter the point to check:: ")
        test_point = get_coordinate(test_data)
        points[-1] = test_point


def main():
    check_within()

if __name__ == '__main__':
    main()
