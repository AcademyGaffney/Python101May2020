
PI = 3.14159


def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be less than zero")
    return PI*radius*radius


def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
