
# Importing math
import math

# Introducing the user to program
print("I can calculate the area of any triangle using Heron's Formula."
    "\nAll I need is a a bit of information from you.")

# Taking inputs
side_a = input("Input the length of the first side of triangle: ")
side_b = input("Input the length of the second side of triangle: ")
side_c = input("Input the length of the third side of triangle: ")

# Converting inputs from strings into floats
side_a = float(side_a)
side_b = float(side_b)
side_c = float(side_c)

# Doing the actual math
semi_perimeter = ((side_a + side_b + side_c) / 2)

triangle_area = math.sqrt(semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c))

print(f"The area of this triangle is {triangle_area: .2f}")

