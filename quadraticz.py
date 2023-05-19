from sys import argv

print(argv)

_, a, b, c = argv

a = float(a)
b = float(b)
c = float(c)

print(f"Решение уравнеия {a}x^2 + {b}x + {c} = 0:")

def quadratic(a, b, c):
    d = b**2 - 4 * a * c
    return -b / 2 * a if d == 0 else [(-b - d**0.5) / (2 * a), (-b + d**0.5) / (2 * a)]

    
    
print(quadratic(a, b, c))