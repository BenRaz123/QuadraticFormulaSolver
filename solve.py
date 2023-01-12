from math import sqrt

a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))


def quadratic(a, b, c):
    x1 = -b / (2 * a)
    x2 = sqrt(b**2 - 4 * a * c) / (2 * a)
    return (x1 + x2), (x1 - x2)


print(f"For {a}x^2+{b}x+{c}=0, x=", quadratic(a, b, c))
