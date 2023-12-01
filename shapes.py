# Calculating Areas of Shapes:

# Area of rectangle: 
print("Area of rectangle:")
rectangle_length = int(input("Enter the length of the rectangle: "))
rectangle_breadth = int(input("Enter the breadth of the rectangle: "))
rectangle_area = float(rectangle_length * rectangle_breadth)
print(f"The area of the rectangle with lenghth {rectangle_length:.1f} and breadth {rectangle_breadth:.1f} is: {rectangle_area:.2f}")
print("")

# Perimeter of rectangle:
print("Perimeter of rectangle:")
rectangle_length = int(input("Enter the length of the rectangle: "))
rectangle_breadth = int(input("Enter the breadth of the rectangle: "))
rectangle_perimeter = float(2 * (rectangle_length + rectangle_breadth))
print(f"The perimeter of the rectangle with lenghth {rectangle_length:.1f} and breadth {rectangle_breadth:.1f} is: {rectangle_perimeter:.2f}")
print("")

# Area of triangle:
print("Area of triangle:")
triangle_base = int(input("Enter the base of the triangle: "))
triangle_height = int(input("Enter the height of the triangle: "))
triangle_area = float((triangle_base * triangle_height) * 0.5)
print(f"The area of triangle with base {triangle_base:.1f} and height {triangle_height:.1f} is: {triangle_area:.2f}")
print("")

# Perimeter of triangle:
print("Perimeter of triangle:")
triangle_base = int(input("Enter the base of the triangle: "))
triangle_height = int(input("Enter the height of the triangle: "))
triangle_width = int(input("Enter the width of triangle: "))
triangle_perimter = float(triangle_base + triangle_height + triangle_width)
print(f"The area of triangle with base {triangle_base:.1f} and height {triangle_height:.1f} and width {triangle_width:.1f} is: {triangle_perimter:.2f}")
print("")

import math

# Area of cirlce: 
print("Area of circle:")
cricle_radius = int(input("Enter the radius of circle: "))
circle_area = float(math.pi * cricle_radius ** 2)
print(f"The area of the circle with radius {cricle_radius:.1f} is: {circle_area:.2f}")
print("")

# Perimeter of cirlce: 
print("Perimeer of circle:")
cricle_radius = int(input("Enter the radius of circle: "))
circle_perimeter = float(2 * math.pi * cricle_radius)
print(f"The area of the circle with radius {cricle_radius:.1f} is: {circle_perimeter:.2f}")
print("")