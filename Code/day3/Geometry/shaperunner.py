import shapes as s

try:
    print("Area of circle: ", s.circle_area(-1))
    print("Area of rectangle: ", s.rectangle_properties(10, 13))
except ValueError as e:
    print(print(e.args))
