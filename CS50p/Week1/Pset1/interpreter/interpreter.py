x, y, z = input("Equation: ").split(" ")
x = int(x)
z = int(z)

if y == "/":
    print(float(x / z) * 1.0)
elif y == '*':
    print(float(x * z) * 1.0)
elif y == '-':
    print(float(x - z) * 1.0)
else:
    print(float(x + z) * 1.0)

