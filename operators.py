from math import pi

number1 = eval(input("Enter number1: "))
number2 = eval(input("Enter number2: "))
diameter = eval(input("Enter diameter: "))
side1 = eval(input("Enter side1: "))
side2 = eval(input("Enter side2: "))
radius = diameter/2
radius_squared = radius*radius

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
modulo = number1 % number2
rounded_division = number1 // number2

print(f"{number1} + {number2} = {addition}")
print(f"{number1} - {number2} = {subtraction}")
print(f"{number1} * {number2} = {multiplication}")
print(f"{number1} / {number2} = {division}")
print(f"{number1} % {number2} = {modulo}")
print(f"{number1} // {number2} = {rounded_division}")
print(f"Area of Circle: {round((2*pi*radius_squared)/2)}")
print(f"Area of Rectangle: {side1*side2}")
