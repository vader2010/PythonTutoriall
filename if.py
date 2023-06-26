n1 = eval(input("enter number1: "))
n2 = eval(input("enter number2: "))

if n1 > n2:
    print(f"{n1} is greater than {n2}")
elif n2 > n1:
    print(f"{n2} is greater than {n1}")
else:
    print(f"{n2} and {n1} are equal")
