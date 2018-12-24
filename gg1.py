def triangleValidator (side1, side2 , side3):
    if side1 <=0 or side2<=0 or side3<=0:
        return False
    elif (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2):
        return True
    return False


def triangleType (side1, side2, side3):
    if triangleValidator(side1, side2, side3) == False:
        return "Not A Triangle"
    if side1 == side2 == side3:
        return "Equilateral Triangle"
    elif (side1 == side2) or (side2 == side3) or (side3 == side1):
        return "Isoceles Triangle"
    return "Scalar Triangle"

assert (triangleType(6,7,8).lower() == "scalar triangle")
assert (triangleType(6,6,6).lower() == "equilateral triangle")
assert (triangleType(6,7,6).lower() == "isoceles triangle")
assert (triangleType(0,0,0).lower() == "not a triangle")
assert (triangleType(-6,-7,-8).lower() == "not a triangle")
assert (triangleType(5,3,8).lower() == "not a triangle")

