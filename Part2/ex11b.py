def calculate(a, b, c):
    if b == "+":
        return a + c
    
    elif b == "-":
        return a - c
    
    elif b == "*":
        return a * c
    
    elif b == "/":
        return a / c

print(calculate(10, "+", 10))
print(calculate(10, "-", 10))
print(calculate(10, "*", 10))
print(calculate(10, "/", 10))